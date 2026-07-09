"""
WSGI configuration for the Django project.
"""
import os
from django.core.wsgi import get_wsgi_application

# Set the environment variable for the project settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

application = get_wsgi_application()