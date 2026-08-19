from django.urls import path
from .views import MyView

# Register the application's routes
urlpatterns = [
    # Route for our view; requests to http://<host>/cbv/ will be handled by MyView
    path('', MyView.as_view(), name='my_view'),
]