from django.contrib import admin
from django.urls import path, include  # The include function allows connecting routes from applications

urlpatterns = [
    path('admin/', admin.site.urls),  # Django admin panel address
    # Connect the myapp application routes to the root URL
    path('', include('myapp.urls')),
]