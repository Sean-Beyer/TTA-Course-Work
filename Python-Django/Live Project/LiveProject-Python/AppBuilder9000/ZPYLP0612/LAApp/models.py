from django.db import models

# Create your models here.
AUTHOR_GENRES = (('SciFi & Fantasy', 'SciFi & Fantasy'), ('Literature', 'Literature'), ('Poetry', 'Poetry'),
                 ('Non-Fiction', 'Non-Fiction'), ('Travel', 'Travel'), ('Crime/Detective', 'Crime/Detective'),
                ('Romance', 'Romance,'), ('Western', 'Western'), ('Horror', 'Horror'), ('Biography', 'Biography'),
                 ('Children\'s Lit','Children\'s Lit'), ('Young Adult Fiction','Young Adult Fiction'), ('Other', 'Other'))

AUTHOR_STATES = (('Oregon', 'OR'), ('Washington', 'WA'), ('California','CA'), ('Alaska','AK'), ('Hawaii','HI'))


class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    genre = models.CharField(max_length=30, choices= AUTHOR_GENRES)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=15, choices= AUTHOR_STATES)
    title = models.CharField(max_length=40)
    publisher = models.CharField(max_length=30, blank=True, null=True)
    published_year = models.PositiveIntegerField(blank=True, null=True)

    Authors = models.Manager()

    def __str__(self):
        return self.last_name

    # def full_name(self):