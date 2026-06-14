import os
from django.core.wsgi import get_wsgi_application

# Set the settings for the project
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

# Get the WSGI application for deployment on a WSGI server
application = get_wsgi_application()
