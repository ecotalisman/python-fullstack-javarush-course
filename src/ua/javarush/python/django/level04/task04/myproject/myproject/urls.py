from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # URL for the Django admin panel
    path('admin/', admin.site.urls),
    # Connect the routes of the 'app' application
    path('', include('app.urls')),
]