from django.urls import path
from .views import json_response

# Define the URL route for the view that returns a JSON response
urlpatterns = [
    # A request to the URL "/json/" will call the json_response function,
    # which returns the required JSON response
    path('json/', json_response, name='json_response'),
]