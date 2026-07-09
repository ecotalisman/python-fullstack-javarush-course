from django.contrib import admin
from .models import User

# Register the User model in the admin panel for convenient management
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'age')