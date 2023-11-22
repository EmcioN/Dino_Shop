from django.urls import path
from . import views  

urlpatterns = [
    path('dinosaurs/', views.all_dinosaurs, name='all_dinosaurs'),
    path('add/', views.add_dinosaur, name='add_dinosaur'),  
]