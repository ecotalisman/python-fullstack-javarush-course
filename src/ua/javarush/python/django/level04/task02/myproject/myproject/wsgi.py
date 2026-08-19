import os
from django.core.wsgi import get_wsgi_application

# Set the environment variable for the settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

# Get the WSGI application for the server
application = get_wsgi_application()