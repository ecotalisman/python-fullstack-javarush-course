"""
Main URL configuration file for the dynamic_project project.
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin panel
    path('', include('greetings.urls')),  # Connect the routes of the greetings application

]