from django.contrib import admin

from pelicula.models import Pelicula

# Register your models here.


#admin.site.register(Pelicula)

@admin.register(Pelicula)
class PeliculaAdmin(admin.ModelAdmin):
    list_display = ('titulo','genero','clasificacion')
    search_fields = ('titulo','genero')
    list_filter = ('genero','clasificacion')