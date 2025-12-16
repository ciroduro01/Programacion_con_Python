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
        └── inventario_api.db  # (Generado automáticamente) IGNORADO - Base de datos SQLite.
```

-----

## 6\. Conclusiones

Este proyecto demuestra un dominio avanzado de:

  * **Arquitectura Backend:** Capacidad para diseñar y construir una API RESTful funcional.
  * **Flask:** Dominio de las rutas, el manejo de métodos HTTP y la serialización JSON.
  * **Mapeo Objeto-Relacional (ORM):** Uso de Flask-SQLAlchemy para interactuar con bases de datos de manera orientada a objetos.
  * **Integridad de Datos:** Implementación de validaciones a nivel de base de datos (`unique=True`) y manejo de errores HTTP para una API robusta y profesional.

-----

# Project N°13: REST API for Inventory Management with Flask and ORM (Building a Backend Service with CRUD)

## 1. Objective and Overview

The main objective of this project is to build a web Application Programming Interface (API) to manage product inventory data.

The project uses the **Flask** framework to configure the server and the **Flask-SQLAlchemy** extension as an Object-Relational Mapper (**ORM**). This allows interaction with an SQLite database using Python code instead of pure SQL, which increases security and productivity.

The API follows **REST** (Representational State Transfer) principles by exposing endpoints with CRUD (Create, Read, Update, Delete) functionality for inventory management.

**Core Concepts**: REST API, Flask, ORM, JSON Serialization, and CRUD Pattern.

---

## 2. Technologies and Tools Used

This project is the culmination of database knowledge and an introduction to web architecture.

* **Language**: Python 3.x
* **Web Framework**: Flask (For handling HTTP routes and requests).
* **Database and ORM**: Flask-SQLAlchemy (For data persistence in the `inventory_api.db` file).
* **Exchange Format**: JSON (JavaScript Object Notation), used to send and receive data in requests and responses.
* **Key Techniques**:
* **HTTP Method Handling**: Implementation of the functions for `GET`, `POST`, `PUT`, and `DELETE`.
* **Serialization**: Use of the `to_dict()` method to convert Product class objects (ORM) into serializable JSON dictionaries.

---

## 3. API Routes (CRUD Endpoints)

The API defines two main endpoints (`/productos` and `/products/<id>`) that handle the four fundamental operations:

| HTTP Method | Route (Endpoint) | Operation Description |
| :--- | :--- | :--- |
| **POST** | `/productos` | **C**REATE: Creates a new product in the database. |
| **GET** | `/productos` | **R**EAD ALL: Retrieves the complete inventory list. |
| **GET** | `/productos/<id>` | **R**EAD ONE: Retrieves a specific product by its ID. |
| **PUT** | `/productos/<id>` | **U**PDATE: Modifies the data (name, price, stock) of a product. |
| **DELETE** | `/productos/<id>` | **D**ELETE: Deletes a product from the database. |

### Error Handling

The project includes professional error handling, such as the use of `abort(404)` for `Not Found` and the capture of SQLAlchemy's `IntegrityError` to prevent the insertion of duplicate product names, returning an HTTP 409 (Conflict) code.

---

## 4. Project Development (Structure and Components)

The project is modularized into the following components:

1. **Initialization (`app.py`)**: Configuration of the Flask application, including the database URI (SQLite) and the SQLAlchemy instance.
2. **ORM Model (`Producto` class)**: Defines the structure of the products table with columns for `id`, `nombre`, `precio`, and `stock`. The `unique=True` setting for the name is a database-level integrity constraint.
3. **Application Context**: Use of `with app.app_context()`: `db.create_all()` to ensure the table is created when the server starts for the first time.
4. **Route Controllers (Decorators)**: Functions marked with `@app.route()` handle incoming requests, query the database through the ORM, and return a JSON response.

---

## 5. Repository and File Structure

The project automatically generates a database file (`inventory_api.db`) upon startup.

```bash
Programacion_con_Python/
└── Proyecto13_API_REST_Flask/
    ├── app_inventario.py  # Main server logic and CRUD API.
    ├── README.md           # Project documentation.
    └── instance/
        └── inventario_api.db  # (Automatically generated) IGNORED! SQLite database.
```

---

## 6. Conclusions

This project demonstrates advanced mastery of:

* **Backend Architecture**: Ability to design and build a functional RESTful API.
* **Flask**: Mastery of routing, HTTP method handling, and JSON serialization.

* **Object-Relational Mapping (ORM)**: Use of Flask-SQLAlchemy to interact with databases in an object-oriented manner.

* **Data Integrity**: Implementation of database-level validations (`unique=True`) and HTTP error handling for a robust and professional API.
