from django.contrib import admin
from ventas.models import Campanas, Productos, Proveedores, FormaPago

# Register your models here.
class cargarCampana(admin.ModelAdmin):
    pass

class cargarProducto(admin.ModelAdmin):
    pass

class Formas_de_pago(admin.ModelAdmin):
    pass

admin.site.register(Campanas)
admin.site.register(Productos)
admin.site.register(Proveedores)
admin.site.register(FormaPago)