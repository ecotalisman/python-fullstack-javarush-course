"""
URL configuration for the myproject project.

Defines a set of URL routes for accessing the administrative interface.
"""

from django.contrib import admin
from django.urls import path

urlpatterns = [
    # Routing for the admin site
    path('admin/', admin.site.urls),
]
