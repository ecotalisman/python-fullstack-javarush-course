"""
ASGI configuration for the Django project.
"""

import os
from django.core.asgi import get_asgi_application

# Set the settings module for the project
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

# Get the ASGI application
application = get_asgi_application()