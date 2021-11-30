from django.shortcuts import render
from django.db.models import fields
from django.views.generic import TemplateView, ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import Book


# Create your views here.
class HomePageView(TemplateView):
    template_name = "home.html"

class BookListView(ListView):
     model = Book
     template_name = "booklist.html"
     
class BookCreateView(CreateView):
    model = Book
    fields = ['author','book_name', 'publication_year', 'no_of_pages', 'book_language']
    template_name = 'newbook.html'
    success_url = '/thankyou/'

class ThanksView(TemplateView):
    template_name = "thankyou.html"
    
class SingleBookView(DetailView):
    model = Book
    template_name = 'detailsupdate.html'

class BookUpdateView(UpdateView):
    model = Book
    fields = ['book_name', 'publication_year', 'no_of_pages', 'book_language']
    template_name = 'detailsupdate.html'
    success_url = '/thankyou/'

class BookDeleteView(DeleteView):
    model = Book
    template_name = "bookdelete.html"
    success_url = '/thankyou/'