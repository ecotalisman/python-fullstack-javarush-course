from django.http import HttpResponse


# View function for handling the request and displaying the selected article
def article_detail(request, article_id):
    return HttpResponse(f"Ви обрали статтю з ID: {article_id}")