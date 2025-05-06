from django.shortcuts import render

def index(request):
    return render(request, 'app1/index.html')

def el_centro(request):
    return render(request, 'app1/el_centro.html')

def quien_soy(request):
    return render(request, 'app1/quien_soy.html')

def servicios(request):
    return render(request, 'app1/servicios.html')

def contacto(request):
    return render(request, 'app1/contacto.html')

def comprar(request):
    return render(request, 'app1/comprar.html')

