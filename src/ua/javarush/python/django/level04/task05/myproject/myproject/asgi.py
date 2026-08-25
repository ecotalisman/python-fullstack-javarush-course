"""
ASGI configuration for the Django project.
Used to support asynchronous servers.
"""
import os
from django.core.asgi import get_asgi_application

# Set the project's settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")

# Get the ASGI application
application = get_asgi_application()