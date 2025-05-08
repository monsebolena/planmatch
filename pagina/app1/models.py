from django.db import models
from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User

class Proyecto(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='proyectos/', blank=True, null=True)

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse('detalle_proyecto', args=[str(self.id)])

class Plan(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha = models.DateField()
    lugar = models.CharField(max_length=100)
    capacidad_maxima = models.PositiveIntegerField()
    creador = models.ForeignKey(User, on_delete=models.CASCADE, related_name='planes_creados')
    participantes = models.ManyToManyField(User, related_name='planes_apuntados', blank=True)

    def __str__(self):
        return self.titulo