from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Configure the route for passing requests to the "store" application
    path('store/', include('store.urls'))
]