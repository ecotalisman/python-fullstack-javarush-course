from django.db import models


# The Author model represents an author with their name and date of birth
class Author(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField()

    def __str__(self):
        return self.name
