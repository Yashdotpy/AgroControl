from django.db import models
from django.contrib.auth.models import User

from django.db import models
from django.contrib.auth.models import User

class Crop(models.Model):
    UNIT_CHOICES = (
        ('kg', 'Kilogram'),
        ('quintal', 'Quintal'),
    )

    farmer = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.FloatField(help_text="Price per unit")
    unit = models.CharField(max_length=10, choices=UNIT_CHOICES, default='kg')
    quantity = models.FloatField(help_text="Available quantity in selected unit")
    image = models.ImageField(upload_to='crops/')
    description = models.TextField()

    def __str__(self):
        return f"{self.name} ({self.unit})"
