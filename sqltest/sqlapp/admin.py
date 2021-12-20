from django.contrib import admin
from django.db.models.fields import Field
from .models import Actor, FilmDirector, Movies, User, Rating

@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ['id','name','age','birth_country']

@admin.register(FilmDirector)
class FilmDirectorAdmin(admin.ModelAdmin):
    list_display = ['id','name','age','birth_country']
    
@admin.register(Movies)
class MoviesAdmin(admin.ModelAdmin):
    list_display = ['id','director','title', 'year']
    
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id','name','email']
    
@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ['id','user_name','title', 'ratings', 'rating_date', 'is_rating_recent']
# admin.site.register(Actor)
# admin.site.register(FilmDirector)
# admin.site.register(Movies)
# admin.site.register(User)
# admin.site.register(Rating)