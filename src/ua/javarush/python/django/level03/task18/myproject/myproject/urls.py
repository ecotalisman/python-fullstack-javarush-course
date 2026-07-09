from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Route to the admin panel
    path('admin/', admin.site.urls),
    # Connect routes from the app application
    path('', include('app.urls')),
]