"""
WSGI config for myproject project.

This file contains the WSGI application used for deployment.
"""

import os
from django.core.wsgi import get_wsgi_application

# Set the environment variable for the project settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

# Get the WSGI application
application = get_wsgi_application()