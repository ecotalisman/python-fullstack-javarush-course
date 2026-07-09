from django.http import JsonResponse  # Import the JsonResponse class to create a JSON response


# View function that returns a static JSON response
def json_response(request):
    data = {"status": "success", "message": "Hello, JSON!"}
    return JsonResponse(data)