from django.urls import path
from . import views  # Import views from the current application

# Define routes for the application
urlpatterns = [
    # Route with the dynamic id parameter.
    # Use path() to integrate the dynamic URL segment.
    path('get-id/<int:id>/', views.show_id, name='show_id'),
]