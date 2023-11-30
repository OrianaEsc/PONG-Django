from django.contrib import admin
from ventas.models import Campanas, Productos

# Register your models here.
class cargarCampana(admin.ModelAdmin):
    pass
admin.site.register(Campanas)

class cargarProducto(admin.ModelAdmin):
    pass
admin.site.register(Productos)
