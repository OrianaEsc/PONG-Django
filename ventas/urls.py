from django.urls import path, include
from ventas import views
from django.views.generic import RedirectView
from ventas.views import register

urlpatterns = [
    path('', RedirectView.as_view(url='inicio')),
    path('inicio/', views.inicio, name='inicio'),

    path('contacto/', views.contacto, name='contacto'),
    path('campanas/', views.campanas, name='campanas'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('proyectos/', views.proyectos, name='proyectos'),

    path('tipocamp/', views.tipocamp, name='tipocamp'),
    path('accounts/register/', views.register, name='registrarse'),
#    path('carro/', views.Carrito, name='carro'),
    path('accounts/logout/', views.mi_logout, name='logout'),
    path('factura/', views.FacturaFinal, name='factura'),
    path('tipopago/', views.tipopago, name='tipopago'),
    path('accounts/', include('django.contrib.auth.urls')),


]
