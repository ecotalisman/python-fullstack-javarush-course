from django.contrib import admin
from django.urls import path

# Define the project URL routes
urlpatterns = [
    path('admin/', admin.site.urls),  # Route to the Django admin panel
]
