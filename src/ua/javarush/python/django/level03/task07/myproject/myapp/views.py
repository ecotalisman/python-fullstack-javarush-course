from django.http import HttpResponse  # Import HttpResponse to create an HTTP response


# The welcome_view view function that returns the text response "Welcome to Django!"
def welcome_view(request):
    return HttpResponse("Welcome to Django!")