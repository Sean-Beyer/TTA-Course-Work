from django.db import models

# Create your models here.
class Game(models.Model):
    game_name = models.CharField(max_length=100, default="", blank=True, null=False)
    game_designer = models.CharField(max_length=100, default="", blank=True, null=False)
    game_publisher = models.CharField(max_length=100, default="", blank=True, null=False)
    game_min_player = models.IntegerField(default=1, blank=True, null=False)
    game_max_player = models.IntegerField(default=1, blank=True, null=False)
    game_image_path = models.CharField(max_length=1000, default="", blank=True, null=False)
    game_playtime = models.CharField(max_length=100, default="", blank=True, null=False)
    game_expansion = models.BooleanField()

    objects = models.Manager()

    def __str__(self):
        return self.game_name