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
    path('snacks/actualizar-precios/',views.actualizar_precios,name="actualizar_precios"),
    #serializer
    path('pelicula_serializer/', views.PeliculaListSerializar, name="pelicula_list_serializer"),
    path('funcion_serializer/', views.FuncionListSerializar, name="funcion_list_serializer"),
    path('entrada_serializer/', views.EntradaListSerializar, name="entrada_list_serializer"),
    path('pelicula_list_vbc/',views.PeliculaList.as_view(),name='pelicula_list_vbc'),
    path('pelicula_create/',views.PeliculaCreate.as_view(),name='pelicula_create_vbc'),
    path('pelicula_edit_vc/<int:pk>',views.PeliculaUpdate.as_view() ,name='pelicula_edit_vc'),
    path('pelicula_delete_vc/<int:pk>',views.PeliculaDelete.as_view() ,name='pelicula_delete_vc'),
    #api
    path('pelicula_list_drf_def/',views.pelicula_api_view,name="pelicula_api_view"),
    path('snack_list_drf_def/', views.snack_api_view, name="snack_api_view"),
    path('entrada_list_drf_def',views.entrada_api_view,name="entrada_api_view"),
    path('top_vendidas/',views.peliculas_mas_vendidas,name="peliculas_mas_vendidas"),
    path('actualizar-precios/',views.actualizar_precios,name="actualizar-precios"),
]