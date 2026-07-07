from django.urls import path  # Import the path function to define routes
from .views import welcome_view  # Import the welcome_view view function from the current package

urlpatterns = [
    # Define the '/welcome/' route to call the welcome_view view function
    path('welcome/', welcome_view, name='welcome')
]