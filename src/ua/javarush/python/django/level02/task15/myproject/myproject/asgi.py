"""
ASGI configuration for the Django project "myproject".
Versions: Django 5.1, Python 3.12
"""

import os
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

application = get_asgi_application()
