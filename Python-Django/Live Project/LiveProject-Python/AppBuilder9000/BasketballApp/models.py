from django.db import models
from django import forms


# Create your models here.

NBA_Conference = (('Western', 'Western'), ('Eastern', 'Eastern'))

class Schedule(models.Model):
    conference = models.CharField(max_length=20, blank=True, choices= NBA_Conference)
    teamz = models.CharField(max_length=30)


    Schedules = models.Manager()

    def __str__(self):
        return self.teamz

class CreateContact(models.Model):
    name = models.CharField(max_length=60)
    description = models.CharField(max_length=300)
    email = models.CharField(max_length=100)


    CreateContacts = models.Manager()

    def __str__(self):
        return self.name




