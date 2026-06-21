"""
ASGI configuration for the myproject project.
Allows the project to be run using an ASGI server.
"""

import os
from django.core.asgi import get_asgi_application

# Set the environment variable for Django settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")

# Get the ASGI application that the server uses to run the project
application = get_asgi_application()
