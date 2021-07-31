from django.apps import AppConfig

dict_hash = None
max_id = None

class UrlshortnerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'urlshortner'
    def ready(self):
        global dict_hash
        global max_id
        dict_hash = {}
        max_id = 0
        
