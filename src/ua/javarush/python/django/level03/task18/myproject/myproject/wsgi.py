import os
from django.core.wsgi import get_wsgi_application

# Set the environment variable with the project settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

# Get the WSGI application
application = get_wsgi_application()