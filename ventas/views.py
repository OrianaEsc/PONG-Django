from itertools import product
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from ventas.models import Productos, Campanas, User
from .form import FormClientes, LoginForm
from .form import FormClientes

# #nose
from django.contrib.auth.models import Group
from imaplib import _Authenticator
from django.contrib import messages # Para mensajes de sesión

#EXEQUIEL
from .carro import carro
from django.shortcuts import redirect

# Create your views here.
def inicio(request):
    datos = {}
    return render (request, 'index.html', datos)

def tipopago(request):
    datos = {}
    return render (request, 'tipopago.html', datos)

def contacto(request):
    datos = {}
    return render (request, 'contacto.html', datos)


def campanas(request):
    datos = {
        'campanas': Campanas.objects.all()
    }

    return render (request, 'campanas.html', datos)

def nosotros(request):
    datos = {}
    return render (request, 'nosotros.html', datos)

def proyectos(request):
    datos = {}
    return render (request,'proyectos.html', datos)

def tipocamp(request):
    campanas = Campanas.objects.all()
    context={
        'campana': campanas
    }
    return render (request,'tipocamp.html', context)

def FacturaFinal(request, cliente_id, campana_id):
    user = User.objects.get(id=cliente_id)
    campana = Campanas.objects.get(id=campana_id)

    if request.method == 'GET':
        form = Factura(request.POST)
        if form.is_valid():
            fact = form.save(commit=False)
            fact.cliente = cliente
            fact.save()
            
    context = {
        'form' : form,
        'cliente' : cliente 
    }

    return render (request, 'factura.html', context)

def register(request):
    if request.method=='GET':
        return render(request, 'registration/register.html', {'form': FormClientes})

    if request.method == 'POST':
        form = FormClientes(request.POST, request.FILES)

        if form.is_valid():
            user = form.save(commit=False)
            user.save()

            user = authenticate(
                username = form.cleaned_data['username'],
                password = form.cleaned_data['password1']
            )
            login(request, user)

            return redirect('inicio')
        else:
            return render(request, 'registration/register.html', {'form': form})

def Carrito(request, venta_id, user_id):
    ventas = ventas.objects.filter(carrito=True)

    context = {
        'ventas': ventas
    }

    return render (request, 'carrito.html', context)

def Terminarventa(request):
    ventas = ventas.objets.get(carrito=True)

    ventas.carrito = carrito = False
    
def agregarcarrito (request, User_id, Campana_id, Ventas):
    user = User.object.get(id=User_id)
    campana = Campanas.object.get(idcam = Campana_id)

    ventas = Ventas(
        user = User,
        campana = Campanas,
        carrito = True
    )
    ventas.save()