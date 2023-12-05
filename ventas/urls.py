from django.urls import path, include
from ventas import views

urlpatterns = [
    path('', views.inicio, name = 'inicio'),
    path('inicio/', views.inicio, name='inicio'),

    path('contacto/', views.contacto, name='contacto'),
    path('campanas/', views.campanas, name='campanas'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('proyectos/', views.proyectos, name='proyectos'),

    path('tipocamp/', views.tipocamp, name='tipocamp'),
    # path('login/', login_view, name='login'),
    path('accounts/register/', views.register, name='registrarse'),
    path('carrito/', views.carro, name= 'carrito'),
    path('carro/', views.Carrito, name='carro')

]
