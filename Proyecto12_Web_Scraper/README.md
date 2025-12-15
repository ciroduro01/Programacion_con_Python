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

# Project N°12: Book Catalog Web Scraper (Web Data Extraction with Requests and BeautifulSoup)

## 1. Objective and Summary

The main objective of this project is to implement a functional web scraper to extract structured data from a public web page.

The program is designed to access a book catalog page, simulate a browser (using `requests`), and then parse the HTML and CSS code (using `BeautifulSoup`) to obtain the title, price, and rating of each book. This demonstrates the ability to obtain data from web sources that do not directly offer an API.

**Core Concepts**: HTTP requests, HTML parsing, and the use of CSS selectors for data extraction.

---

## 2. Technologies and Tools Used

This project is based on the integration of Python with specific libraries for web interaction and analysis.

* **Language**: Python 3.x
* **HTTP Requests**: `requests` (To send the GET request and receive the response).
* **HTML Analysis (Parser)**: `BeautifulSoup` (For navigating, searching, and extracting elements from the DOM tree).
* **Localization Technique**: Use of CSS selectors (e.g., `select()`) to accurately identify the HTML elements containing the desired information (titles, prices).

---

## 3. Key Results

The fundamental result is the ability to convert unstructured data (HTML) into structured data (a list of Python dictionaries).

### Extraction Robustness

The scraper demonstrates good extraction practices:

* **HTTP Error Handling**: Uses `respuesta.raise_for_status()` to detect and handle common error codes (`403`, `404`, `500`), preventing silent failures.
* **HTTP Headers**: Includes a custom `User-Agent`, which is essential to avoid being blocked by some websites.
* **Missing Data Handling**: Includes `try/except` blocks or conditional logic to handle cases where an element (such as the rating) might be missing or malformed in a book card, allowing the scraper to continue.

---

## 4. Project Development (Procedure)

The workflow is divided into two main phases, encapsulated in modular functions:

1. **Content Retrieval (`obtener_html`)**:

* The destination URL and headers are configured.
* The `requests.get()` function is called.
* The plain HTML text (`respuesta.text`) is returned.

2. **Data Extraction (`extraer_datos_pagina`)**:
* `BeautifulSoup` is initialized to build the DOM tree.
* The CSS selector (`.product_pod`) is used to identify each book card.
* Within each card, more specific selectors are used to retrieve the title (`a` tag), the price (`.price_color`), and the rating class (`.star-rating`).
* The result is formatted as a Python dictionary.

---

## 5. Repository and File Structure

The project is contained in a single executable code file.

```bash
Programacion_con_Python/
└── Proyecto12_Web_Scraper/
    ├── scraper_libros.py # Request logic and parsing.
    └── README.md # Project documentation.
```

---

## 6. Conclusions

This project demonstrates mastery of:

* **Web Connectivity**: Ability to make HTTP requests to external servers.
* **HTML Processing**: Mastery of the *BeautifulSoup* library for parsing and navigating the DOM (Document Object Model).
* **Structured Extraction**: Ability to use CSS selectors to extract information efficiently and specifically.
* **Ethical and Robustness Considerations**: Use of *User-Agents* and error handling for respectful and stable interaction with the web server.
