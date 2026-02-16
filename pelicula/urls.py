from django.urls import path
from . import views

urlpatterns=[
    path('', views.pelicula_list ,name='pelicula_list'),
    path('pelicula_details/<int:id_pelicula>', views.pelicula_detail ,name='pelicula_detail'),
    path('<int:id_pelicula>/funciones', views.pelicula_funcion ,name='pelicula_funcion'),
    path('funciones/<int:id_funcion>/entradas', views.funcion_entrada ,name='funcion_entrada'),
    path('entradas/<int:id_entrada>/snacks', views.entrada_snacks ,name='entrada_snacks'),
    path('cartelera/', views.cartelera ,name='cartelera'),
    path('unica/', views.pelicula_unica ,name='pelicula_unica'),
    path('contiene/', views.pelicula_contiene ,name='pelicula_contiene'),
    path('termina/', views.pelicula_termina ,name='pelicula_termina'),
    path('orden_mixto/', views.orden_mixto ,name='orden_mixto'),
    path('rango/', views.entradas_rango ,name='entradas_rango'),
    path('snack/prefijo',views.snacks_prefijo,name='snacks_prefijo'),
    path('actualizar',views.pelicula_actualizar ,name='pelicula_actualizar'),
    path('entradas/<int:id_entrada>/eliminar',views.entrada_eliminar, name="entrada_eliminar"),
    path('snacks/actualizar-precios/',views.actualizar_precios,name="actualizar_precios")
]