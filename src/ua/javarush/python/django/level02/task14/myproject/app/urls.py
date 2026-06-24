from django.urls import path
from .views import document_list

urlpatterns = [
    # The main page of the application displays a list of uploaded documents
    path('', document_list, name='document_list'),
]