from sqlite3.dbapi2 import Date

from django.db import models
from django.forms import DateField


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_date = models.DateField()
