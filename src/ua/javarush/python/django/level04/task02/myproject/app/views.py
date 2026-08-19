from django.http import HttpResponse
from django.views import View

# Class-based view for handling GET and POST requests, inherits from the base View class
class MyView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('This is a GET request')

    def post(self, request, *args, **kwargs):
        return HttpResponse('This is a POST request')