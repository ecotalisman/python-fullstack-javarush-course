# Import the admin module and functions for connecting routes
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin panel address
    # Connect the URL configuration of the "news" application with the "news/" prefix
    path('news/', include('news.urls'))
]
