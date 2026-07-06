from django.http import HttpResponse  # Import HttpResponse to create a response

# View function that returns an HTML page
def hello_html(request):
    html_content = "<h1>Welcome to Django!</h1><p>This is an HTML response.</p>"
    return HttpResponse(html_content)