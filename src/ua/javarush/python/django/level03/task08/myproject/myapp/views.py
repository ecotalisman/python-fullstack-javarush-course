import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


# The calculate view that handles GET and POST requests
@csrf_exempt
def calculate(request):
    if request.method == 'GET':
        return HttpResponse("Please send two numbers for calculation.")
    elif request.method == 'POST':
        numbers = json.loads(request.body)
        a = numbers.get("a")
        b = numbers.get("b")
        sum_ab = a + b
        return HttpResponse(f"Result: {sum_ab}")
    else:
        return HttpResponse(f"Method {request.method} not allowed.", status=405)