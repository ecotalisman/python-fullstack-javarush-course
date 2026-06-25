"""
WSGI configuration for the debug_settings_project project.
It allows WSGI servers to interact with your Django project.
"""

import os
from django.core.wsgi import get_wsgi_application

# Set the environment variable to use the Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'debug_settings_project.settings')

# Get the WSGI application object for handling requests
application = get_wsgi_application()
