from django import forms
from .models import Dinosaur


class DinosaurForm(forms.ModelForm):
    class Meta:
        model = Dinosaur
        fields = [
            'name', 'description', 'price', 'health',
            'attack_power', 'server', 'image', 'video_url'
        ]
