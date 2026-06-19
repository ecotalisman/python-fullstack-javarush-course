import os
from django.core.asgi import get_asgi_application

# Set the environment variable to specify the project settings file
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

# Get the ASGI application for handling asynchronous requests
application = get_asgi_application()
