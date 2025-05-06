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
from app1 import views as view
from django.conf import settings
from django.conf.urls.static import static
from app1 import views

urlpatterns = [
    path('', view.index, name='index'),
    path('admin/', admin.site.urls),
    path('recetas/', view.recetas_cocina, name='recetas_cocina'),
    path('peliculas/', view.peliculas_catalogo, name='peliculas_catalogo'),
    path('proyecto/<int:id>/', view.detalle_proyecto, name='detalle_proyecto'),
    path('videojuego/', view.videojuego_view, name='videojuego'),  # ✅ añadida esta línea
    path('tarot/', view.tarot_view, name='tarot'),
    path('biblioteca/', view.biblioteca_virtual, name='biblioteca_virtual'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

