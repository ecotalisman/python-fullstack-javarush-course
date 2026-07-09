"""
ASGI configuration for the Django project.
"""
import os
from django.core.asgi import get_asgi_application

# Set the environment variable for the project settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

application = get_asgi_application()