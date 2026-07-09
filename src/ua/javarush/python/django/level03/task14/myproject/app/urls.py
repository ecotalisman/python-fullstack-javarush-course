from django.urls import path
from .views import user_profile

# Define routes for the application
urlpatterns = [
    # Dynamic route for handling a URL with the username parameter
    path('user/<str:username>/', user_profile, name='user_profile'),
]