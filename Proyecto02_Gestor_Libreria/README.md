# Proyecto N°2: Gestor de Inventario de Librería

## Persistencia de Datos con JSON

## 1\. Objetivo y Resumen

El objetivo principal de este proyecto es simular un **Sistema de Gestión de Inventario** de una librería, enfocado en el concepto de **Persistencia de Datos**. La aplicación permite al usuario realizar operaciones **CRUD** (Crear, Leer, Actualizar, Eliminar) sobre una colección de libros y garantiza que el estado de la librería se guarde automáticamente en un archivo **JSON** al salir, y se recargue al iniciar.

**Valor Clave:** Demostrar el manejo de estructuras de datos complejas (diccionarios anidados) y la capacidad de serializar/deserializar objetos Python a un formato persistente (JSON).

## 2\. Tecnologías y Herramientas Utilizadas

Este proyecto utiliza módulos estándar de Python, lo que lo hace fácilmente ejecutable en cualquier entorno básico.

  * **Lenguaje:** Python 3.x
  * **Módulo Principal:** **`json`** (Para la serialización y deserialización de datos).
  * **Módulos de Sistema:** **`os`** y **`sys`** (Para la verificación de la existencia del archivo de datos y el control de salida).
  * **Estructura de Datos Central:** Un diccionario de diccionarios, donde la **clave es el ISBN** del libro.

## 3\. Resultados Clave

El programa proporciona una interfaz de línea de comandos (CLI) con funcionalidades CRUD, siendo su resultado clave la **creación y gestión persistente** del inventario.

### Estructura y Visualización de `libreria.json` (Fragmento)

El inventario completo se almacena como un **objeto JSON principal**, donde cada clave es el ISBN único de un libro y su valor es un objeto (diccionario) con los detalles.

```json
{
    "978-0135905189": {
        "titulo": "Python Crash Course, 2nd Edition",
        "autor": "Eric Matthes",
        "año": 2019,
        "cantidad": 15
    },
    "978-8437604947": {
        "titulo": "Cien años de soledad",
        "autor": "Gabriel García Márquez",
        "año": 1967,
        "cantidad": 8
    }
}
```

*El sistema garantiza que si se cierra y se vuelve a abrir, los datos del inventario se mantendrán intactos.*

## 4\. Desarrollo del Proyecto (Procedimiento)

El desarrollo se enfoca en separar la lógica de negocio de la lógica de persistencia:

1.  **Módulo de Persistencia:** Las funciones `cargar_datos()` y `guardar_datos()` manejan exclusivamente la lectura (`json.load`) y escritura (`json.dump`) del archivo `libreria.json`. Se utiliza `ensure_ascii=False` para manejar caracteres especiales como tildes y eñes.
2.  **Lógica de Negocio (CRUD):** El resto de las funciones (`agregar_libro`, `buscar_libro`, `eliminar_libro`, etc.) operan únicamente sobre el diccionario de Python que representa la librería.
3.  **Flujo Principal:** La función `main()` llama a `cargar_datos()` al inicio y a `guardar_datos()` justo antes de salir del *loop* principal (`while True`), asegurando que todos los cambios se hagan persistentes.
4.  **Manejo de ISBN:** El ISBN actúa como la clave única y primaria dentro del diccionario, simplificando las búsquedas y eliminaciones.

## 5\. Estructura del Repositorio y Archivos

El proyecto se compone de dos archivos principales:

```
Programacion_con_Python/
└── Proyecto02_Gestor_Libreria/
    ├── libreria_manager.py       # Contiene toda la lógica del gestor (CRUD y JSON).
    ├── libreria.json             # IGNORADO - Archivo de persistencia de datos (diccionario de ISBNs).
    └── README.md                 # Documentación del proyecto.
```

## 6\. Conclusiones

Este proyecto demuestra un entendimiento fundamental de:

  * **Serialización de Datos:** Capacidad de convertir objetos complejos de Python (diccionarios) a un formato de texto universal (JSON) para el almacenamiento.
  * **Diseño Modular:** Separación clara entre las responsabilidades de la interfaz de usuario (menú) y las responsabilidades de persistencia de datos (JSON).
  * **Manejo de Excepciones de Persistencia:** Implementación de robustez para manejar fallos de *I/O* (Input/Output) y problemas de formato de archivos.

-----

# Project N°2: Library Inventory Manager (Data Persistence with JSON)

## 1. Objective and Summary

The main objective of this project is to simulate a Library Inventory Management System, focusing on the concept of Data Persistence. The application allows the user to perform **CRUD** (Create, Read, Update, Delete) operations on a collection of books and ensures that the library's state is automatically saved to a **JSON** file upon exit and reloaded upon startup.

**Key Value**: Demonstrate the handling of complex data structures (nested dictionaries) and the ability to serialize/deserialize Python objects to a persistent format (JSON).

## 2. Technologies and Tools Used

This project uses standard Python modules, making it easily executable in any basic environment.

* **Language**: Python 3.x
* **Main Module**: `json` (For data serialization and deserialization).
* **System Modules**: `os` and `sys` (For verifying the existence of the data file and output control).
* **Central Data Structure**: A dictionary of dictionaries, where the key is the book's **ISBN**.

## 3. Key Results

The program provides a command-line interface (CLI) with CRUD functionalities, its key result being the creation and persistent management of the inventory.

### Structure and Visualization of library.json (Excerpt)

The complete inventory is stored as a main JSON object, where each key is the unique ISBN of a book and its value is an object (dictionary) containing the details.

```json
{
"978-0135905189": {
"title": "Python Crash Course, 2nd Edition",
"author": "Eric Matthes",
"year": 2019,
"quantity": 15

}
"978-8437604947": {
"title": "One Hundred Years of Solitude",
"author": "Gabriel García Márquez",
"year": 1967,
"quantity": 8

}
}
```

* The system guarantees that if it is closed and reopened, the inventory data will remain intact.

## 4. Project Development (Procedure)

The development focuses on separating the business logic from the persistence logic:

1. **Persistence Module**: The functions `cargar_datos()` and `guardar_data()` exclusively handle reading (json.load) and writing (json.dump) to the `libreria.json` file. `ensure_ascii=False` is used to handle special characters such as accented letters and the letter ñ.
2. **Business Logic (CRUD)**: The remaining functions (`agregar_libro`, `buscar_libro`, `eliminar_libro`, etc.) operate solely on the Python dictionary that represents the library.
3. **Main Flow**: The `main()` function calls `cargar_datos()` at the beginning and `guardar_datos()` just before exiting the main loop (`while True`), ensuring that all changes are persisted.
4. **ISBN Handling**: The ISBN acts as the unique and primary key within the dictionary, simplifying searches and deletions.

## 5. Repository and File Structure

The project consists of two main files:

```bash
Programacion_con_Python/
└── Proyecto02_Gestor_Libreria/
├── libreria_manager.py # Contains all the manager logic (CRUD and JSON).
├── libreria.json # IGNORED - Data persistence file (ISBN dictionary).
└── README.md # Project documentation.

```

## 6. Conclusions
This project demonstrates a fundamental understanding of:

* **Data Serialization**: The ability to convert complex Python objects (dictionaries) to a universal text format (JSON) for storage.
* **Modular Design**: Clear separation between user interface (menu) responsibilities and data persistence (JSON) responsibilities.
* **Persistence Exception Handling**: Robust implementation to handle I/O (Input/Output) failures and file format problems.
