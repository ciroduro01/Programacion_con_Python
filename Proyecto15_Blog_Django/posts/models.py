from django.db import models

# Creamos los modelos aquí.
from django.utils import timezone

class Post(models.Model):
    # Campos de la tabla 'posts_post'
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    fecha_publicacion = models.DateTimeField(default=timezone.now)
    # Agregamos un campo para saber si está publicado
    publicado = models.BooleanField(default=True)

    def __str__(self):
        # Muestra el título del post en el Panel de Administración
        return self.titulo