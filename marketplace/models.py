from django.db import models
from django.contrib.auth.models import User

class Crop(models.Model):
    farmer = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.FloatField()
    quantity = models.IntegerField()
    image = models.ImageField(upload_to='crops/')
    description = models.TextField()

    def __str__(self):
        return self.name
