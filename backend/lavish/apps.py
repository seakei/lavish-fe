from django.apps import AppConfig


class LavishConfig(AppConfig):
    name = 'lavish'

    def ready(self):
        # Don't remove this!!!
        import lavish.signals  # noqa
