from django.http import HttpResponse


# View function for handling the blog archive
def blog_archive(request, year, month, day):
    return HttpResponse(f"Архів блогу за {year}-{month}-{day}")