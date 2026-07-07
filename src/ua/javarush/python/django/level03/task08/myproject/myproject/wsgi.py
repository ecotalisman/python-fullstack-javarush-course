"""
WSGI configuration for the Django project.
"""

import os
from django.core.wsgi import get_wsgi_application

# Specify Django settings for WSGI
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

# Get the WSGI application
application = get_wsgi_application()