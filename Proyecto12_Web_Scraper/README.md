# Proyecto N°12: Web Scraper de Catálogo de Libros

## Extracción de Datos de la Web con Requests y BeautifulSoup

## 1\. Objetivo y Resumen

El objetivo principal de este proyecto es implementar un **Web Scraper** funcional para extraer datos estructurados de una página web pública.

El programa está diseñado para acceder a una página de catálogo de libros, simular ser un navegador (con `requests`) y luego parsear el código **HTML** y **CSS** (con `BeautifulSoup`) para obtener el título, el precio y el *rating* de cada libro. Esto demuestra la capacidad de obtener datos de fuentes web que no ofrecen una API de forma directa.

**Conceptos Centrales:** **Peticiones HTTP**, **Análisis de HTML (Parsing)** y uso de **Selectores CSS** para la extracción de datos.

-----

## 2\. Tecnologías y Herramientas Utilizadas

Este proyecto se basa en la integración de Python con librerías específicas para la interacción y análisis web.

  * **Lenguaje:** Python 3.x
  * **Peticiones HTTP:** **`requests`** (Para enviar la petición `GET` y recibir la respuesta).
  * **Análisis HTML (Parser):** **`BeautifulSoup`** (Para navegar, buscar y extraer elementos del árbol DOM).
  * **Técnica de Localización:** Uso de **Selectores CSS** (ej. `select()`) para identificar de forma precisa los elementos HTML que contienen la información deseada (títulos, precios).

-----

## 3\. Resultados Clave

El resultado fundamental es la capacidad de convertir datos no estructurados (HTML) en datos estructurados (una lista de diccionarios de Python).

### Robustez en la Extracción

El *scraper* demuestra buenas prácticas de extracción:

  * **Manejo de Errores HTTP:** Utiliza `respuesta.raise_for_status()` para detectar y manejar códigos de error comunes (403, 404, 500), evitando fallos silenciosos.
  * **Encabezados HTTP:** Incluye un `User-Agent` personalizado, que es esencial para evitar ser bloqueado por algunos sitios web.
  * **Manejo de Datos Faltantes:** Incluye bloques `try/except` o lógica condicional para manejar casos donde un elemento (como el *rating*) podría estar ausente o malformado en una tarjeta de libro, permitiendo que el *scraper* continúe.

-----

## 4\. Desarrollo del Proyecto (Procedimiento)

El flujo de trabajo se divide en dos fases principales, encapsuladas en funciones modulares:

1.  **Obtención del Contenido (`obtener_html`):**

      * Se configura la URL de destino y los encabezados.
      * Se realiza la llamada `requests.get()`.
      * Se retorna el texto HTML plano (`respuesta.text`).

2.  **Extracción de Datos (`extraer_datos_pagina`):**

      * Se inicializa `BeautifulSoup` para construir el árbol DOM.
      * Se usa el selector CSS (`.product_pod`) para identificar cada tarjeta de libro.
      * Dentro de cada tarjeta, se navega con selectores más específicos para obtener el título (`a` tag), el precio (`.price_color`) y la clase del *rating* (`.star-rating`).
      * Se formatea el resultado como un diccionario de Python.

-----

## 5\. Estructura del Repositorio y Archivos

El proyecto se encuentra en un único archivo de código ejecutable.

```
Programacion_con_Python/
└── Proyecto12_Web_Scraper/
    ├── scraper_libros.py   # Lógica de la petición y el parsing.
    └── README.md             # Documentación del proyecto.
```

-----

## 6\. Conclusiones

Este proyecto demuestra un dominio de:

  * **Conectividad Web:** Capacidad para realizar peticiones HTTP a servidores externos.
  * **Procesamiento de HTML:** Dominio de la librería **BeautifulSoup** para analizar y navegar el DOM (Document Object Model).
  * **Extracción Estructurada:** Habilidad para usar **selectores CSS** para extraer información de manera eficiente y específica.
  * **Consideraciones Éticas y de Robustez:** Uso de *User-Agents* y manejo de errores para una interacción respetuosa y estable con el servidor web.

-----