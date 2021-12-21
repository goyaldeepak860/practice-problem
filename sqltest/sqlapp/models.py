from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import datetime, date, time, timedelta
from django.utils import timezone

# Create your models here.
class Actor(models.Model):
    actor_name = models.CharField(max_length=250)
    actor_age =  models.IntegerField()
    actor_birth_country = models.CharField(max_length=250)
    
        
    def __str__(self):
        return self.actor_name

class FilmDirector(models.Model):
    director_name = models.CharField(max_length=250)
    director_age =  models.IntegerField()
    director_birth_country = models.CharField(max_length=250)
       
    def __str__(self):
        return self.director_name
    
class Movies(models.Model):
    director = models.ForeignKey(FilmDirector, on_delete=models.CASCADE, blank=False, null=True)
    title = models.CharField(max_length=250, blank=False, null=False, default="")
    year =  models.IntegerField()
    actor = models.ManyToManyField(Actor)
    
    def movies_actors(self):
        return ",".join([str(p) for p in self.actor.all()])
    
    def __str__(self):
        return self.title or ''
    
    
class User(models.Model):
    user_name = models.CharField(max_length=250)
    user_email=  models.EmailField()
        
    def __str__(self):
        return self.user_name

class Rating(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=True)
    title =  models.ForeignKey(Movies, on_delete=models.CASCADE, blank=False, null=True)
    ratings=  models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)])
    rating_date= models.DateTimeField('date published')
  
    def is_rating_recent(self):
        now = timezone.now()
        return now - timedelta(days=7) <= self.rating_date
    is_rating_recent.boolean = True
    
    def movie_average(self):
     if self.ratings < 3 :
         return 'Below Average'
     elif self.ratings == 3 : 
         return 'Average' 
     else:
         return 'Above Average'   
     
class NewRating(Rating):
    feedback = models.CharField(max_length=100, default="", blank=True, null=True)
            
    
    
        
    
