from django.contrib import admin
from django.urls import path, include  # Import the include function to connect application routes

urlpatterns = [
    path('admin/', admin.site.urls),
    # Connect the routes of the "app_name" application. All URLs that start with "app/" will be
    # passed for processing to this application's urls.py.
    path('app/', include('app_name.urls')),
]