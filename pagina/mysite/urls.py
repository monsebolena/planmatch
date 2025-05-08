"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='inicio'),
    path('registro/', views.registro, name='registro'),
    path('login/', views.login_view, name='login'),
    path('panel/', views.panel, name='panel'),
    path('crear_plan/', views.crear_plan, name='crear_plan'),
    path('logout/', views.logout_view, name='logout'),
    path('plan/editar/<int:plan_id>/', views.editar_plan, name='editar_plan'),
    path('plan/eliminar/<int:plan_id>/', views.eliminar_plan, name='eliminar_plan'),
    path('apuntarse/<int:plan_id>/', views.apuntarse_plan, name='apuntarse_plan'),







]
