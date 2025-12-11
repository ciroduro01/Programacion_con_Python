# posts/urls.py

from django.urls import path
from . import views # Importa las vistas creadas

# Define el namespace (espacio de nombres) para esta app. Útil para referenciar URLs.
app_name = 'posts' 

urlpatterns = [
    # La URL 'http://127.0.0.1:8000/blog/' se mapea a la función views.post_list
    path('', views.post_list, name='post_list'), 

    # La URL 'http://127.0.0.1:8000/blog/1/' se mapea a la función views.post_detail
    # <int:pk> es un placeholder que captura la ID del post.
    path('<int:pk>/', views.post_detail, name='post_detail'),
]