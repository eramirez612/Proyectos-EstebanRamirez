from django.contrib import admin
from serialApp.models import Inscritos, Instituciones
# Register your models here.

class InscritosAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'institucion', 'telefono', 'fechareserva', 'horareserva', 'estado', 'observacion']

admin.site.register(Inscritos, InscritosAdmin)

class InstitucionesAdmin(admin.ModelAdmin):
    list_display = ['id', 'institucion']
    
admin.site.register(Instituciones, InstitucionesAdmin)