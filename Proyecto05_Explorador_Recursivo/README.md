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