from django.http import HttpResponse


# View that returns the text "Це сторінка додатку!"
def app_page(request):
    return HttpResponse("Це сторінка додатку!")