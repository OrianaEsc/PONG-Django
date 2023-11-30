from django.urls import path, include
from ventas import views

urlpatterns = [
    path('inicio/', views.inicio, name='inicio'),
]
