# Django project routes file

from django.contrib import admin
from django.urls import path, include  # The include function allows connecting application URL configurations

urlpatterns = [
    path('admin/', admin.site.urls),  # Route to the Django admin panel
    # Connect routes from our 'app' application
    path('', include('app.urls')),
]