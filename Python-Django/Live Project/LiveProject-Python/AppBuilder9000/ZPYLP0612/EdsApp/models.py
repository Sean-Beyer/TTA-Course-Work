from django.db import models


# Animal class
class Animal(models.Model):
    name = models.CharField(max_length=20)
    age = models.PositiveIntegerField(null=True, blank=True)

    class Meta:
        db_tablespace = "Animals"
        ordering = ['name']


# Dog class
class Dog(Animal):
    breed = models.CharField(max_length=20)
    HAIR_TYPES = [('short hair', 'short hair'),
                  ('long hair', 'long hair'),
                  ('curly hair', 'curly hair'), ]
    hair = models.CharField(max_length=20, choices=HAIR_TYPES, null=True)
    favorite_dog_park = models.CharField(max_length=50)

    def __Str__(self):
        return self.name


# Cat class
class Cat(Animal):
    breed = models.CharField(max_length=20)
    HAIR_TYPES = [('short hair', 'short hair'),
                  ('long hair', 'long hair'), ]
    hair = models.CharField(max_length=20, choices=HAIR_TYPES, null=True)

    def __Str__(self):
        return self.name


# Dragon class
class Dragon(Animal):
    fire_breathing = models.BooleanField()
    COLOR = {('black', 'black'),
             ('red', 'red'),
             ('green', 'green'),
             ('brown', 'brown'),
             ('yellow', 'yellow'), }

    def __Str__(self):
        return self.name
