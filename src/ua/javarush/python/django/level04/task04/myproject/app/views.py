from django.http import HttpResponse
from django.views import View  # Import of the base class for CBVs


# Class-based view that implements the handling of GET and POST requests
class MyView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('This is a GET request')

    def post(self, request, *args, **kwargs):
        return HttpResponse('This is a POST request')