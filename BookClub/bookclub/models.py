from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

class Book(models.Model):
    book = models.CharField(max_length=100)
    description = models.TextField()
    read_by = models.DateField()

    def __str__(self):
        return self.book


class Discussion(models.Model):
    book = models.ForeignKey('Book', related_name='discussion', on_delete=models.CASCADE)
    author = models.ForeignKey('auth.User', related_name='records', on_delete=models.CASCADE)
    opinion = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True)

