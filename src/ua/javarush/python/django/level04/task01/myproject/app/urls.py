from django.urls import path
from .views import WelcomeView

urlpatterns = [
    # Register the URL for our class-based view.
    # The as_view() method turns the class into a callable function.
    path('', WelcomeView.as_view(), name='welcome_view'),
]