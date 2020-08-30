from django.db import models
from django.forms import ModelForm

Genre = (('Rap', 'Rap'), ('Pop', 'Pop'), ('Rock', 'Rock'), ('Jazz', 'Jazz'), ('Other', 'Other'))
NewsOutlets = (('Billboard', 'Billboard'), ('Fuse', 'Fuse'), ('SPIN', 'SPIN'), ('Digital Music News', 'Digital Music News'))


class MNews(models.Model):
    genre = models.CharField(max_length=20, choices=Genre)
    NewsOutlets = models.CharField(max_length=50, choices=NewsOutlets)

    MNews = models.Manager()


def __str__(self):
    return self.name