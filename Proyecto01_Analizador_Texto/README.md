# Proyecto N°1: Analizador de Frecuencia de Palabras

## 1\. Objetivo y Resumen

El objetivo principal de este proyecto es implementar una herramienta de **análisis de texto** capaz de procesar un archivo fuente, limpiar su contenido y determinar la frecuencia absoluta de cada palabra. El script identifica y reporta las **palabras más comunes**, proporcionando métricas clave como el total de palabras y la cantidad de palabras únicas.

**Valor Clave:** Demostrar el dominio de las estructuras de datos nativas de Python (diccionarios y la clase `Counter`) para resolver problemas de procesamiento de texto (NLP Básico).

## 2\. Tecnologías y Herramientas Utilizadas

Este es un proyecto puramente de Python, utilizando bibliotecas estándar (que no requieren `pip install`):

  * **Lenguaje:** Python 3.x
  * **Módulo Principal:** **`collections.Counter`** (Para el conteo eficiente de frecuencias).
  * **Módulo Estándar:** **`string`** (Para identificar y eliminar puntuación).
  * **Manejo de Archivos:** Funciones nativas de Python (`open`, `read`, `try-except`).

## 3\. Resultados Clave

El resultado del programa es un informe impreso en la consola con las siguientes métricas:

  * **Total de Palabras:** Conteo total de tokens en el archivo.
  * **Palabras Únicas:** Número de palabras distintas que aparecen en el texto.
  * **Top N Palabras Comunes:** Un listado de las 10 (o N) palabras con mayor frecuencia, mostrando su conteo.

### Ejemplo de Salida (Usando `texto_ejemplo.txt`):

```bash
--- INFORME DEL ANALIZADOR DE TEXTO ---
Archivo procesado con éxito.
Total de palabras: 55
Palabras únicas: 35
--------------------------------------

 TOP 10 PALABRAS MÁS COMUNES:
  - de: 4
  - python: 3
  - un: 3
  - la: 3
  - es: 2
  - lenguaje: 1
  - programación: 1
  - muy: 1
  - popular: 1
  - fácil: 1
--------------------------------------
```

## 4\. Desarrollo del Proyecto (Procedimiento)

El flujo de trabajo sigue una estructura clara de procesamiento por lotes dentro de la función `main()`:

1.  **Lectura con Manejo de Errores:** La función `leer_archivo()` usa `with open()` y bloques `try-except` para garantizar que el archivo se abre y se cierra correctamente, gestionando errores comunes como `FileNotFoundError`.
2.  **Normalización de Datos:** La función `limpiar_texto()` realiza la pre-limpieza de texto:
      * Convierte todo el texto a **minúsculas**.
      * Elimina todos los caracteres de **puntuación** (`string.punctuation`).
      * Divide el texto en una lista de palabras (tokens).
3.  **Conteo de Frecuencias:** Se utiliza la clase `collections.Counter` que simplifica y optimiza el proceso de conteo de las palabras en la lista.
4.  **Generación de Reporte:** La función `generar_reporte()` utiliza el método `most_common(N)` de `Counter` para obtener directamente el ranking de palabras.

## 5\. Estructura del Repositorio y Archivos

El proyecto consta de dos archivos clave:

```
Programacion_con_Python/
└── Proyecto01_Analizador_Texto/
    ├── main.py                   # Contiene toda la lógica del Analizador.
    ├── texto_ejemplo.txt         # Archivo de prueba para demostración.
    └── README.md                 # Documentación del proyecto.
```

## 6\. Conclusiones

Este proyecto refuerza las habilidades en:

  * **Manejo de Archivos y Excepciones:** Lectura de *I/O* de forma segura.
  * **Estructuras de Datos Avanzadas:** Uso de `collections.Counter` para resolver problemas de conteo de forma eficiente, demostrando comprensión más allá de los diccionarios básicos.
  * **Pre-procesamiento de Datos:** Aplicación de lógica para limpiar y normalizar datos textuales, un paso fundamental en cualquier proyecto de Análisis de Datos o Machine Learning.

-----