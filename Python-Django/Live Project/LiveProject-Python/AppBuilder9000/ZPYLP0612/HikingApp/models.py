from django.db import models
from datetime import datetime
from django.utils import timezone

# Create your models here.
HIKE_DIFFICULTIES = (('easy', 'easy'), ('moderate', 'moderate'), ('hard', 'hard'))
HIKE_RATINGS = ((1, 1), (1.5, 1.5), (2, 2), (2.5, 2.5), (3, 3), (3.5, 3.5), (4, 4), (4.5, 4.5), (5, 5))
Hike_Completion = (('True', 'True'), ('False', 'False'))


class Hikes(models.Model):
    Hike_Name = models.CharField(max_length=100)
    Date = models.DateField(default=None)
    Start_Time = models.TimeField(default="12:00", blank=True, null=True )
    Difficulty = models.CharField(max_length=10, choices=HIKE_DIFFICULTIES, default='easy')
    Completed = models.CharField(max_length=5, choices=Hike_Completion, default='True')
    End_Time = models.TimeField(default="18:00", blank=True, null=True )
    Rating = models.DecimalField(max_digits=2, decimal_places=1, choices=HIKE_RATINGS, default=5)

    Hikes = models.Manager()

