from django.contrib import admin

from entrada.models import Entrada

# Register your models here.
#admin.site.register(Entrada)

@admin.register(Entrada)
class EntradaAdmin(admin.ModelAdmin):
    list_display = ('funcion','asiento','vendido')