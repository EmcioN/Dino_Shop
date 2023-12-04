from django.urls import path
from .views import (
    view_basket, add_to_basket, increase_quantity, decrease_quantity
)

urlpatterns = [
    path('basket/', view_basket, name='view_basket'),
    path('add-to-basket/<int:dinosaur_id>/', add_to_basket,
         name='add_to_basket'),
    path('increase-quantity/<int:item_id>/', increase_quantity,
         name='increase_quantity'),
    path('decrease-quantity/<int:item_id>/', decrease_quantity,
         name='decrease_quantity'),
]
