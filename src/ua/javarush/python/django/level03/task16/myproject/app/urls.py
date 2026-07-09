from django.urls import path  # Import the path function for creating routes
from .views import handle_post  # Import the view function

# Define routes for the application
urlpatterns = [
    # URL route for calling the view that handles POST requests
    path('json/', handle_post, name='handle_post'),
]