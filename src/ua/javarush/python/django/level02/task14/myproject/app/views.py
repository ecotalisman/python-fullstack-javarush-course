from django.shortcuts import render
from .models import UserDocument


# View for displaying the list of uploaded documents
def document_list(request):
    # Get all objects of the UserDocument model
    documents = UserDocument.objects.all()
    # Pass the list of documents to the template for further display
    return render(request, 'app/documents.html', {'documents': documents})
