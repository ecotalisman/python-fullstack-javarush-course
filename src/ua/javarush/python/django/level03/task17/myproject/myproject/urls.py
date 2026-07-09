"""
Main URL configuration for the myproject project.

Routes from the admin interface and the "app" application are connected here.
"""
from django.contrib import admin
from django.urls import path, include  # include allows connecting URLs from other applications

urlpatterns = [
    # Route for the Django admin interface
    path('admin/', admin.site.urls),
    # Connect routes from the "app" application
    path('', include('app.urls')),
]