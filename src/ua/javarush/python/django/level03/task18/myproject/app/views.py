from django.http import JsonResponse
from .models import User


# View for displaying a list of users filtered by minimum age and name
def user_list(request, min_age):
    # Extract the 'name' parameter from the GET request if it is passed
    search_name = request.GET.get('name')

    # Filter users, keeping only those whose age is >= min_age
    users = User.objects.filter(age__gte=min_age)

    # If the 'name' parameter is passed, add additional filtering by name
    if search_name:
        users = users.filter(name=search_name)

    # Convert the query results into a list of dictionaries
    find_users = list(users.values("id", "name", "age"))

    # Return the data in JSON format
    return JsonResponse(find_users, safe=False)