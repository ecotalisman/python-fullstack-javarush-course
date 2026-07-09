from django.contrib import admin  # Django admin application
from django.urls import path, include  # Functions for routing

# Define the root routes of the project
urlpatterns = [
    path('admin/', admin.site.urls),  # Route for the admin panel
    path('', include('app.urls')),      # Connect routes from the "app" application
]