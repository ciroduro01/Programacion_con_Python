# Proyecto N°13: API REST de Inventario con Flask y ORM

## Construcción de un Servicio Backend con CRUD

## 1\. Objetivo y Resumen

El objetivo principal de este proyecto es construir una **Interfaz de Programación de Aplicaciones (API)** web que gestione los datos de un inventario de productos.

El proyecto utiliza el *framework* **Flask** para configurar el servidor y la extensión **Flask-SQLAlchemy** como **Mapeador Objeto-Relacional (ORM)**. Esto permite interactuar con una base de datos **SQLite** usando código Python en lugar de SQL puro, lo cual aumenta la seguridad y la productividad.

La API sigue los principios **REST** (Representational State Transfer) al exponer *endpoints* con la funcionalidad **CRUD** (Create, Read, Update, Delete) para la gestión del inventario.

**Conceptos Centrales:** **API REST**, **Flask**, **ORM**, **Serialización JSON** y **Patrón CRUD**.

-----

## 2\. Tecnologías y Herramientas Utilizadas

Este proyecto es la culminación de los conocimientos de bases de datos y la introducción a la arquitectura web.

  * **Lenguaje:** Python 3.x
  * **Framework Web:** **Flask** (Para manejar rutas y peticiones HTTP).
  * **Base de Datos y ORM:** **Flask-SQLAlchemy** (Para la persistencia de datos en el archivo `inventario_api.db`).
  * **Formato de Intercambio:** **JSON** (JavaScript Object Notation), utilizado para enviar y recibir datos en las peticiones y respuestas.
  * **Técnicas Clave:**
      * **Manejo de Métodos HTTP:** Implementación de las funciones para `GET`, `POST`, `PUT` y `DELETE`.
      * **Serialización:** Uso del método `to_dict()` para convertir objetos de la clase **Producto** (ORM) en diccionarios JSON serializables.

-----

## 3\. Rutas de la API (Endpoints CRUD)

La API define dos *endpoints* principales (`/productos` y `/productos/<id>`) que manejan las cuatro operaciones fundamentales:

| Método HTTP | Ruta (Endpoint) | Descripción de la Operación |
| :--- | :--- | :--- |
| **POST** | `/productos` | **C**REATE: Crea un nuevo producto en la base de datos. |
| **GET** | `/productos` | **R**EAD ALL: Obtiene la lista completa del inventario. |
| **GET** | `/productos/<id>` | **R**EAD ONE: Obtiene un producto específico por su ID. |
| **PUT** | `/productos/<id>` | **U**PDATE: Modifica los datos (nombre, precio, stock) de un producto. |
| **DELETE** | `/productos/<id>` | **D**ELETE: Elimina un producto de la base de datos. |

### Manejo de Errores

El proyecto incluye manejo de errores profesionales, como el uso de `abort(404)` para `Not Found` y la captura de `IntegrityError` de SQLAlchemy para evitar la inserción de nombres de productos duplicados, retornando un código HTTP **409 (Conflict)**.

-----

## 4\. Desarrollo del Proyecto (Estructura y Componentes)

El proyecto está modularizado en los siguientes componentes:

1.  **Inicialización (`app.py`):** Configuración de la aplicación Flask, incluyendo el URI de la base de datos (SQLite) y la instancia de `SQLAlchemy`.
2.  **Modelo ORM (`class Producto`):** Define la estructura de la tabla `productos` con columnas para `id`, `nombre`, `precio` y `stock`. La configuración `unique=True` en el nombre es una restricción de integridad a nivel de base de datos.
3.  **Contexto de Aplicación:** Uso de `with app.app_context(): db.create_all()` para asegurar que la tabla se cree al iniciar el servidor por primera vez.
4.  **Controladores de Ruta (Decoradores):** Las funciones marcadas con `@app.route()` manejan las peticiones entrantes, consultan la base de datos a través del ORM y devuelven una respuesta JSON.

-----

## 5\. Estructura del Repositorio y Archivos

El proyecto genera automáticamente un archivo de base de datos (`inventario_api.db`) al iniciar.

```
Programacion_con_Python/
└── Proyecto13_API_REST_Flask/
    ├── app_inventario.py   # Lógica principal del servidor y la API CRUD.
    ├── README.md             # Documentación del proyecto.
    └── instance/
        └── inventario_api.db  # (Generado automáticamente) Base de datos SQLite.
```

-----

## 6\. Conclusiones

Este proyecto demuestra un dominio avanzado de:

  * **Arquitectura Backend:** Capacidad para diseñar y construir una API RESTful funcional.
  * **Flask:** Dominio de las rutas, el manejo de métodos HTTP y la serialización JSON.
  * **Mapeo Objeto-Relacional (ORM):** Uso de Flask-SQLAlchemy para interactuar con bases de datos de manera orientada a objetos.
  * **Integridad de Datos:** Implementación de validaciones a nivel de base de datos (`unique=True`) y manejo de errores HTTP para una API robusta y profesional.

-----