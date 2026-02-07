from django.urls import path
from . import views

urlpatterns=[
    path('', views.pelicula_list ,name='pelicula_list'),
    path('pelicula_details/<int:id_pelicula>', views.pelicula_detail ,name='pelicula_detail'),
    path('<int:id_pelicula>/funciones', views.pelicula_funcion ,name='pelicula_funcion'),
    path('funciones/<int:id_funcion>/entradas', views.funcion_entrada ,name='funcion_entrada'),
    path('entradas/<int:id_entrada>/snacks', views.entrada_snacks ,name='entrada_snacks'),
    path('cartelera/', views.cartelera ,name='cartelera'),
]