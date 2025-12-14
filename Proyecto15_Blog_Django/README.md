# **Proyecto N°15: Blog Profesional con Django**

## Desarrollo de una Aplicación Web Full-Stack con Framework

## 1\. Objetivo y Resumen

El objetivo principal de este proyecto es migrar del microframework (como Flask) a un **framework web full-stack** completo, **Django**. Este proyecto demuestra la capacidad para desarrollar aplicaciones web profesionales que siguen el patrón de diseño **MVT (Model-View-Template)**.

Se construye la base de un blog funcional que incluye:

  * **Modelos de Base de Datos:** Definición de la estructura de datos (`Post`) en Python.
  * **Vistas Dinámicas:** Lógica para consultar los datos y pasarlos a la capa de presentación.
  * **Templates Avanzadas:** Uso de plantillas para renderizar una lista (`list.html`) y el detalle (`detail.html`) de publicaciones dinámicamente.

**Conceptos Centrales:** **Framework Web Full-Stack**, **Patrón MVT (Model-View-Template)**, **ORMs**, **Rutas de Django**, **Templates Dinámicas**.

-----

## 2\. Tecnologías y Herramientas Utilizadas

  * **Lenguaje:** Python 3.x
  * **Framework Web:** **Django** (incluye su propio ORM, sistema de rutas, y motor de plantillas).
  * **Base de Datos:** **SQLite** (Base de datos por defecto de Django).
  * **Herramientas Clave:** Sistemas **WSGI/ASGI** para el despliegue de la aplicación.

-----

## 3\. Desarrollo del Proyecto (Estructura MVT)

El proyecto se centra en la aplicación **`posts`**, ilustrando el flujo **MVT** para el manejo de colecciones de datos:

1.  **Modelo (`posts/models.py`):** Define la estructura de datos (`Post`).
2.  **Vista (`posts/views.py`):** Contiene la lógica para:
      * **Listar Posts:** Obtener todos los posts y enviarlos a la plantilla de lista.
      * **Detalle del Post:** Obtener un post específico por su ID y enviarlo a la plantilla de detalle.
3.  **Templates (`list.html` y `detail.html`):** La capa de presentación que recibe los datos de la Vista y los formatea en HTML para el usuario.

-----

## 4\. Estructura del Repositorio y Archivos

La estructura refleja una aplicación Django profesional completa, incluyendo todos los archivos de configuración estándar.

### Jerarquía de Carpetas

```
Programacion_con_Python/
└── Proyecto15_Blog_Django/
    ├── manage.py                   <-- Script de administración (esencial)
    ├── requirements.txt            <-- Dependencias de Python
    ├── .gitignore                  <-- Archivo para ignorar db.sqlite3, venv, etc.
    ├── blog_principal/             <-- Directorio del proyecto
    │   ├── settings.py             <-- Configuración global
    │   ├── urls.py                 <-- Mapeo de rutas raíz
    │   ├── wsgi.py / asgi.py       <-- Archivos de despliegue
    │   └── __init__.py
    └── posts/                      <-- Directorio de la aplicación 'posts'
        ├── models.py               <-- Definición de la tabla Post
        ├── views.py                <-- Lógica (funciones home, detalle)
        ├── urls.py                 <-- Mapeo de rutas específicas de la app
        ├── admin.py                <-- Registro del modelo en el Admin
        ├── apps.py                 <-- Configuración de la app
        ├── tests.py                <-- Pruebas unitarias
        ├── migrations/             <-- Historial de cambios de la DB (necesario)
        └── templates/
            └── posts/
                ├── list.html       <-- Muestra el listado de posts (index)
                └── detail.html     <-- Muestra un solo post
```

**Notas adicionales**
| Archivo/Carpeta | Función | Nota Importante |
| :--- | :--- | :--- |
| **`db.sqlite3`** | Archivo de Base de Datos. | **IGNORADO por Git** (archivo de datos binario). |
| `migrations/` | Historial de las tablas. | Para que otros puedan replicar la estructura de la base de datos. |

-----

## 5\. Conclusiones

Este proyecto demuestra un dominio avanzado de:

  * **Estructura de Proyectos Avanzada:** Manejo del patrón MVT (Model-View-Template) y la estructura modular de Django (Proyecto vs. Aplicación).
  * **Desarrollo Full-Stack:** Capacidad para manejar desde la persistencia de datos (Modelos) hasta la presentación dinámica (Templates).
  * **Preparación para Despliegue:** Inclusión de archivos WSGI/ASGI y configuración de rutas, mostrando entendimiento del ciclo de vida de una aplicación web profesional.

-----
