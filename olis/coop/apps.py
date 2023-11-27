from django.apps import AppConfig


default_app_config = 'coop.app.CoopAppConfig'


class CoopConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "coop"
    
