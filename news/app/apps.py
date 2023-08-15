from django.apps import AppConfig


class AppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app'

    def ready(self):
        from . import signals
        from .scheduler import scheduler
        print('def ready...OK! import...OK! Started from apps.py!')
        scheduler.start()

