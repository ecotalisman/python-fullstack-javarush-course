"""
ASGI config for myproject project.

This file contains the ASGI application used for deployment.
"""

import os
from django.core.asgi import get_asgi_application

# Set the project settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

# Get the ASGI application
application = get_asgi_application()