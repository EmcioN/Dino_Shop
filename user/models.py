from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pics/')
    age = models.PositiveIntegerField(null=True, blank=True)
    server = models.CharField(max_length=100)
    description = models.TextField(max_length=500, blank=True)
    facebook = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    instagram = models.URLField(blank=True)

    def get_transactions(self):
        return self.user.checkout_set.all()

    def __str__(self):
        return self.user.username
