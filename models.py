from django.db import models
from datetime import datetime

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=200)
    director = models.CharField(max_length=200)
    year = models.PositiveSmallIntegerField(default = 0000)
    rt_rating = models.IntegerField(default=0)
    watched = models.BooleanField(default = False)
    tmdb_id = models.IntegerField(default = 0)
    date_added = models.DateTimeField(default = datetime.today)
    date_watched = models.DateTimeField(default = datetime.today)
    poster_url = models.CharField(max_length=200)
    def __str__(self):
        return self.title

#class TVShow(models.Model):