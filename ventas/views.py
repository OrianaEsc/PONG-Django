from itertools import product
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from ventas.models import Productos, Campanas
from .form import FormClientes, LoginForm
from .form import FormClientes
from django.contrib.auth import logout

from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required
# #nose
from django.contrib.auth.models import Group
from imaplib import _Authenticator
from django.contrib import messages # Para mensajes de sesión

#EXEQUIEL

from django.shortcuts import redirect

# Create your views here.
def mi_logout(request):
    logout(request)
    # Limpia la sesión y redirige a la página deseada después del logout
    return redirect('login')


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

@login_required
def FacturaFinal(request):
    lastname = request.user.last_name
    firstname = request.user.first_name
    email = request.user.email 

    id_cliente = None
    if request.user.is_authenticated:
        id_cliente = request.user.id

    context = {'lastname': lastname, 'firstname': firstname, 'email': email, 'id_cliente': id_cliente}

    return render(request, 'factura.html', context)

def register(request):
    if request.method=='GET':
        return render(request, 'registration/register.html', {'form': FormClientes})

    if request.method == 'POST':
        form = FormClientes(request.POST)

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

def agregar_producto(request, producto_id):

    carro=carro(request)

    producto=Productos.objects.get(id=producto_id)

    carro.agregar(producto=producto)
    return redirect("tienda")

def eliminar_producto(request, producto_id):

    carro=carro(request)

    producto=producto.objects.get(id=producto_id)

    carro.eliminar(producto=Productos)
    return redirect("tienda")

def restar_producto(request, producto_id):

    carro=carro(request)

    producto=Productos.objects.get(id=producto_id)

    carro.restar(producto=Productos)
    return redirect("tienda")
