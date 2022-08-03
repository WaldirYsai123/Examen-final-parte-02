from django.shortcuts import render, HttpResponse

# Create your views here.


def inicio(request):
    mensaje = '¡Hola! Este es el Examen Final'
    return render(request, 'inicio.html', {'mensaje': mensaje})


def integrantes(request):
    integrantes = [ 'Rodriguez Mejia Jose Jean Piere',
                    'Azañero Espinoza Waldir',
                    'Diaz Seminario Daniel', ]
    return render(request,'integrantes.html',{'integrantes':integrantes})


def crear_productos(request):
    return render(request, 'crear-productos.html')


def crear_cursos(request):
    return render(request, 'crear-cursos.html')