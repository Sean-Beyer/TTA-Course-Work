from django.db import models


class Classes(models.Model):
    Title = models.CharField(max_length=60)
    Course_Number = models.IntegerField(default=000, blank=True, null=False)
    Instructor_Name = models.CharField(max_length=100, default="", blank=True)
    Duration = models.FloatField(null=True, blank=True)

    objects = models.Manager()