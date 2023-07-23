import threading

from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.translation import ugettext as _
from django.conf import settings
from django.contrib.auth import get_user_model
import jwt

class CurrentUserMiddleware:
    """
    Middleware to load the user accessing the current thread into a local
    memory.

    Richard, 23.05.2023
    """
    __users = {}

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request = self.process_request(request)
        response = self.get_response(request)
        return response

    def process_request(self, request):
        """
        Store User into current thead when processing a request.
        """
        from django.contrib.auth.middleware import get_user
        request.user = get_user(request)
        
        httpAuthorization = request.headers.get('Authorization')
        if httpAuthorization:
            token = httpAuthorization.split(' ')[1]
            decoded_payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.JWT_AUTH['JWT_ALGORITHM']])
            user_id = decoded_payload['user_id']
            request.user.id = user_id
            userModel = get_user_model()
            request.user = userModel.objects.get(uuid=user_id)
            
        if request.user.is_authenticated:
            self.__class__.set_user(request.user)

        return request

    def process_response(self, get_response):
        """
        Delete User from current thread when the request is complete.
        """
        self.__class__.clear_user()
        return get_response

    def process_exception(self, request, exception):
        """
        If there is an exception, clear the current User.
        """
        self.__class__.clear_user()

    @classmethod
    def get_user(cls, default=None):
        """
        Retrieve User from the current thread.
        """
        user = cls.__users.get(threading.current_thread(), default)
        return user

    @classmethod
    def set_user(cls, user):
        """
        Store User into the current thread.
        """
        cls.__users[threading.current_thread()] = user

    @classmethod
    def clear_user(cls):
        """
        Clear User from the current thread.
        """
        cls.__users.pop(threading.current_thread(), None)


def get_current_user():
    """
    Return the current User from the CurrentUserMiddleware
    """
    return CurrentUserMiddleware.get_user()


class ForceChangePasswordMiddleware:
    """
    Middleware to force user to change password

    Richard, 23.05.2023
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        redirect_url = reverse('auths:change-password')
        if (
            request.user.is_authenticated and request.user.force_change_password and
            redirect_url != request.get_full_path()
        ):
            messages.add_message(
                request, messages.ERROR, _(
                    'Please change your password to continue'
                )
            )
            return HttpResponseRedirect(redirect_url)

        return response
