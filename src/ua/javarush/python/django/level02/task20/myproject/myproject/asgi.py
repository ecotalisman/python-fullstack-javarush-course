"""
ASGI configuration for the debug_settings_project project.
It allows ASGI servers to interact with your Django project.
"""

import os
from django.core.asgi import get_asgi_application

# Set the environment variable to use the Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'debug_settings_project.settings')

# Get the ASGI application object for handling requests
application = get_asgi_application()
