from django.urls import path
from .views import app_page  # Імпортуємо наш view

urlpatterns = [
    # Define the route for the application page.
    # The path 'page/' together with the 'app/' prefix from the main urls.py will give the full address /app/page/
    path('page/', app_page, name='app_page'),
]