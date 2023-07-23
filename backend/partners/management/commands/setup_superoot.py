import logging

from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.db import transaction

from partners.models import (
    BusinessPartner, Hierarchy
)

from partners.const import (
    PERSON, ADMINISTRATOR, VERIFIED
)

logger = logging.getLogger(__name__)

UserModel = get_user_model()


class Command(BaseCommand):
    """
    Setup Superoot
    """
    help = "Create Superoot user"

    def add_arguments(self, parser):
        parser.add_argument(
            '--commit',
            '-c',
            action='store_true',
            dest='commit',
            default=False,
            help="Confirmation"
        )

    def setup_superoot(self):
        kwargs = {
            'username': 'superoot',
            'email': 'superoot@lavishfilm.com',
            'password': 'lavishfilm!@#2023',
            'is_active': True,
            'is_staff': True,
            'is_superuser': True,
            'first_name': 'Super',
            'last_name': 'Root'
        }

        user = UserModel.objects.create_user(**kwargs)

        partner = BusinessPartner.objects.create(
            category=PERSON,
            email=kwargs['email'],
            name='Super Root',
            user=user,
            role=ADMINISTRATOR,
            profile_status=VERIFIED,
        )
        Hierarchy.add_root(partner=partner)

    @transaction.atomic
    def handle(self, **options):
        sid = transaction.savepoint()

        self.setup_superoot()

        if options['commit']:
            logger.info(self.style.SUCCESS("Successful commit"))
            transaction.savepoint_commit(sid)
        else:
            logger.info(self.style.WARNING("Successful dry-run"))
            transaction.savepoint_rollback(sid)
