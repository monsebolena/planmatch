from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import PlanForm
from .models import Plan  # ¡IMPORTANTE!

# Página de inicio
def index(request):
    return render(request, 'app1/index.html')

# Landing (si la mantienes)
def landing(request):
    return render(request, 'app1/landing.html')

# Cerrar sesión
def logout_view(request):
    logout(request)
    return redirect('inicio')

# Registro de usuario
def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            return redirect('inicio')
    else:
        form = UserCreationForm()
    return render(request, 'app1/registro.html', {'form': form})

# Login de usuario
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('panel')
        else:
            return render(request, 'app1/login.html', {'form': True})
    return render(request, 'app1/login.html', {'form': False})

# Panel privado del usuario
@login_required
def panel(request):
    usuario = request.user
    planes_creados = Plan.objects.filter(creador=usuario)
    planes_apuntado = Plan.objects.filter(participantes=usuario)
    return render(request, 'app1/panel.html', {
        'planes_creados': planes_creados,
        'planes_apuntado': planes_apuntado
    })

# Crear un nuevo plan
@login_required
def crear_plan(request):
    print("==> Vista crear_plan cargada")  # consola

    if request.method == 'POST':
        print("==> Se recibió un POST")
        form = PlanForm(request.POST)
        if form.is_valid():
            print("==> Formulario válido")
            plan = form.save(commit=False)
            plan.creador = request.user
            plan.save()
            print("==> Plan guardado")
            return redirect('panel')
        else:
            print("==> Formulario inválido:", form.errors)
    else:
        print("==> GET: cargando formulario")
        form = PlanForm()

    return render(request, 'app1/crear_plan.html', {'form': form})

from django.shortcuts import get_object_or_404

# Editar un plan
@login_required
def editar_plan(request, plan_id):
    plan = get_object_or_404(Plan, id=plan_id, creador=request.user)
    if request.method == 'POST':
        form = PlanForm(request.POST, instance=plan)
        if form.is_valid():
            form.save()
            return redirect('panel')
    else:
        form = PlanForm(instance=plan)
    return render(request, 'app1/editar_plan.html', {'form': form, 'plan': plan})

# Eliminar un plan
@login_required
def eliminar_plan(request, plan_id):
    plan = get_object_or_404(Plan, id=plan_id, creador=request.user)
    if request.method == 'POST':
        plan.delete()
        return redirect('panel')
    return render(request, 'app1/eliminar_plan.html', {'plan': plan})
