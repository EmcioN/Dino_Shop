from django.db import models
from django.shortcuts import redirect


class Dinosaur(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    health = models.IntegerField()
    attack_power = models.IntegerField()
    server = models.CharField(max_length=100)
    image = models.ImageField(upload_to='product_images/')
    video_url = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name
        
class Sale(models.Model):
    dinosaur = models.ForeignKey(Dinosaur, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.dinosaur.name} - {self.quantity}"        

