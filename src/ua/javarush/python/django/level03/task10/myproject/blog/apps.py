from django.apps import AppConfig

# Configuration for the blog application
class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'