import os
from django.core.asgi import get_asgi_application

# Set the settings module for ASGI
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

# Get the ASGI application
application = get_asgi_application()