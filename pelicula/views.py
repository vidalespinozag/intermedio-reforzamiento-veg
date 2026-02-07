from django.shortcuts import render

# Create your views here.

data_context = [
    {
        'id': 1,
        'titulo': '300',
        'duracion_min': '140',
        'genero': 'Accion',
        'clasificacion': '+18',
        'activa': False,
        'funciones': [
            {
                'funcion_id': 1,
                'fecha_horario': '07-02-2026 16:00',
                'precio': 35,
                'estado': 'agotado',
                'entradas': [
                    {
                        'entrada_id': 1,
                        'codigo': 'E001',
                        'asiento': 'A1',
                        'estado': 'VENDIDA',
                        'fecha_venta': '2026-02-01',
                        'snacks': [
                            {'producto': 'Popcorn', 'cantidad': 2, 'precio_unitario': 8},
                            {'producto': 'Gaseosa', 'cantidad': 1, 'precio_unitario': 5},
                        ]
                    }
                ]
            },
            {
                'funcion_id': 2,
                'fecha_horario': '07-02-2026 19:00',
                'precio': 40,
                'estado': 'agotado',
                'entradas': []
            },
            {
                'funcion_id': 3,
                'fecha_horario': '07-02-2026 22:30',
                'precio': 30,
                'estado': 'activo',
                'entradas': []
            },
        ]
    },

    {
        'id': 2,
        'titulo': 'La llorona',
        'duracion_min': '180',
        'genero': 'Terror',
        'clasificacion': '+18',
        'activa': False,
        'funciones': [
            {
                'funcion_id': 4,
                'fecha_horario': '07-02-2026 10:00',
                'precio': 30,
                'estado': 'agotado',
                'entradas': []
            },
            {
                'funcion_id': 5,
                'fecha_horario': '07-02-2026 13:00',
                'precio': 30,
                'estado': 'agotado',
                'entradas': []
            },
            {
                'funcion_id': 6,
                'fecha_horario': '07-02-2026 21:00',
                'precio': 35,
                'estado': 'agotado',
                'entradas': []
            },
        ]
    },

    {
        'id': 3,
        'titulo': 'Moana',
        'duracion_min': '120',
        'genero': 'Animacion',
        'clasificacion': '+10',
        'activa': True,
        'funciones': [
            {
                'funcion_id': 7,
                'fecha_horario': '07-02-2026 15:00',
                'precio': 40,
                'estado': 'activo',
                'entradas': []
            },
            {
                'funcion_id': 8,
                'fecha_horario': '07-02-2026 17:00',
                'precio': 45,
                'estado': 'activo',
                'entradas': [
                    {
                        'entrada_id': 2,
                        'codigo': 'E010',
                        'asiento': 'C3',
                        'estado': 'VENDIDA',
                        'fecha_venta': '2026-02-02',
                        'snacks': [
                            {'producto': 'Nachos', 'cantidad': 1, 'precio_unitario': 7.5}
                        ]
                    }
                ]
            },
            {
                'funcion_id': 9,
                'fecha_horario': '07-02-2026 19:30',
                'precio': 40,
                'estado': 'activo',
                'entradas': []
            },
        ]
    },

    {
        'id': 4,
        'titulo': 'Que paso ayer?',
        'duracion_min': '150',
        'genero': 'Comedia',
        'clasificacion': '+15',
        'activa': True,
        'funciones': [
            {
                'funcion_id': 10,
                'fecha_horario': '07-02-2026 11:00',
                'precio': 25,
                'estado': 'agotado',
                'entradas': []
            },
            {
                'funcion_id': 11,
                'fecha_horario': '07-02-2026 14:00',
                'precio': 25,
                'estado': 'activo',
                'entradas': []
            },
            {
                'funcion_id': 12,
                'fecha_horario': '07-02-2026 18:00',
                'precio': 30,
                'estado': 'activo',
                'entradas': []
            },
        ]
    },

    {
        'id': 5,
        'titulo': 'La La Land',
        'duracion_min': '200',
        'genero': 'Musical',
        'clasificacion': '+10',
        'activa': True,
        'funciones': [
            {
                'funcion_id': 13,
                'fecha_horario': '07-02-2026 09:00',
                'precio': 28,
                'estado': 'agotado',
                'entradas': []
            },
            {
                'funcion_id': 14,
                'fecha_horario': '07-02-2026 13:00',
                'precio': 28,
                'estado': 'activo',
                'entradas': []
            },
            {
                'funcion_id': 15,
                'fecha_horario': '07-02-2026 20:00',
                'precio': 35,
                'estado': 'activo',
                'entradas': []
            },
        ]
    },

    {
        'id': 6,
        'titulo': 'Avengers',
        'duracion_min': '160',
        'genero': 'Accion',
        'clasificacion': '+13',
        'activa': True,
        'funciones': [
            {
                'funcion_id': 16,
                'fecha_horario': '07-02-2026 16:00',
                'precio': 45,
                'estado': 'activo',
                'entradas': []
            },
            {
                'funcion_id': 17,
                'fecha_horario': '07-02-2026 19:00',
                'precio': 50,
                'estado': 'activo',
                'entradas': [
                    {
                        'entrada_id': 3,
                        'codigo': 'E020',
                        'asiento': 'D5',
                        'estado': 'VENDIDA',
                        'fecha_venta': '2026-02-03',
                        'snacks': [
                            {'producto': 'Hot Dog', 'cantidad': 2, 'precio_unitario': 6},
                            {'producto': 'Frank Futter', 'cantidad': 1, 'precio_unitario': 25}
                        ]
                    },
                    {
                        'entrada_id': 4,
                        'codigo': 'E021',
                        'asiento': 'E4',
                        'estado': 'VENDIDA',
                        'fecha_venta': '2026-02-04',
                        'snacks': [
                            {'producto': 'Hot Dog', 'cantidad': 2, 'precio_unitario': 6}
                        ]
                    }

                ]
            },
            {
                'funcion_id': 18,
                'fecha_horario': '07-02-2026 22:00',
                'precio': 55,
                'estado': 'activo',
                'entradas': []
            },
        ]
    },

    {
        'id': 7,
        'titulo': 'Toy Story',
        'duracion_min': '100',
        'genero': 'Animacion',
        'clasificacion': 'TP',
        'activa': True,
        'funciones': [
            {
                'funcion_id': 19,
                'fecha_horario': '07-02-2026 10:00',
                'precio': 25,
                'estado': 'activo',
                'entradas': []
            },
            {
                'funcion_id': 20,
                'fecha_horario': '07-02-2026 12:00',
                'precio': 30,
                'estado': 'activo',
                'entradas': []
            },
            {
                'funcion_id': 21,
                'fecha_horario': '07-02-2026 15:00',
                'precio': 30,
                'estado': 'activo',
                'entradas': []
            },
        ]
    },
]
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
    return render(request, 'cine/peliculas_list.html', context= {'data':data_context})

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