from django.db import models

# Model for storing information about users
class User(models.Model):
    name = models.CharField(max_length=100)  # User name
    age = models.PositiveIntegerField()      # User age

    def __str__(self):
        # Convenient string representation of the model object
        return f"{self.name} ({self.age})"