"""
ASGI configuration for the myproject project.
"""

import os
from django.core.asgi import get_asgi_application

# Set the environment variable for Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

# Get the ASGI application
application = get_asgi_application()
