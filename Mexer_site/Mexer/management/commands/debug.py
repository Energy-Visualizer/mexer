from django.core.management.commands.runserver import Command as BaseRunServer
from django.conf import settings

# Class must be named exactly "Command"
class Command(BaseRunServer):
    help = "Run in debug mode. Do NOT use in production"

    def handle(self, *args, **options):
        settings.DEBUG = True

        super().handle(*args, **options)
