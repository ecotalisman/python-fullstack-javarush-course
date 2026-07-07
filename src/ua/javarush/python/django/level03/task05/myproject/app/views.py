from django.http import HttpResponse  # Import HttpResponse to create a response


# View function that returns the text "Welcome to the home page!".
def home_view(request):
    return HttpResponse("Welcome to the home page!")