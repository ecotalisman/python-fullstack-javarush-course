from django.contrib import admin
from django.urls import path
# Import the article_detail view function from our application
from app.views import article_detail

urlpatterns = [
    path('admin/', admin.site.urls),  # Route for the admin panel
    # Dynamic URL where article_id is accepted as an integer
    path('article/<int:article_id>/', article_detail, name='article_detail'),
]