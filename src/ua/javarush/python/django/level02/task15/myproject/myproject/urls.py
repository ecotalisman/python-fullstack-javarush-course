from django.contrib import admin
from django.urls import path

# URL route for the admin panel
urlpatterns = [
    path('admin/', admin.site.urls),
]