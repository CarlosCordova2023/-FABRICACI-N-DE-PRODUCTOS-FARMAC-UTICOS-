from django.contrib import admin
from .models import Laboratorio, DirectorGeneral, Producto

class LaboratorioAdmin(admin.ModelAdmin):
    list_display = ('nombre',)

class DirectorGeneralAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'laboratorio')
    search_fields = ['nombre']  # Para facilitar la búsqueda

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'laboratorio', 'f_fabricacion', 'p_costo', 'p_venta')
    list_filter = ['laboratorio']  # Para filtrar por laboratorio

admin.site.register(Laboratorio, LaboratorioAdmin)
admin.site.register(DirectorGeneral, DirectorGeneralAdmin)
admin.site.register(Producto, ProductoAdmin)
