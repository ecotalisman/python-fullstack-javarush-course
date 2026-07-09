"""
WSGI configuration for the myproject project.

This module is used to deploy the application on WSGI servers.
"""
import os
from django.core.wsgi import get_wsgi_application

# Set the environment variable with the project settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

# Get the WSGI application that will handle requests
application = get_wsgi_application()