from django.contrib import admin
from .models import UserDocument


# Register the UserDocument model in the admin interface
@admin.register(UserDocument)
class UserDocumentAdmin(admin.ModelAdmin):
    list_display = ('id', 'file')