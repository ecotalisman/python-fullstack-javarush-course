"""
WSGI configuration for the myproject project.

This file is used to deploy the project on a server through WSGI.
"""

import os
from django.core.wsgi import get_wsgi_application

# Set the environment variable for Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

# Get the Django WSGI application
application = get_wsgi_application()