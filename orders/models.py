from django.db import models
from django.contrib.auth.models import User
from marketplace.models import Crop

class Order(models.Model):
    buyer = models.ForeignKey(User, on_delete=models.CASCADE)
    crop = models.ForeignKey(Crop, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    status = models.CharField(default="Pending", max_length=20)

    def __str__(self):
        return f"Order {self.id}"
