# apps.app3/admin.py
from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'isbn', 'publication_year', 'classification')
    search_fields = ('title', 'author', 'isbn', 'subjects')
    list_filter = ('publication_year', 'language', 'classification')
