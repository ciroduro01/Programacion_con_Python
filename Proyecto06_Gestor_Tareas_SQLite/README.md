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
    ├── tareas.db           # (Generado automáticamente) El archivo binario de la base de datos.
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