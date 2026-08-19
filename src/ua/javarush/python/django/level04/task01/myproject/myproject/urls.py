"""URL configuration for the myproject project."""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),           # URL for the admin interface
    path('', include('app.urls')),             # Add the URLs of our application
]