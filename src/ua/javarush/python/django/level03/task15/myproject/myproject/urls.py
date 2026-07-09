from django.contrib import admin
from django.urls import path, include

# Define URL routes for the project
urlpatterns = [
    path('admin/', admin.site.urls),  # URL for the admin panel
    path('', include('app.urls')),      # Connect the URL routing of our app application
]