from django.urls import path
from .views import HelloView  # Import our view

urlpatterns = [
    # Set up the route for our view.
    # An empty string '' means that HelloView will be called when a URL like /cbv/ is requested.
    path('', HelloView.as_view(), name='hello_view'),
]