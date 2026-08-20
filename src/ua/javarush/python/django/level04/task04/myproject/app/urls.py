from django.urls import path
from .views import MyView  # Import the view we created

urlpatterns = [
    # Setting up the route for our view.
    # The as_view() method turns our class into a view function that Django understands.
    path('', MyView.as_view(), name='my_view'),
]