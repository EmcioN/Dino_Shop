from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('contact/', views.contact, name='contact'),
    path('success/', views.success, name='success_url'),
    path('patch-notes/', views.patch_notes, name='patch_notes'),
]
