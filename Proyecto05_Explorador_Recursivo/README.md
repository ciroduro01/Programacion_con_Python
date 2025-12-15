# Proyecto N°5: Explorador de Árboles de Directorio

## Aplicación Práctica del Concepto de Recursividad

## 1\. Objetivo y Resumen

El objetivo principal de este proyecto es implementar un **Explorador de Árboles de Directorio** para demostrar la aplicación práctica y eficiente del concepto de **Recursividad**.

La aplicación toma una ruta de directorio (por ejemplo, `.` para la carpeta actual) y la recorre en profundidad, calculando el **tamaño total** que ocupa en disco y generando un reporte con los 5 archivos más grandes encontrados.

**Valor Clave:** Demostrar cómo la recursividad simplifica el recorrido de estructuras jerárquicas o anidadas (como un sistema de archivos).

-----

## 2\. Tecnologías y Herramientas Utilizadas

Este proyecto utiliza módulos nativos de Python diseñados específicamente para interactuar con el sistema operativo.

  * **Lenguaje:** Python 3.x
  * **Módulos del Sistema:**
      * **`os`**: Esencial para interactuar con el sistema operativo (listar directorios, verificar si es archivo/directorio, obtener tamaño).
      * **`sys`**: Para manejar argumentos de línea de comandos.
  * **Técnica Central:** **Recursividad** (la función `recorrer_directorio` se llama a sí misma).
  * **Utilidades:** Función de formateo (`formatear_bytes`) para mostrar el tamaño en unidades legibles (KB, MB, GB).

-----

## 3\. Resultados Clave

El programa finaliza con un reporte de resumen que consolida las métricas del análisis y presenta la información de manera legible.

### Reporte de Ejemplo

```
==================================================
RESULTADO DE LA EXPLORACIÓN
Total de archivos encontrados: 1250
Tamaño total: 3.54 GB
==================================================

Top 5 Archivos más Grandes:
- 1.25 GB   : /ruta/a/video_final.mp4
- 850.50 MB : /ruta/a/datos/backup.zip
- 200.12 MB : /ruta/a/instalador.exe
- 150.00 MB : /ruta/a/documento/temp.pdf
- 100.00 MB : /ruta/a/otro/archivo.log
--------------------------------------------------
```

  * **Manejo de Caso Base:** La recursividad termina al encontrar un **archivo** (se calcula su tamaño) o al encontrar una **carpeta vacía**.
  * **Manejo de Errores:** Incluye bloques `try/except` para manejar archivos o directorios a los que el usuario no tiene permisos de acceso (excepción `PermissionError`).

-----

## 4\. Desarrollo del Proyecto (Procedimiento)

El núcleo del proyecto reside en la función `recorrer_directorio`, que aplica la lógica recursiva:

1.  **Caso Base (Archivo):** Si la ruta actual es un archivo, se obtiene su tamaño, se añade a una lista global y se retorna su tamaño.
2.  **Paso Recursivo (Directorio):** Si la ruta es un directorio:
      * Se utiliza `os.listdir()` para obtener una lista de todos los elementos internos.
      * Por cada elemento, se llama a `recorrer_directorio` de forma recursiva, y el valor de retorno (el tamaño del subárbol) se suma al `tamano_total` del directorio padre.
3.  **Manejo de Errores OS:** Se implementa el manejo de excepciones de `PermissionError` para evitar que el programa se detenga al intentar acceder a directorios restringidos del sistema.
4.  **Post-Proceso:** Una vez que la recursividad termina, la función `mostrar_resultados` usa la lista global (`archivos_encontrados`) para calcular el tamaño total y encontrar los archivos más grandes mediante el ordenamiento.

-----

## 5\. Estructura del Repositorio y Archivos

El proyecto se encuentra en un único archivo de código ejecutable.

```
Programacion_con_Python/
└── Proyecto05_Explorador_Recursivo/
    ├── explorador_recursivo.py  # Implementación de la función recursiva.
    └── README.md                 # Documentación del proyecto.
```

-----

## 6\. Conclusiones

Este proyecto demuestra un entendimiento sólido de:

  * **Recursividad:** Capacidad para definir una función que se llama a sí misma para resolver un problema de naturaleza auto-similar.
  * **Módulos de Sistema:** Uso práctico de la biblioteca `os` para la interacción con el sistema de archivos.
  * **Manejo de Estructuras Jerárquicas:** Solución elegante al problema de recorrer estructuras de datos anidadas y profundas (como un árbol de directorios).
  * **Manejo de Excepciones:** Robustez ante errores comunes del sistema operativo.

-----

# Project N°5: Directory Tree Explorer (Practical Application of the Recursion Concept)

## 1. Objective and Summary

The main objective of this project is to implement a Directory Tree Explorer to demonstrate the practical and efficient application of the Recursion concept.

The application takes a directory path (for example, `.` for the current folder) and traverses it in depth, calculating the total disk space occupied and generating a report with the 5 largest files found.

**Key Value**: To demonstrate how recursion simplifies traversing hierarchical or nested structures (such as a file system).

---

## 2. Technologies and Tools Used

This project uses native Python modules specifically designed to interact with the operating system.

* **Language**: Python 3.x
* **System Modules**:
* **`os`**: Essential for interacting with the operating system (listing directories, verifying if it is a file/directory, obtaining size).
* **`sys`**: For handling command-line arguments.
* **Core Technique**: Recursion (the `recorrer_directorio` function calls itself).
* **Utilities**: Formatting function (`formatear_bytes`) to display the size in readable units (KB, MB, GB).

---

## 3. Key Results

The program concludes with a summary report that consolidates the analysis metrics and presents the information in a readable format.

### Sample Report (English Translation)

```bash
====================================================
SCAN RESULTS
Total files found: 1250
Total size: 3.54 GB
==================================================

Top 5 Largest Files:
- 1.25 GB: /path/to/video_final.mp4
- 850.50 MB: /path/to/data/backup.zip
- 200.12 MB: /path/to/installer.exe
- 150.00 MB: /path/to/document/temp.pdf
- 100.00 MB: /path/to/another/file.log
--------------------------------------------------
```

* **Base Case Handling**: Recursion ends when a file is found (its size is calculated) or when an empty folder is found.
* **Error Handling**: Includes `try/except` blocks to handle files or directories to which the user does not have access permissions (`PermissionError` exception).

---

## 4. Project Development (Procedure)

The core of the project resides in the `recorrer_directorio` function, which applies recursive logic:

1. **Base Case (File)**: If the current path is a file, its size is obtained, added to a global list, and its size is returned.
2. **Recursive Step (Directory)**: If the path is a directory:
* `os.listdir()` is used to obtain a list of all internal elements.
* For each element, the `recorrer_directorio` function is called recursively, and the return value (the size of the subtree) is added to the total size of the parent directory.
3. **OS Error Handling**: `PermissionError` exception handling is implemented to prevent the program from crashing when attempting to access restricted system directories.
4. **Post-Processing**: Once recursion finishes, the `mostrar_resultados` function uses the global list (`archivos_encontrados`) to calculate the total size and find the largest files by sorting them.

---

## 5. Repository and File Structure

The project is contained in a single executable code file.

```bash
Programacion_con_Python/
└── Proyecto05_Explorador_Recursivo/
    ├── explorador_recursivo.py  # Implementation of the recursive function.
    └── README.md   # Project documentation.
```

---

## 6. Conclusions

This project demonstrates a solid understanding of:

* **Recursion**: The ability to define a function that calls itself to solve a self-similar problem.
* **System Modules**: Practical use of the `os` library for interacting with the file system.
* **Handling Hierarchical Structures**: An elegant solution to the problem of traversing deep, nested data structures (such as a directory tree).
* **Exception Handling**: Robustness against common operating system errors.
