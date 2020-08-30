from django.db import models


# Created models

class Comedies(models.Model):
    comedy = models.CharField(max_length=100, blank=True)
    actor = models.CharField(max_length=100, blank=True)
    director = models.CharField(max_length=100, blank=True)
    year = models.CharField(max_length=100, blank=True)
    imdb_rating = models.CharField(max_length=100, null=True)
    rating = models.DecimalField(max_digits=2, decimal_places=1, null=True)
    review = models.CharField(max_length=1000, blank=True, null=True)

    Comedy= models.Manager() # object manager for Movie Database

    def __str__(self):
        return self.comedy


