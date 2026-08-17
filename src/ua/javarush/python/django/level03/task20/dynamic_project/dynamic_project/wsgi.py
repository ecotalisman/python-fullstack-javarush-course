"""
WSGI configuration for the dynamic_project project.
Configures the WSGI application. Additional details are available in the documentation:
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dynamic_project.settings')
application = get_wsgi_application()
