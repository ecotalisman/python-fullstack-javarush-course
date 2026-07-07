"""
WSGI configuration for the myproject project.
Allows interaction with WSGI servers, such as Gunicorn.
"""
import os
from django.core.wsgi import get_wsgi_application

# Set the project settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

application = get_wsgi_application()