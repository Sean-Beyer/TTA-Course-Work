from django.db import models

RACES = (('Android', 'Android'), ('Human', 'Human'), ('Kasatha', 'Kasatha'), ('Lashunta', 'Lashunta'), ('Shirren', 'Shirren'), ('Vesk', 'Vesk'))

CLASSES = (('Envoy', 'Envoy'), ('Mechanic', 'Mechanic'), ('Mystic', 'Mystic'), ('Operative', 'Operative'), ('Solarian', 'Solarian'), ('Soldier', 'Soldier'),
                        ('Technomancer', 'Technomancer'))

THEMES = (('Ace Pilot', 'Ace Pilot'), ('Bounty Hunter', 'Bounty Hunter'), ('Icon', 'Icon'), ('Mercenary', 'Mercenary'), ('Outlaw', 'Outlaw'), ('Priest', 'Priest'),
                        ('Scholar', 'Scholar'), ('Spacefarer', 'Spacefarer'), ('Themeless', 'Themeless'), ('Xenoseeker', 'Xenoseeker'))

SIZES = (('Small', 'Small'), ('Medium', 'Medium'), ('Large', 'Large'))

ALIGNMENT = (('Lawful Good', 'Lawful Good'), ('Neutral Good', 'Neutral Good'), ('Chaotic Good', 'Chaotic Good'), ('Lawful Neutral', 'Lawful Neutral'), ('Neutral', 'Neutral'),
                        ('Chaotic Neutral', 'Chaotic Neutral'), ('Lawful Evil', 'Lawful Evil'), ('Neutral Evil', 'Neutral Evil'), ('Chaotic Evil', 'Chaotic Evil'))


class Character(models.Model):
    Player_Name = models.CharField(max_length=30)
    Character_Name = models.CharField(max_length=20)
    Race = models.CharField(max_length=20, choices=RACES)
    HP = models.IntegerField(default=00)
    Theme = models.CharField(max_length=20, choices=THEMES)
    Class = models.CharField(max_length=20, choices= CLASSES)
    Level = models.IntegerField(default=00)
    Size = models.CharField(max_length=20, choices=SIZES)
    Society = models.BooleanField(default=False, blank=True)
    Senses = models.CharField(max_length=20, blank=True)
    Speed = models.IntegerField(default=000)
    Gender = models.CharField(max_length=20, blank=True)
    Home_World = models.CharField(max_length=20, blank=True)
    Alignment = models.CharField(max_length=20, choices=ALIGNMENT)
    Deity = models.CharField(max_length=20, blank=True)
    Languages = models.CharField(max_length=20, blank=True)



    Characters = models.Manager()

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.toons = None

    def __str__(self):
        return self.Character_Name


class Items(models.Model):
    name = models.CharField(max_length=100)
    bulk = models.CharField(max_length=100)
    price = models.IntegerField(max_length=100)
    level = models.IntegerField(max_length=100)
    damage = models.CharField(max_length=100)
    range = models.IntegerField(max_length=100)
    critical = models.CharField(max_length=100)
    special = models.CharField(max_length=100)
    capacity = models.IntegerField(max_length=100)
    usage = models.IntegerField(max_length=100)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name