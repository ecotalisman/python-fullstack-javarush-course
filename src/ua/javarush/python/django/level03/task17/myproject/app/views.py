from django.http import HttpResponse


# View for extracting the id parameter from the URL and creating a response
def show_id(request, id):
    return HttpResponse(f"Ваш ID: {id}")