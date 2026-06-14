from django.http import HttpResponse  # Import the HttpResponse class for sending an HTTP response
from django.shortcuts import render


# Function-based view for the home page
def homepage(request):
    return HttpResponse("Ласкаво просимо на наш сайт!")