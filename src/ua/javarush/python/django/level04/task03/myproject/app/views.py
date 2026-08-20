from django.http import HttpResponse  # Import HttpResponse to build the response
from django.views import View         # Import the base View class to create a CBV


# Create a Class-Based View (CBV) by inheriting from django.views.View
class HelloView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello from CBV!')