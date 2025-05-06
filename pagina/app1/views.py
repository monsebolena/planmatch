
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Proyecto


def index(request):
    proyectos = Proyecto.objects.all()
    return render(request, "app1/index.html", {"proyectos": proyectos})

def recetas_cocina(request):
    return render(request, "app1/recetas.html")

def detalle_proyecto(request, id):
    proyecto = get_object_or_404(Proyecto, pk=id)
    return render(request, "app1/detalle_proyecto.html", {"proyecto": proyecto})

def peliculas_catalogo(request):
    return render(request, "app1/peliculas.html")

def videojuego_view(request):
    return render(request, 'app1/videojuego.html')

def tarot_view(request):
    return render(request, 'app1/tarot.html')

def biblioteca_virtual(request):
    return render(request, "app1/biblioteca.html")
