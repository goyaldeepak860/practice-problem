from django.shortcuts import render
from django.db import connection
from sqlapp.models import Actor, FilmDirector, Movies, User, Rating
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
    cursor.execute("SELECT title, director_name, ratings FROM sqlapp_movies JOIN sqlapp_filmdirector ON sqlapp_filmdirector.id = sqlapp_movies.director_id JOIN sqlapp_rating ON sqlapp_rating.title_id = sqlapp_movies.id" )
    r = dictfetchall(cursor)
    print(r)
    return render (request, 'output.html',{'results': r})


def jointhreetables_manytomany(request):
    cursor=connection.cursor()
    cursor.execute("SELECT * FROM sqlapp_movies_actor JOIN sqlapp_actor ON sqlapp_movies_actor.actor_id = sqlapp_actor.id JOIN sqlapp_movies ON sqlapp_movies.id = sqlapp_movies_actor.movies_id JOIN sqlapp_filmdirector ON sqlapp_filmdirector.id = sqlapp_movies.director_id JOIN sqlapp_rating ON sqlapp_rating.title_id = sqlapp_movies.id JOIN sqlapp_user ON sqlapp_user.id = sqlapp_rating.user_name_id" )
    r = dictfetchall(cursor)
    print(r)
    return render (request, 'output.html',{'resultnew': r})

def jointhreetables_manytomanynew(request):
    cursor=connection.cursor()
    cursor.execute("SELECT * FROM sqlapp_movies_actor JOIN  sqlapp_movies ON sqlapp_movies.id = sqlapp_movies_actor.movies_id JOIN sqlapp_filmdirector ON sqlapp_filmdirector.id = sqlapp_movies.director_id JOIN sqlapp_rating ON sqlapp_rating.title_id = sqlapp_movies.id JOIN sqlapp_user ON sqlapp_user.id = sqlapp_rating.user_name_id JOIN sqlapp_actor ON sqlapp_movies_actor.actor_id = sqlapp_actor.id" )
    r = dictfetchall(cursor)
    print(r)
    return render (request, 'output.html',{'resultnew': r})

def aggre_hav(request):
    cursor=connection.cursor()
    cursor.execute("SELECT ratings, COUNT(*) FROM sqlapp_Rating WHERE ratings < 5 GROUP BY ratings HAVING COUNT(*) > 2 ")
    r = dictfetchall(cursor)
    print(r)
    return render (request, 'output.html',{'resultnew': r})