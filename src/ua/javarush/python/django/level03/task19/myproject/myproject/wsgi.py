"""
WSGI configuration for the myproject project.
This entry point for WSGI servers uses the project settings.
"""
import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

application = get_wsgi_application()