"""
WSGI config for the myproject project.

The module provides a WSGI callable that WSGI servers use to serve the project.
"""
import os
from django.core.wsgi import get_wsgi_application

# Set the project settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
application = get_wsgi_application()