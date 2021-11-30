from django.contrib import admin
from .models import Book, Author

# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'book_name', 'publication_year', 'no_of_pages', 'book_language']

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id', 'author_name', 'author_age', 'author_country']


