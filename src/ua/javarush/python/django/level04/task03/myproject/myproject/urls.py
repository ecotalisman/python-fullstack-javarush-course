"""
URL configuration file of the project.

This is where URLs are bound to their corresponding handlers (views).
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # URL for the admin panel
    # Connect the URLs from the 'app' application
    # All requests starting with 'cbv/' will be handled by the 'app' application
    path('cbv/', include('app.urls')),
]