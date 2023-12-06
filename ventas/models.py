from django.db import models
from django.contrib.auth.models import User

class Clientes(models.Model):
   
    nombre_cli = models.CharField (max_length=20)
    apellido_cli = models.CharField(max_length=20)
    dni_cli = models.CharField(max_length=9)
    cuit_cli = models.CharField(max_length=13)
    tel_cli = models.CharField(max_length=22)
    dom_cli = models.CharField(max_length=40)
    email_cli = models.EmailField(max_length=254)

class FormaPago(models.Model):
    nombrepago = models.CharField(max_length=50)
    nombre = models.CharField(max_length=40)
    dni = models.CharField(max_length=9)
    num_tarjeta = models.CharField(max_length=16)
    codigo_seg = models.CharField(max_length=3)
    vencimiento = models.CharField(max_length=4)

class Campanas(models.Model):
    productos = models.ForeignKey("Productos", on_delete=models.DO_NOTHING)
    tipo_cam = models.CharField(max_length=20)
    nombre_cam = models.CharField(max_length=20)
    descripcion_camp = models.TextField()
    monto_cam = models.FloatField()

class Empleados(models.Model):
    nombre_emp = models.CharField (max_length=20)
    apellido_emp = models.CharField(max_length=20)
    dni_emp = models.CharField(max_length=9)
    tel_emp = models.CharField(max_length=22)
    dom_emp = models.CharField(max_length=40)

class Ventas(models.Model):
    user_cli = models.ForeignKey(User, on_delete=models.CASCADE)
    campana = models.ForeignKey("Campanas", on_delete=models.CASCADE)
    empleado = models.ForeignKey("Empleados", on_delete=models.DO_NOTHING)

class FacturaFinal(models.Model):
    cliente = models.ForeignKey('Clientes', on_delete=models.CASCADE)
    campanaeleg = models.ForeignKey('Campanas', on_delete=models.CASCADE)
    fecha_facfin = models.DateField(auto_now_add=True)
    hora_facfin = models.TimeField(auto_now_add=True)

class Tipo_De_Contrato(models.Model):
    tipo_contrato = models.CharField(max_length=50)

class Contratos(models.Model):
    contrato = models.ForeignKey("Tipo_De_Contrato", on_delete=models.CASCADE)
    venta = models.ForeignKey("Ventas", on_delete=models.DO_NOTHING)
    fecha_inicio = models.DateField(auto_now_add=True)
    fecha_fin = models.DateField(auto_now=True)

class Detalles (models.Model):
    contrato = models.ForeignKey("Contratos", on_delete=models.DO_NOTHING)
    nro_factura = models.ForeignKey("Facturas", on_delete=models.DO_NOTHING)
    forma_pago = models.ForeignKey("FormaPago", on_delete=models.DO_NOTHING)
    fecha = models.DateField(auto_now_add=True)
    hora = models.TimeField(auto_now_add=True)


class Cajas (models.Model):
    empleado = models.ForeignKey("Empleados", on_delete=models.DO_NOTHING)
    num_planilla = models.IntegerField()
    monto_inicial = models.FloatField()
    monto_final = models.FloatField()
    hora_inicio = models.TimeField(auto_now_add=True)
    hora_fin = models.TimeField(auto_now=True)

class Facturas (models.Model):
    caja = models.ForeignKey("Cajas", on_delete=models.DO_NOTHING)
    cliente = models.ForeignKey("Clientes", on_delete=models.CASCADE)
    tipo_fact = models.CharField(max_length=20)
    fecha_fact = models.DateField(auto_now_add=True)
    mont_fact = models.FloatField()

class Medios(models.Model):
    nombre_medio = models.CharField(max_length=50)
    empresa_medio = models.CharField(max_length=20)

class Camxmed (models.Model):
    campana = models.ForeignKey("Campanas", on_delete=models.DO_NOTHING)
    medio = models.ForeignKey("Medios", on_delete=models.DO_NOTHING)
    fecha_inicio = models.DateField(auto_now_add=True)
    fecha_fin = models.DateField(auto_now=True)

class Proveedores(models.Model):
    nombre_prov = models.CharField (max_length=20)
    apellido_prov = models.CharField(max_length=20)
    dni_prov = models.CharField(max_length=9)
    cuit_prov = models.CharField(max_length=13)
    tel_prov = models.CharField(max_length=22)
    dom_prov = models.CharField(max_length=40)

class Productos(models.Model):
    proveedor = models.ForeignKey("Proveedores", on_delete=models.DO_NOTHING)
    nombre_prod = models.CharField(max_length=50)
    precio_prod = models.FloatField()
    cantidad_prod = models.IntegerField()

