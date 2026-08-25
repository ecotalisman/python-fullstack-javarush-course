"""
WSGI configuration for the Django project.
Used for deploying the application on a WSGI server.
"""
import os
from django.core.wsgi import get_wsgi_application

# Set the project's settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")

# Get the WSGI application
application = get_wsgi_application()