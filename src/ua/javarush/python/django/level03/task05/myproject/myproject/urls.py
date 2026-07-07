"""
Main URL routing file for the project.
Routes are registered here, including the route for the home_view view function.
"""
from django.contrib import admin
from django.urls import path, include
from app.views import home_view  # Import the view function

urlpatterns = [
    path('admin/', admin.site.urls),  # URL for the admin panel
    path('', include('app.urls')),
]