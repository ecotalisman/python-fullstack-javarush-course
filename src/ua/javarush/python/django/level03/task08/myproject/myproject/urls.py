from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Route to the Django admin panel
    # Add routes for our myapp application
    path('', include('myapp.urls')),
]