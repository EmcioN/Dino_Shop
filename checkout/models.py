from django.db import models
from django.contrib.auth.models import User
from products.models import Dinosaur

class Checkout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField()
    username_in_game = models.CharField(max_length=100)
    server = models.CharField(max_length=100)
    address = models.TextField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Checkout by {self.user.username} for {self.total_price}"