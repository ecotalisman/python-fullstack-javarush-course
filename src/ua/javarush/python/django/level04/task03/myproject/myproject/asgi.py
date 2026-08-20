"""
ASGI config for the myproject project.

The module provides an ASGI callable that allows the application to be run through an ASGI server.
"""
import os
from django.core.asgi import get_asgi_application

# Set the project settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
application = get_asgi_application()