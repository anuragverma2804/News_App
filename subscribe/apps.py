from django.apps import AppConfig
from django.conf import settings


class SubscribeConfig(AppConfig):
    name = 'subscribe'

    # def ready(self):
# from . import scheduler
# if settings.SCHEDULER_AUTOSTART:
#     scheduler.scheduler.start()
