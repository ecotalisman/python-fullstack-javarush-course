"""
ASGI configuration for the 'website' project.

This file is used to run the project on an ASGI-compatible web server.
"""

import os
from django.core.asgi import get_asgi_application

# Set the environment variable for the project settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'website.settings')

application = get_asgi_application()
