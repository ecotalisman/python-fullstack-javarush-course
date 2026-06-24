"""
ASGI configuration for the myproject project.

Exporting the application variable for the ASGI server.
"""
import os
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

application = get_asgi_application()