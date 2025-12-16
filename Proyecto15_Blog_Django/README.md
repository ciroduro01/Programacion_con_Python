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
  * **Preparación para Despliegue:** Inclusión de archivos WSGI/ASGI y configuración de rutas, mostrando entendimiento del ciclo de trabajo de una aplicación web profesional.

-----

# Project N°15: Professional Blog with Django (Developing a Full-Stack Web Application with a Framework)

## 1. Objective and Summary

The main objective of this project is to migrate from a microframework (such as **Flask**) to a complete full-stack web framework, **Django**. This project demonstrates the ability to develop professional web applications that follow the **MVT** (Model-View-Template) design pattern.

The foundation of a functional blog is built, including:

* **Database Models**: Definition of the data structure (`Post`) in Python.
* **Dynamic Views**: Logic for querying data and passing it to the presentation layer.
* **Advanced Templates**: Use of templates to dynamically render a list (`list.html`) and the details (`detail.html`) of posts.

**Core Concepts**: Full-Stack Web Framework, MVT (Model-View-Template) Pattern, ORMs, Django Routing, Dynamic Templates.

---

## 2. Technologies and Tools Used

* **Language**: Python 3.x
* **Web Framework**: Django (includes its own ORM, routing system, and template engine).
* **Database**: SQLite (Django's default database).
* **Key Tools**: WSGI/ASGI systems for application deployment.

---

## 3. Project Development (MVT Structure)

The project focuses on the `posts` application, illustrating the MVT flow for managing data collections:

1. **Model (`posts/models.py`)**: Defines the data structure (`Post`).
2. **View (`posts/views.py`)**: Contains the logic for:
* **Listing Posts**: Retrieving all posts and sending them to the list template.
* **Detailing a Post**: Retrieving a specific post by its ID and sending it to the detail template.
3. **Templates (`list.html` and `detail.html`)**: The presentation layer that receives the data from the View and formats it in HTML for the user.

---

## 4. Repository and File Structure

The structure reflects a complete professional Django application, including all standard configuration files.

### Folder Hierarchy

```bash
Programacion_con_Python/
└── Proyecto15_Blog_Django/
    ├── manage.py       # Administration script (essential)
    ├── requirements.txt    # Python dependencies
    ├── .gitignore   # File to ignore db.sqlite3, venv, etc.
    ├── blog_principal/   # Project directory
    │   ├── settings.py   # Global configuration
    │   ├── urls.py       # Root route mapping
    │   ├── wsgi.py / asgi.py  # Deployment files
    │   └── __init__.py
    └── posts/            # 'Posts' application directory
        ├── models.py     # Post table definition
        ├── views.py      # Logic (home, detail functions)
        ├── urls.py       # App-specific route mapping
        ├── admin.py      # Log from the model in the Admin
        ├── apps.py       # App configuration
        ├── tests.py      # Unit tests
        ├── migrations/   # Database change history (required)
        └── templates/
            └── posts/
                ├── list.html    # Displays the list of posts (index)
                └── detail.html  # Displays a single post
```

**Additional Notes**

| File/Folder | Function | Important Note |
| :--- | :--- | :--- |
| `db.sqlite3` | Database file. | IGNORED by Git (binary data file). |
| migrations/ | Table history. | So that others can replicate the database structure. |

---

## 5. Conclusions

This project demonstrates advanced mastery of:

* **Advanced Project Structure**: Handling the MVT (Model-View-Template) pattern and Django's modular structure (Project vs. Application).
* **Full-Stack Development**: Ability to manage everything from data persistence (Models) to dynamic presentation (Templates).
* **Deployment Preparation**: Inclusion of WSGI/ASGI files and route configuration, demonstrating an understanding of the professional web application workflow.
