"""
Main URL routing file for the project.
Register routes here, including the route for the hello_html view function.
"""
from django.contrib import admin
from django.urls import path
from app.views import hello_html  # Import the view function

urlpatterns = [
    path('admin/', admin.site.urls),  # URL for the admin panel
    path('html/', hello_html, name='hello_html')
]