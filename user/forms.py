from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = [
            'profile_picture', 'age', 'server', 'description',
            'facebook', 'twitter', 'instagram'
            ]
