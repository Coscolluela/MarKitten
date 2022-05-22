from django.apps import AppConfig


class MarkittenAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'markitten_app'

    #automatically create profile of registered user by invoking signals.py
    # def ready(self):
    #     import markitten_app.signals