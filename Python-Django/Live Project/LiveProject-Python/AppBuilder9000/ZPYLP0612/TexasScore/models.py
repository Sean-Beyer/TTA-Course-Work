from django.db import models

# Create your models here.
Team_Against = (('South Florida', 'South Florida'), ('Louisiana State University', 'Louisiana State University'),
                ('Kansas State', 'Kansas State'), ('Oklahoma State', 'Oklahoma State'), ('Oklahoma', 'Oklahoma'),
                ('West Virginia', 'West Virginia'), ('Texas Tech', 'Texas Tech'), ('Baylor', 'Baylor'),
                ('Kansas', 'Kansas'), ('Iowa State', 'Iowa State'),
                ('Texas Christian University', 'Texas Christian University'), ('Other', 'Other'))

Home_Away = (('Home', 'Home'), ('Away', 'Away'), ('Other', 'Other'))
Game_Time = (('Morning', 'Morning'), ('Afternoon', 'Afternoon'), ('Evening', 'Evening'), ('Other', 'Other'))
Game_Importance = (('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'),
                   ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'))
Win_Loss = (('Texas', 'Texas'), ('Opponent', 'Opponent'))


class TexasGame(models.Model):
    win_loss = models.CharField(max_length=20, choices=Win_Loss)
    stadium = models.CharField(max_length=20, choices=Home_Away)
    against = models.CharField(max_length=75, choices=Team_Against)
    time_of_day = models.CharField(max_length=20, choices=Game_Time)
    score = models.PositiveIntegerField(blank=True, null=True)
    significance = models.CharField(max_length=20, choices=Game_Importance)

    TexasGames = models.Manager()
