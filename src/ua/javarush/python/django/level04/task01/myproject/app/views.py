from django.http import HttpResponse
from django.views import View


# Class-based view for handling a GET request
class WelcomeView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Welcome to Class-Based Views!')