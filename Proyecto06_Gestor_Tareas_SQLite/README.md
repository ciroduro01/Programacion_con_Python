# Proyecto N°6: Sistema de Gestión de Tareas

## Aplicación CRUD con Base de Datos SQLite

## 1\. Objetivo y Resumen

El objetivo de este proyecto es construir una aplicación de consola funcional que implemente las cuatro operaciones fundamentales de gestión de datos, conocidas como **CRUD** (*Create, Read, Update, Delete*), utilizando la biblioteca **`sqlite3`** de Python.

La aplicación permite a un usuario crear, ver, marcar como completada y eliminar tareas, asegurando que todos los datos persistan de forma segura en un archivo de base de datos (`tareas.db`) incluso después de cerrar el programa.

**Concepto Central:** Demostrar el manejo de una **Base de Datos Relacional Local** y la ejecución de sentencias **SQL** mediante Python.

-----

## 2\. Tecnologías y Herramientas Utilizadas

Este proyecto se basa en la integración directa de Python con su módulo de base de datos estándar.

  * **Lenguaje:** Python 3.x
  * **Base de Datos:** **SQLite** (Base de datos embebida, sin necesidad de un servidor externo).
  * **Módulo de Python:** **`sqlite3`** (Módulo estándar para interactuar con bases de datos compatibles con SQL).
  * **Técnica Central:** **SQL** (Sentencias `CREATE TABLE`, `INSERT`, `SELECT`, `UPDATE`, `DELETE`).
  * **Diseño de Software:** **Programación Orientada a Objetos (POO)**. La clase `DBManager` encapsula la conexión y todas las operaciones SQL.

-----

## 3\. Resultados Clave

El sistema ofrece un menú de consola simple pero robusto que permite realizar las siguientes operaciones de gestión de tareas:

| Operación | Método Python | Sentencia SQL Relacionada | Descripción |
| :--- | :--- | :--- | :--- |
| **C**reate (Crear) | `agregar_tarea(desc)` | `INSERT INTO...` | Permite añadir una nueva tarea a la tabla. |
| **R**ead (Leer) | `obtener_todas_las_tareas()` | `SELECT * FROM...` | Recupera y muestra la lista completa de tareas. |
| **U**pdate (Actualizar) | `marcar_como_completada(id)` | `UPDATE... SET...` | Modifica el estado de la tarea (de 0 a 1). |
| **D**elete (Eliminar) | `eliminar_tarea(id)` | `DELETE FROM...` | Remueve permanentemente una tarea. |

  * **Persistencia:** La conexión con la base de datos (`sqlite3.connect('tareas.db')`) asegura que las tareas añadidas se guarden en el archivo local y estén disponibles al volver a ejecutar el programa.
  * **Manejo de Transacciones:** El uso de `self.conn.commit()` tras cada modificación garantiza que los cambios se escriban de forma segura en el disco.

-----

## 4\. Desarrollo del Proyecto (Procedimiento)

La lógica del programa se divide en una clase para el manejo de la DB y una función principal para la interfaz de usuario.

1.  **Conexión y Setup:** La clase `DBManager` inicializa la conexión y llama a `crear_tabla()`. La función `crear_tabla()` ejecuta un `CREATE TABLE IF NOT EXISTS` para asegurar que la estructura de datos esté lista.
2.  **Abstracción SQL:** Cada método de la clase `DBManager` (ej. `agregar_tarea`, `eliminar_tarea`) es responsable de construir y ejecutar su correspondiente sentencia SQL, utilizando **parámetros seguros** (`?` y tuplas) para prevenir inyecciones SQL.
3.  **Interfaz de Usuario:** La función `main()` presenta un **menú cíclico** (`while True`) en la consola.
4.  **Gestión de Datos:** La lógica de usuario procesa la opción elegida y pide los datos necesarios (descripción o ID), los valida (`try/except` para los IDs), y llama al método apropiado del `DBManager`.
5.  **Cierre Seguro:** El método mágico `__del__` en la clase `DBManager` asegura que la conexión (`self.conn.close()`) se cierre cuando la instancia del objeto sea destruida, liberando el archivo de la base de datos.

-----

## 5\. Estructura del Repositorio y Archivos

El proyecto utiliza un archivo de código y genera el archivo de la base de datos automáticamente.

```
Programacion_con_Python/
└── Proyecto06_Gestor_Tareas_SQLite/
    ├── gestor_tareas_db.py # Lógica de la DB y la interfaz de usuario.
    ├── tareas.db           # (Generado automáticamente) IGNORADO - El archivo binario de la base de datos.
    └── README.md           # Documentación del proyecto.
```

-----

## 6\. Conclusiones

Este proyecto valida la habilidad de:

  * **Persistencia de Datos:** Implementación exitosa de un sistema que mantiene la información entre sesiones de ejecución.
  * **Conocimiento de SQL:** Dominio de las sentencias CRUD para interactuar con una base de datos relacional.
  * **Arquitectura de Software:** Uso adecuado de clases y encapsulamiento (POO) para separar la lógica de negocio (interfaz de usuario) de la lógica de acceso a datos (`DBManager`).
  * **Seguridad y Robustez:** Aplicación de **parámetros seguros** en las consultas para mitigar riesgos y manejo de excepciones.

-----

# Project N°6: Task Management System (CRUD Application with SQLite Database)

## 1. Objective and Summary

The objective of this project is to build a functional console application that implements the four fundamental data management operations, known as CRUD (Create, Read, Update, Delete), using the Python `sqlite3` library.

The application allows a user to create, view, mark as completed, and delete tasks, ensuring that all data is securely persisted in a database file (`tareas.db`) even after the program is closed.

**Key Concept**: To demonstrate the handling of a local relational database and the execution of SQL statements using Python.

---

## 2. Technologies and Tools Used

This project is based on the direct integration of Python with its standard database module.

* **Language**: Python 3.x
* **Database**: SQLite (Embedded database, no external server required). 
* **Python Module**: `sqlite3` (Standard module for interacting with SQL-compatible databases).
* **Core Technique**: SQL (CREATE TABLE, INSERT, SELECT, UPDATE, and DELETE statements).
* **Software Design**: Object-Oriented Programming (OOP). The `DBManager` class encapsulates the connection and all SQL operations.

---

## 3. Key Results

The system offers a simple yet robust console menu that allows the following task management operations:

| Operation | Python Method | Related SQL Statement | Description |
| :--- | :--- | :--- | :--- |
| **C**reate (Crear) | `agregar_tarea(desc)` | `INSERT INTO...` | Allows adding a new task to the table. |
| **R**ead (Leer) | `obtener_todas_las_tareas()` | `SELECT * FROM...` | Retrieves and displays the complete list of tasks.
| **U**pdate (Actualizar) | `marcar_como_completada(id)` | `UPDATE... SET...` | Modifies the task status (from 0 to 1). |
| **D**elete (Eliminar) | `eliminar_tarea(id)` | `DELETE FROM...` | Permanently removes a task. |

* **Persistence**: The database connection (`sqlite3.connect('tareas.db')`) ensures that added tasks are saved to the local file and available when the program is run again.
* **Transaction Management**: Using `self.conn.commit()` after each modification ensures that changes are safely written to disk.

---

## 4. Project Development (Procedure)

The program logic is divided into a class for database management and a main function for the user interface.

1. **Connection and Setup**: The `DBManager` class initializes the connection and calls `crear_tabla()`. The `crear_tabla()` function executes a `CREATE TABLE IF NOT EXISTS` statement to ensure the data structure is ready.
2. **SQL Abstraction**: Each method of the `DBManager` class (e.g., `agregar_tarea`, `eliminar_tarea`) is responsible for constructing and executing its corresponding SQL statement, using safe parameters (`?` and tuples) to prevent SQL injection.
3. **User Interface**: The `main()` function presents a looping menu (`while True`) in the console.
4. **Data Management**: User logic processes the selected option and requests the necessary data (description or ID), validates it (`try/except` for IDs), and calls the appropriate `DBManager` method.
5. **Safe Closure**: The magic method `__del__` in the `DBManager` class ensures that the connection (`self.conn.close()`) is closed when the object instance is destroyed, releasing the database file.

---

## 5. Repository and File Structure

The project uses a code file and automatically generates the database file.

```bash
Programacion_con_Python/
└── Proyecto06_Gestor_Tareas_SQLite/
    ├── gestor_tareas_db.py # Database logic and user interface.
    ├── tareas.db   # (Automatically generated) IGNORED - The binary database file.
    └── README.md    # Project documentation.
```

---

## 6. Conclusions

This project validates the ability to:

* **Data Persistence**: Successful implementation of a system that maintains information between execution sessions.
* **SQL Knowledge**: Mastery of CRUD statements for interacting with a relational database.
* **Software Architecture**: Appropriate use of classes and encapsulation (OOP) to separate business logic (user interface) from data access logic (DBManager).
* **Security and Robustness**: Application of secure parameters in queries to mitigate risks and handle exceptions.
