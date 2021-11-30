from django.db import models


# Create your models here.

class Author(models.Model):
    author_name =  models.CharField(max_length=250, blank=True)
    author_age = models.IntegerField(blank=True)
    author_country = models.CharField(max_length=100, blank=True)
    
    def __str__(self):
        return self.author_name
    
class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, blank=True, null=True)
    book_name = models.CharField(max_length=250, blank=True)
    publication_year = models.IntegerField(blank=True)
    no_of_pages = models.IntegerField(blank=True)
    book_language = models.CharField(max_length=250, default="",blank=True)

    # def __str__(self):
    #     return self.author

#Either comment the whole function as above or use it as below by adding or ''
    def __str__(self):
        return self.author or ''