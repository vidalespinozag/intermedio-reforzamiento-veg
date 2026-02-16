from django.db.models import Q, F
from django.shortcuts import render

from pelicula.models import Pelicula

from funcion.models import Funcion

from entrada.models import Entrada

from snackCompra.models import SnackCompra


# Create your views here.


def obtener_entradas_por_funcion(data, funcion_id_buscado):
    entradas_filtradas = []

    for pelicula in data:
        for funcion in pelicula["funciones"]:
            if funcion["funcion_id"] == funcion_id_buscado:
                entradas_filtradas.extend(funcion["entradas"])

    return entradas_filtradas

def obtener_snacks_por_entrada(data, entrada_id_buscado):
    for pelicula in data:
        for funcion in pelicula["funciones"]:
            for entrada in funcion["entradas"]:
                if entrada["entrada_id"] == entrada_id_buscado:
                    total = sum(
                        snack["cantidad"] * snack["precio_unitario"]
                        for snack in entrada["snacks"]
                    )
                    return {
                        "snacks": entrada["snacks"],
                        "total_snacks": total
                    }
    return {
        "snacks": [],
        "total_snacks": 0
    }


def pelicula_list(request):
    # data_context = {
    #     'nombre': 'Katty',
    #     'edad':29,
    #     'pais': 'Perú'
    # }
    data_context = Pelicula.objects.all()
    return render(request, 'cine/peliculas_list.html', context= {'data':data_context})

def pelicula_unica(request):
    try:
        data_context = Pelicula.objects.get(
            titulo="moana 2",
            clasificacion="Animado"
        )
    except Pelicula.DoesNotExist:
        data_context = None
        print('No se encontró la película')
    return render(request, 'cine/pelicula_unica.html', context={'data': data_context})


def pelicula_contiene(request):
    query = request.GET.get('q','')
    print("QUERY : {}".format(query))

    results = (Q(titulo__icontains=query))


    data_context = Pelicula.objects.filter(results)

    return render(request, 'cine/peliculas_contiene.html', context= {'data':data_context})


def pelicula_termina(request):
    query = request.GET.get('q', '')
    print("QUERY : {}".format(query))

    results = (Q(titulo__endswith=query))

    data_context = Pelicula.objects.filter(results)

    return render(request, 'cine/peliculas_termina.html', context={'data': data_context})

def orden_mixto(request):
    data_context = Funcion.objects.order_by('estado','-fecha_horario')
    return render(request, 'cine/funciones_orden_mixto.html', context={'data': data_context})

def entradas_rango(request):
    data_context = Entrada.objects.all().order_by("id")[3:6]
    return render(request, 'cine/entradas_rango.html', context={'data': data_context})

def snacks_prefijo(request):
    query = request.GET.get('q', '')
    print("QUERY : {}".format(query))

    results = (Q(producto__startswith=query))

    data_context = SnackCompra.objects.filter(results)
    return render(request, 'cine/snacks_prefijo.html', context={'data': data_context})

def pelicula_actualizar(request):
    query = request.GET.get('q', '')
    pref = "Acc"
    data_context = Pelicula.objects.all()
    if query != "":
        update_peliculas = Pelicula.objects.filter(genero__startswith=pref).order_by("titulo").update(clasificacion = query)
        data_context = Pelicula.objects.filter(genero__startswith=pref).order_by("titulo")
    return render(request, 'cine/peliculas_actualizar.html', context={'data': data_context})

def entrada_eliminar(request, id_entrada):
    try:
        entrada = Entrada.objects.get(id=id_entrada)
        entrada.delete()
        data_context = {
            'response': 'Entrada eliminada: {}'.format(id_entrada),
        }
    except Entrada.DoesNotExist:
        data_context = {
            'response': 'No existe esa entrada',
        }
    return render(request, 'cine/entrada_eliminar.html', context={'data': data_context})

def actualizar_precios(request):
    min_precio = 17
    data_context = SnackCompra.objects.filter(precio_unitario__gte=min_precio)
    data_context.update(precio_unitario=F('precio_unitario') - 2)
    return render(request, 'cine/snacks_actualizar_precios.html', context={'data': data_context})

def pelicula_detail(request, id_pelicula):
    print("ID Pelicula: {}".format(id_pelicula))
    return render(request, 'cine/peliculas_detail.html', context={'pelicula': data_context[id_pelicula]})
def pelicula_funcion(request, id_pelicula):
    print("ID Pelicula: {}".format(id_pelicula))
    return render(request, 'cine/funciones_list.html', context={'pelicula': data_context[id_pelicula]})
def funcion_entrada(request, id_funcion):
    return render(request, 'cine/entradas_list.html', context={'funentr': obtener_entradas_por_funcion(data_context, id_funcion)})
def entrada_snacks(request, id_entrada):
    return render(request, 'cine/snacks_list.html', context={'funsnack': obtener_snacks_por_entrada(data_context, id_entrada)})
def cartelera(request):
    return render(request, 'cine/cartelera.html',context={'cartelera': data_context})