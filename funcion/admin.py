from django.contrib import admin

from funcion.models import Funcion

# Register your models here.


#admin.site.register(Funcion)
@admin.register(Funcion)
class FuncionAdmin(admin.ModelAdmin):
    list_display = ('pelicula','estado')
    list_filter = ('estado','fecha_horario')
    search_fields = ('estado',)