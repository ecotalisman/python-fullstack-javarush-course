from django.http import HttpResponse


# View for handling a dynamic URL with the username parameter
def user_profile(request, username):
    return HttpResponse(f"Ласкаво просимо, {username}!")