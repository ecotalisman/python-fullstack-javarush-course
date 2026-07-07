from django.contrib import admin
from django.urls import path, include  # include allows connecting URL configurations from applications

urlpatterns = [
    path('admin/', admin.site.urls),  # URL for the Django admin panel
    # Connect the URL routing of the myapp application
    path('', include('myapp.urls'))
]