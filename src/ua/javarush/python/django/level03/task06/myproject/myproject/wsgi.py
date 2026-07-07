"""
WSGI configuration for the myproject project.
"""

import os
from django.core.wsgi import get_wsgi_application

# Specify the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

# Get the WSGI application for the server
application = get_wsgi_application()