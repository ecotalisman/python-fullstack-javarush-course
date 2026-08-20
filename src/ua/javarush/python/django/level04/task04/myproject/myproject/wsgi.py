import os
from django.core.wsgi import get_wsgi_application

# Set the settings module for WSGI
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

# Get the WSGI application
application = get_wsgi_application()