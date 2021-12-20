from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import datetime, date, time, timedelta
from django.utils import timezone

# Create your models here.
class Actor(models.Model):
    name = models.CharField(max_length=250)
    age =  models.IntegerField()
    birth_country = models.CharField(max_length=250)
        
    def __str__(self):
        return self.name

class FilmDirector(models.Model):
    name = models.CharField(max_length=250)
    age =  models.IntegerField()
    birth_country = models.CharField(max_length=250)
       
    def __str__(self):
        return self.name
    
class Movies(models.Model):
    director = models.ForeignKey(FilmDirector, on_delete=models.CASCADE, blank=False, null=True)
    title = models.CharField(max_length=250, blank=False, null=False, default="")
    year =  models.IntegerField()
    actor = models.ManyToManyField(Actor)
       
    def __str__(self):
        return self.title or ''
    
    
class User(models.Model):
    name = models.CharField(max_length=250)
    email=  models.EmailField()
        
    def __str__(self):
        return self.name

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
         average='Below Average'
         return average
     elif self.ratings == 3 : 
         average='Average'
         return average 
     else:
         average= 'Above Average'
         return average   
       
            
    
    
        
    
