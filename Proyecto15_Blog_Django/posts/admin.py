from django.contrib import admin

# Registramos los modelos aquí.
from .models import Post # Importamos el modelo

admin.site.register(Post) # Registramos el modelo