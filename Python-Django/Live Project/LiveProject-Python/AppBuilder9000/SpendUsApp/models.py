from django.db import models

# Sample content below, not functional
TYPE_CHOICES = (
    ('fuel','fuel'),
    ('food','food'),
    ('drink','drink'),
    ('hotel','hotel'),
    ('supplies','supplies'),
)

class Expense(models.Model):
    type = models.CharField(max_length=60, choices=TYPE_CHOICES)
    name = models.CharField(max_length=60, default="first and last name of purchaser...", blank=True, null=False)
    description = models.TextField(max_length=300, default="description of purchase...", blank=True)
    price = models.DecimalField(default=0.00, max_digits=10000, decimal_places=2)

    Expenses = models.Manager()

    def __str__(self):
        return self.name