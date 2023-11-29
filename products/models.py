from django.db import models


class Dinosaur(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    health = models.IntegerField()
    attack_power = models.IntegerField()
    server = models.CharField(max_length=100)
    image = models.ImageField(upload_to='product_images/')

    def __str__(self):
        return self.name
        
class Sale(models.Model):
    dinosaur = models.ForeignKey(Dinosaur, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.dinosaur.name} - {self.quantity}"        