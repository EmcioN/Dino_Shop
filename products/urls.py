from django.urls import path
from . import views

urlpatterns = [
    path('dinosaurs/', views.all_dinosaurs, name='all_dinosaurs'),
    path('add/', views.add_dinosaur, name='add_dinosaur'),
    path('dinosaur/<int:dinosaur_id>/', views.item_page, name='item_page'),
    path('dinosaur/delete/<int:dinosaur_id>/',
         views.delete_dinosaur, name='delete_dinosaur'),
    path('dinosaur/edit/<int:dinosaur_id>/',
         views.edit_dinosaur, name='edit_dinosaur'),
]
