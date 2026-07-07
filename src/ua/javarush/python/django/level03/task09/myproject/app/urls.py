# Import the necessary functions for creating routes
from django.urls import path
from .views import welcome_view  # Import our view

# Define the list of routes for the application
urlpatterns = [
    # Create a route for the URL '/welcome/' and connect it to the welcome_view function
    path('welcome/', welcome_view, name='welcome')
]