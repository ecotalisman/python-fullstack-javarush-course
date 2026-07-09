"""
ASGI configuration for the myproject project.

This module is used to deploy the application through ASGI servers.
"""
import os
from django.core.asgi import get_asgi_application

# Set the environment variable specifying the settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

# Get the ASGI application that will handle requests
application = get_asgi_application()