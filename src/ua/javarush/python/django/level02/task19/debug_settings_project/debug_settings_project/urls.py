"""
URL routes for the debug_settings_project project.
"""

from django.contrib import admin
from django.urls import path
from . import views  # Import the created view

urlpatterns = [
    path('admin/', admin.site.urls),  # URL for the admin panel
    path('', views.view, name='view')
]
