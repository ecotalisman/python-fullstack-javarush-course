from django.urls import path
from .views import user_list

urlpatterns = [
    # The required min_age parameter is passed through the URL.
    # An additional name parameter may be passed in the GET request for filtering by name.
    # Example: /users/18/?name=John
    path('users/<int:min_age>/', user_list, name='user_list'),

]