from django.shortcuts import render
from django.db import connection
from .models import Actor, FilmDirector, Movies, User, Rating
from django.db.models import Q
from django.db import connection 
# Create your views here.

# def tablesjoin(request):
#     cursor=connection.cursor()
#     cursor.execute("select Actor.name, Movies.title, Movies.director from Movies join Movies on Actor.name=Movies.actor")
#     results = cursor.fetchall()
#     return render (request, 'output.html', {'Actor':results})