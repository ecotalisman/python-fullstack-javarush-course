# Import HttpResponse to create an HTTP response
from django.http import HttpResponse


# View function that returns the text "Welcome!"
def welcome_view(request):
    return HttpResponse("Ласкаво просимо!")