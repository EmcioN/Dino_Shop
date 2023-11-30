from django.urls import path
from .views import view_profile, edit_profile

urlpatterns = [    
    path('user/profile/', view_profile, name='view_profile'),
    path('user/profile/edit/', edit_profile, name='edit_profile'),
]