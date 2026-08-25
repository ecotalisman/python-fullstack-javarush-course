from django.http import HttpResponse
from django.views import View


# Creating a Class-Based View that inherits from the base View class
class HelloWorldView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello from CBV!')