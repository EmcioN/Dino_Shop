from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('contact/', views.contact, name='contact'),
    path('success/', views.success, name='success_url'),
    path('patch-notes/', views.patch_notes, name='patch_notes'),
    path('subscribe/', views.subscribe_newsletter, name='subscribe_newsletter'),
]
