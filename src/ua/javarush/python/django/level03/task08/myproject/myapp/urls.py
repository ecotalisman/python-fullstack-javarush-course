from django.urls import path
from .views import calculate

# Define routes for the myapp application
urlpatterns = [
    # The /calculate/ route is linked to the calculate function
    path('calculate/', calculate, name='calculate')
]