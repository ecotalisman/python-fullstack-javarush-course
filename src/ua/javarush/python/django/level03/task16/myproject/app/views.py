from django.http import JsonResponse  # Import JsonResponse for creating JSON responses


# View function for handling an HTTP request
def handle_post(request):
    if request.method == "POST":
        data = {"status": "Дані успішно отримані"}
        return JsonResponse(data)
    else:
        data = {"error": "Невірний метод запиту"}
        return JsonResponse(data, status=400)