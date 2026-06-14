from django.contrib import admin
from django.urls import path, include

# Main routing file of the project
urlpatterns = [
    path('admin/', admin.site.urls),  # URL for the Django admin panel
    path('myapp/', include('myapp.urls')),

]
