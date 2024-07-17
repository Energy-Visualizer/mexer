from django.apps import AppConfig


class EvizConfig(AppConfig):
    """ Configuration class for the 'eviz' Django application"""
    default_auto_field = 'django.db.models.BigAutoField'
    # The name of the app. This should match the name of the directory containg the app's code
    name = 'eviz'
