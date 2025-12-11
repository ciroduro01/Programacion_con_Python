# Creamos las views aquí.
from django.shortcuts import render, get_object_or_404
from .models import Post

# Vista para LISTAR todos los posts
def post_list(request):
    # Obtiene todos los objetos Post de la base de datos
    # Los ordena por fecha de publicación (más nuevo primero)
    posts = Post.objects.filter(publicado=True).order_by('-fecha_publicacion')
    
    # Renderiza la plantilla 'posts/post_list.html' y le pasa los datos 'posts'
    return render(request, 'posts/post_list.html', {'posts': posts})

# Vista para ver un solo post
def post_detail(request, pk):
    # Busca un post por su clave primaria (pk) o muestra un error 404
    post = get_object_or_404(Post, pk=pk)
    
    # Renderiza la plantilla 'posts/post_detail.html' y le pasa el dato 'post'
    return render(request, 'posts/post_detail.html', {'post': post})