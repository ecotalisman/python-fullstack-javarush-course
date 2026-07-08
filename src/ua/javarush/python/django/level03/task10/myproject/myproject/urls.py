"""
Root URL configuration of the project.
Routes URL requests to the corresponding applications.
"""

from django.contrib import admin
from django.urls import path, include  # include allows connecting application URL configurations

urlpatterns = [
    path('admin/', admin.site.urls),  # URL for the admin panel
    path('', include('blog.urls')),   # Connect the URL configuration of the blog application
]