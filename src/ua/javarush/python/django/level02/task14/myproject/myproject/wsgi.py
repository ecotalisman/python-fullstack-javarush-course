"""
WSGI configuration for the myproject project.

Exporting the application variable for the WSGI server.
"""
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

application = get_wsgi_application()