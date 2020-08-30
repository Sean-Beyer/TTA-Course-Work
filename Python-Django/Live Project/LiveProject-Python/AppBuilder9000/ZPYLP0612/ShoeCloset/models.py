from django.db import models

TYPE_CHOICES = ('Athletic', 'Athletic'), ('Casual', 'Casual'), ('Work', 'Work'), ('Boots', 'Boots'), ('Other', 'Other')
BRAND_CHOICES = ('Adidas', 'Adidas'), ('Puma', 'Puma'), ('Nike', 'Nike'), ('Gucci', 'Gucci'), (
    'Michael Kors', 'Michael Kors')
COLOR_CHOICES = ('Black', 'Black'), ('White', 'White'), ('Navy', 'Navy'), ('Brown', 'Brown'), ('Oxblood', 'Oxblood'), (
    'Other', 'Other')


# Create your models here.,
class ShoeClosetModel(models.Model):
    type = models.CharField(max_length=30, default="blank", choices=TYPE_CHOICES)
    brand = models.CharField(max_length=30, default="blank", choices=BRAND_CHOICES)
    color = models.CharField(max_length=30, default="blank", choices=COLOR_CHOICES)
    size = models.DecimalField(default=0.00, max_digits=100, decimal_places=1)

    Shoes = models.Manager()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.errors = None

    def __str__(self):
        return self.type

    def is_valid(self):
        pass

