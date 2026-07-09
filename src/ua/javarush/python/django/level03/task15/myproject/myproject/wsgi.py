"""
WSGI config for myproject.

This file serves as the entry point for WSGI servers to run the application.
"""

import os
from django.core.wsgi import get_wsgi_application

# Set the environment variable for the project settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

application = get_wsgi_application()