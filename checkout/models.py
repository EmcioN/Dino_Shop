from django.db import models
from django.contrib.auth.models import User
from products.models import Dinosaur


class Checkout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField()
    username_in_game = models.CharField(max_length=100)
    server = models.CharField(max_length=100)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)
    payment_method = models.CharField(max_length=50, default='Unknown')
    transaction_id = models.CharField(max_length=100, null=True)

    def __str__(self):
        return f"Checkout by {self.user.username} for {self.total_price}"


class OrderItem(models.Model):
    checkout = models.ForeignKey(Checkout, on_delete=models.CASCADE)
    dinosaur = models.ForeignKey(Dinosaur, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.dinosaur.name} in {self.checkout}"
