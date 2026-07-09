from django.contrib import admin
from django.urls import path, include

# Main route of the project
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),  # Connect the application routes
]