import os
from django.core.asgi import get_asgi_application

# Set the settings for the project
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

# Get the ASGI application for deployment on an ASGI server
application = get_asgi_application()
