from django.db.models import Q, F, Count
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from pelicula.models import Pelicula

from funcion.models import Funcion

from entrada.models import Entrada
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from snackCompra.models import SnackCompra

from django.core import serializers as ssr

from pelicula.forms import PeliculaForm

from pelicula.serializers import PeliculaSerializer

from snackCompra.serializers import SnackSerializer

from entrada.serializers import EntradaSerializer


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
    return render(request, 'cine/peliculas_list.html', context={'data': data_context})


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
    query = request.GET.get('q', '')
    print("QUERY : {}".format(query))

    results = (Q(titulo__icontains=query))

    data_context = Pelicula.objects.filter(results)

    return render(request, 'cine/peliculas_contiene.html', context={'data': data_context})


def pelicula_termina(request):
    query = request.GET.get('q', '')
    print("QUERY : {}".format(query))

    results = (Q(titulo__endswith=query))

    data_context = Pelicula.objects.filter(results)

    return render(request, 'cine/peliculas_termina.html', context={'data': data_context})


def orden_mixto(request):
    data_context = Funcion.objects.order_by('estado', '-fecha_horario')
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
        update_peliculas = Pelicula.objects.filter(genero__startswith=pref).order_by("titulo").update(
            clasificacion=query)
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
    return render(request, 'cine/entradas_list.html',
                  context={'funentr': obtener_entradas_por_funcion(data_context, id_funcion)})


def entrada_snacks(request, id_entrada):
    return render(request, 'cine/snacks_list.html',
                  context={'funsnack': obtener_snacks_por_entrada(data_context, id_entrada)})


def cartelera(request):
    return render(request, 'cine/cartelera.html', context={'cartelera': data_context})


# serializer
def PeliculaListSerializar(request):
    list_pelicula = ssr.serialize('json', Pelicula.objects.all(), fields=["director"])
    return HttpResponse(list_pelicula, content_type="application/json")


def FuncionListSerializar(request):
    list_funcion = Funcion.objects.select_related('pelicula').values(
        'id',
        'estado',
        titulo=F('pelicula__titulo')
    )
    return JsonResponse(list(list_funcion), safe=False)


def EntradaListSerializar(request):
    list_entrada = Entrada.objects.select_related('funcion').values(
        'id',
        entrada=F('funcion__estado')
    )
    return JsonResponse(list(list_entrada), safe=False)


# clases

class PeliculaList(ListView):
    model = Pelicula
    template_name = 'cine/pelicula_list_vc.html'


class PeliculaCreate(CreateView):
    model = Pelicula
    form_class = PeliculaForm
    template_name = 'cine/pelicula_form.html'
    success_url = reverse_lazy('pelicula_list_vbc')


class PeliculaUpdate(UpdateView):
    model = Pelicula
    form_class = PeliculaForm
    template_name = 'cine/pelicula_update_vc.html'
    success_url = reverse_lazy('pelicula_list_vbc')


class PeliculaDelete(DeleteView):
    model = Pelicula
    success_url = reverse_lazy('pelicula_list_vbc')
    template_name = 'cine/pelicula_confirm_delete.html'


# @api_view(['GET','POST'])
# def pelicula_api_view(request):
#     if request.method == 'GET':
#         print("Ingreso a get")
#         queryset = Pelicula.objects.all()
#         serializer_class = PeliculaSerializer(queryset, many=True)
#         return Response(serializer_class.data, status=status.HTTP_200_OK)
#     elif request.method == 'POST':
#         serializer_class = PeliculaSerializer(data=request.data)
#         if serializer_class.is_valid():
#             serializer_class.save()
#             return Response(serializer_class.data, status=status.HTTP_201_CREATED)
#         return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)
#     return None
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])  # 401 si no está autenticado
def pelicula_api_view(request):
    # GET → Listar
    if request.method == 'GET':
        queryset = Pelicula.objects.all()
        serializer = PeliculaSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # POST → Crear
    elif request.method == 'POST':
        serializer = PeliculaSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED  # Creación exitosa
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST  # Error validación
        )

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def snack_api_view(request):
    if request.method == 'GET':
        print("Ingreso a get")
        queryset = SnackCompra.objects.all()
        serializer_class = SnackSerializer(queryset, many=True)
        return Response(serializer_class.data, status=status.HTTP_200_OK)
    return None


# @api_view(['DELETE'])
# @permission_classes([IsAuthenticated])
# def pelicula_details_view(request, pk):
#     pelicula = Pelicula.objects.get(id=pk)
#     if pelicula:
#         if request.method == 'DELETE':
#             pelicula.delete()
#             return Response("Eliminado de la base de datos correctamente.",status=status.HTTP_202_ACCEPTED)
#     return None
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def pelicula_details_view(request, pk):

    pelicula = get_object_or_404(Pelicula, pk=pk)  # 404 automático

    # Aquí puedes agregar control de autorización
    # ejemplo: solo staff puede eliminar
    if not request.user.is_staff:
        return Response(
            {"detail": "No autorizado"},
            status=status.HTTP_403_FORBIDDEN
        )

    pelicula.delete()

    return Response(
        {"detail": "Eliminado correctamente"},
        status=status.HTTP_204_NO_CONTENT  # Eliminación correcta
    )
@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def entrada_api_view(request):
    if request.method == 'GET':
        print("Ingreso a get")
        queryset = Entrada.objects.all()
        serializer_class = EntradaSerializer(queryset, many=True)
        return Response(serializer_class.data, status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer_class = EntradaSerializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data, status=status.HTTP_201_CREATED)
        return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)
    return None

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def peliculas_mas_vendidas(request):

    peliculas = (
        Pelicula.objects
        .annotate(
            total_entradas_vendidas=Count(
                'funcion__entrada',
                filter=Q(funcion__entrada__vendido=True)
            )
        )
        .filter(total_entradas_vendidas__gt=0)
        .order_by('-total_entradas_vendidas')
        .values('titulo', 'genero', 'total_entradas_vendidas')
    )

    return Response(peliculas, status=status.HTTP_200_OK)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def actualizar_precios(request):
    descuento = request.data.get("descuento")

    if not descuento:
        return Response(
            {"error": "Debe enviar el descuento"},
            status=status.HTTP_400_BAD_REQUEST
        )

    try:
        descuento = float(descuento)
    except ValueError:
        return Response(
            {"error": "Descuento inválido"},
            status=status.HTTP_400_BAD_REQUEST
        )

    if SnackCompra.objects.filter(precio_unitario__lt=descuento).exists():
        return Response(
            {"error": "El descuento no puede ser mayor al precio_unitario"},
            status=status.HTTP_400_BAD_REQUEST
        )
    SnackCompra.objects.update(
        precio_unitario=ExpressionWrapper(
            F('precio_unitario') - descuento,
            output_field=DecimalField(max_digits=5, decimal_places=2)
        )
    )
    snacks_actualizados = SnackCompra.objects.all()

    from .serializers import SnackSerializer
    serializer = SnackSerializer(snacks_actualizados, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)