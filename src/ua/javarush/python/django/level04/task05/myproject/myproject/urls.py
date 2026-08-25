"""
URL configuration for the myproject project.
This is where the URL rules for the admin site and the application are connected.
"""
from django.contrib import admin
from django.urls import path
# Import our HelloWorldView view from the app application
from app.views import HelloWorldView

urlpatterns = [
    path("admin/", admin.site.urls),
    # Setting up the /hello/ route to display HelloWorldView
    path('hello/', HelloWorldView.as_view(), name='hello')
]