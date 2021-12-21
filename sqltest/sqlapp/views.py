from django.shortcuts import render
from django.db import connection
from .models import Actor, FilmDirector, Movies, User, Rating
from django.db.models import Q
from django.db import connection 
# Create your views here.

def dictfetchall(cursor):
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]

def jointables(request):
    cursor=connection.cursor()
    cursor.execute("SELECT * FROM sqlapp_movies JOIN sqlapp_rating ON sqlapp_rating.title_id = sqlapp_movies.id" )
    r = dictfetchall(cursor)
    print(r)
    return render (request, 'output.html',{'result': r})

def jointhreetables(request):
    cursor=connection.cursor()
    cursor.execute("SELECT title, director_name, ratings FROM sqlapp_movies JOIN sqlapp_filmdirector ON sqlapp_filmdirector.id = sqlapp_movies.director_id Join sqlapp_rating ON sqlapp_rating.title_id = sqlapp_movies.id" )
    r = dictfetchall(cursor)
    print(r)
    return render (request, 'output.html',{'results': r})
