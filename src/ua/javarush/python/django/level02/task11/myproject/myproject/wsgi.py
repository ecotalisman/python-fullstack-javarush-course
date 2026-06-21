"""
WSGI configuration for the myproject project.

Provides a WSGI application for use by the server.
"""

import os
from django.core.wsgi import get_wsgi_application

# Set the environment variable for Django settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")

# Get the WSGI application
application = get_wsgi_application()
