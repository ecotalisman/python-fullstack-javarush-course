from django.contrib import admin
from django.urls import path

urlpatterns = [
    # Route for the Django admin panel
    path('admin/', admin.site.urls),
]