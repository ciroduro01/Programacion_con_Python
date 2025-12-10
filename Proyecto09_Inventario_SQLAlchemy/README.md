# Proyecto N°9: Sistema de Inventario con ORM

## Abstracción de Base de Datos con SQLAlchemy (Mapeo Objeto-Relacional)

## 1\. Objetivo y Resumen

El objetivo principal de este proyecto es implementar un sistema de gestión de inventario para el cumplimiento de las operaciones **CRUD**, utilizando la biblioteca **SQLAlchemy** como un **Mapeador Objeto-Relacional (ORM)**.

Este proyecto demuestra cómo **abstraer** la necesidad de escribir sentencias SQL manuales (como `SELECT * FROM...`) y en su lugar, manipular los datos de la base de datos (SQLite) como si fueran **objetos de Python**. Esto resulta en un código más limpio, seguro y fácil de mantener.

**Concepto Central:** Implementación de la capa **ORM** para simplificar la interacción con la base de datos.

-----

## 2\. Tecnologías y Herramientas Utilizadas

Este proyecto se basa en la integración de Python con una de las herramientas fundamentales del desarrollo web y de *backend*.

  * **Lenguaje:** Python 3.x
  * **ORM:** **SQLAlchemy** (Core y ORM Declarativo).
  * **Base de Datos:** **SQLite** (Motor de base de datos ligero utilizado para persistencia local).
  * **Componentes Clave de SQLAlchemy:**
      * `create_engine`: Para establecer la conexión física con la DB.
      * `declarative_base`: Para definir el modelo de la tabla.
      * `sessionmaker`: Para gestionar las transacciones (el equivalente al `commit()` de SQL manual).

-----

## 3\. Resultados Clave

El sistema permite gestionar el inventario a través de una aplicación de consola, pero la diferencia clave reside en la forma en que el código interactúa con la DB.

### Mapeo Objeto-Relacional

El resultado más importante es la **Clase Modelo `Producto`**, que funciona como un *esquema* de la tabla. Cada objeto instanciado (`Producto(nombre='Laptop', precio=800)`) se mapea directamente a una fila en la tabla `productos`.

| Operación SQL | Código ORM equivalente (Ejemplo) |
| :--- | :--- |
| `INSERT INTO productos...` | `session.add(Producto(...))` |
| `SELECT * FROM productos` | `session.query(Producto).all()` |
| `UPDATE productos SET...` | `producto.stock = nuevo_valor` y `session.commit()` |
| `DELETE FROM productos...` | `session.delete(producto)` |

  * **Seguridad:** El ORM maneja automáticamente la sanitización de entradas, haciendo que las consultas sean **inmunes a la inyección SQL**.
  * **Pythonic:** La gestión de datos es más intuitiva, utilizando la sintaxis de clases y objetos nativa de Python.

-----

## 4\. Desarrollo del Proyecto (Procedimiento)

El desarrollo se organiza en capas claras, separando la lógica de la base de datos de la lógica de la aplicación.

1.  **Configuración del Motor (`create_engine`):** Se establece el punto de conexión a la DB, especificando que se usará SQLite.
2.  **Definición del Modelo ORM:** Se crea la clase `Producto`, que hereda de `Base` y define los atributos (`id`, `nombre`, `precio`, `stock`) como columnas, especificando sus tipos de datos SQL (`Integer`, `String`, `Float`).
3.  **Creación de Tablas (`Base.metadata.create_all`):** Se asegura que el esquema de la tabla exista antes de que se inicie la aplicación.
4.  **Clase `InventarioManager`:** Esta clase centraliza la **lógica de negocio** y utiliza las sesiones (`sessionmaker`) para realizar todas las operaciones CRUD. Al usar `session.add()`, `session.delete()` y `session.commit()`, se gestionan las transacciones de manera abstracta.
5.  **Interfaz de Consola:** La función `main()` presenta el menú de usuario y llama a los métodos de la clase `InventarioManager`.

-----

## 5\. Estructura del Repositorio y Archivos

El proyecto consta del archivo de código y el archivo de base de datos generado por SQLAlchemy.

```
Programacion_con_Python/
└── Proyecto09_Inventario_SQLAlchemy/
    ├── inventario_orm.py   # Código principal con la implementación del ORM y la lógica CRUD.
    ├── inventario.db       # (Generado) El archivo binario de la base de datos SQLite.
    └── README.md           # Documentación del proyecto.
```

-----

## 6\. Conclusiones

Este proyecto valida la habilidad de:

  * **Dominio de ORM:** Uso de **SQLAlchemy** para mapear clases de Python a tablas de bases de datos.
  * **Abstracción de Datos:** Capacidad para interactuar con la DB sin necesidad de escribir SQL directamente, mejorando la legibilidad y seguridad del código.
  * **Patrón de Diseño:** Implementación de un **Modelo** de datos y un **Manager** de lógica de negocio, lo que es fundamental para aplicaciones grandes como APIs y *frameworks* web.
  * **Gestión de Sesiones:** Comprensión de cómo las sesiones de ORM manejan las transacciones de la base de datos.

-----