from django.contrib import admin
from django.urls import path, include

# Register the project's routes, including the application's routes
urlpatterns = [
    path('admin/', admin.site.urls),           # URL for the admin panel
    path('', include('app.urls')),             # Include the URL config of the "app" application
]