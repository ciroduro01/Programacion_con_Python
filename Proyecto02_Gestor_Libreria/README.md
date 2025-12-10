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

### 💾 Estructura y Visualización de `libreria.json`

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
    },
    // ... más libros
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
    ├── libreria.json             # Archivo de persistencia de datos (diccionario de ISBNs).
    └── README.md                 # Documentación del proyecto.
```

## 6\. Conclusiones

Este proyecto demuestra un entendimiento fundamental de:

  * **Serialización de Datos:** Capacidad de convertir objetos complejos de Python (diccionarios) a un formato de texto universal (JSON) para el almacenamiento.
  * **Diseño Modular:** Separación clara entre las responsabilidades de la interfaz de usuario (menú) y las responsabilidades de persistencia de datos (JSON).
  * **Manejo de Excepciones de Persistencia:** Implementación de robustez para manejar fallos de *I/O* (Input/Output) y problemas de formato de archivos.

-----