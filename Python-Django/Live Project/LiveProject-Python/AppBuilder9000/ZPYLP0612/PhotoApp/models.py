from django.db import models

# Create your models here.
Photography_Genres = (('Fashion', 'Portrait'), ('Street', 'Landscape'), ('Wildlife', 'Astrophotography'),
                 ('travel', 'Wedding'), ('Documentary', 'Marco'), ('Still Life', 'Food'),
                ('Sports', 'Fine-Art,'), ('Underwater', 'Event'), ('Aerial', 'Abstract'), ('Architectural', 'Candid'),
                 ('Long Exposure','Night'), ('Lifestyle','Black and White'), ('Stock', 'Infrared'))


class Photography(models.Model):
    DarkRoom = models.CharField(max_length=30)
    PhotoBooth = models.CharField(max_length=30)
    PolaroidInstant = models.CharField(max_length=30, choices= Photography_Genres)
    Digital = models.CharField(max_length=30)
    PhotographicFilm = models.CharField(max_length=15,)

    Photography = models.Manager()

    def __str__(self):
        return self.photo

