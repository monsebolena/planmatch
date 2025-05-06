from django.db import models
from django.urls import reverse

class Proyecto(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='proyectos/', blank=True, null=True)

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse('detalle_proyecto', args=[str(self.id)])

