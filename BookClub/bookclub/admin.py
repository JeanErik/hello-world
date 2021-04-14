from django.contrib import admin

# Register your models here.

from .models import Book, Discussion

admin.site.register(Book)
admin.site.register(Discussion)
