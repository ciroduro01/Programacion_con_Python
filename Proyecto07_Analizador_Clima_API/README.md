# Proyecto N°7: Analizador de Datos de Clima

## Interacción con API REST, Peticiones HTTP y Procesamiento JSON

## 1\. Objetivo y Resumen

El objetivo principal de este proyecto es demostrar la capacidad de interactuar con servicios web externos utilizando el protocolo **HTTP** para consumir datos de una **API REST**.

La aplicación consulta la **API de OpenWeatherMap** para obtener el estado del clima en varias ciudades del mundo. Luego, **procesa el complejo formato JSON** que la API retorna y exporta solo la información relevante (temperatura, humedad, viento) a un archivo `reporte_clima.json` limpio y estructurado.

**Conceptos Centrales:** **Peticiones HTTP (GET)**, manejo de bibliotecas de terceros (`requests`), **deserialización** y **serialización** de datos JSON.

-----

## 2\. Tecnologías y Herramientas Utilizadas

Este proyecto se basa en el manejo de bibliotecas especializadas para la comunicación y el manejo de datos.

  * **Lenguaje:** Python 3.x
  * **Módulo de Peticiones:** **`requests`** (Biblioteca estándar para realizar peticiones HTTP).
  * **Módulo de Datos:** **`json`** (Biblioteca estándar para trabajar con la notación JSON).
  * **API Externa:** **OpenWeatherMap API** (para obtener datos meteorológicos).
  * **Diseño:** **Programación Orientada a Objetos (POO)**. La clase `ClimaAnalyzer` gestiona la conexión, la lógica de *fetching* y el procesamiento.

-----

## 3\. Resultados Clave

El resultado principal es la generación de un archivo `reporte_clima.json` limpio y listo para el análisis, así como el manejo robusto de posibles fallos.

### Robustez y Manejo de Errores

El proyecto demuestra la capacidad de manejar errores comunes en la interacción con APIs:

  * **Configuración:** Verifica la existencia y validez de la `API_KEY` en `config.py`.
  * **Errores HTTP (4xx/5xx):** La función `fetch_data` utiliza `respuesta.raise_for_status()` para detectar fallos como el error **404 Not Found** (por ejemplo, si se busca una ciudad no reconocida).
  * **Estructura JSON:** Utiliza bloques `try/except KeyError` para capturar errores si la estructura del JSON devuelto por la API cambia o es inesperada, evitando que el programa falle por completo.

-----

## 4\. Desarrollo del Proyecto (Procedimiento)

El flujo de trabajo está diseñado para ser secuencial y modular:

1.  **Configuración de Clave:** El script lee la `API_KEY` de un archivo `config.py` separado, una buena práctica para la gestión de credenciales sensibles.
2.  **Petición GET:** La instancia de `ClimaAnalyzer` construye la URL con los parámetros necesarios (ciudad, clave, unidades métricas).
3.  **Procesamiento de Respuesta:** Después de recibir una respuesta exitosa, la función `procesar_json` extrae selectivamente los campos de interés (ej. `main['temp']`, `wind['speed']`, `weather[0]['description']`) y los reformatea en un nuevo diccionario.
4.  **Exportación Final:** El método `exportar_a_json` serializa la lista de diccionarios limpios al archivo final, utilizando `json.dump` con formato legible (`indent=4`).

-----

## 5\. Estructura del Repositorio y Archivos

El proyecto consta de tres archivos:

```
Programacion_con_Python/
└── Proyecto07_Analizador_Clima_API/
    ├── clima_analyzer.py   # Lógica principal de conexión y procesamiento.
    ├── config.py           # (Ignorado por .gitignore) Contiene la API_KEY secreta.
    ├── reporte_clima.json  # (Generado) IGNORADO - Resultado final limpio de la extracción.
    └── README.md           # Documentación del proyecto.
```

-----

## 6\. Conclusiones

Este proyecto demuestra un dominio de:

  * **Consumo de API:** Capacidad para obtener datos de fuentes externas a través de HTTP.
  * **Manejo de JSON:** Habilidad para trabajar con el formato de datos estándar de la web (deserialización y serialización).
  * **Gestión de Credenciales:** Uso del patrón de archivo de configuración (`config.py`) para manejar de forma segura información sensible (APIs, tokens).
  * **Programación Robusta:** Implementación de lógica de manejo de errores para peticiones de red y estructuras de datos inesperadas.

-----

# Project N°7: Weather Data Analyzer (REST API Interaction, HTTP Requests, and JSON Processing)

## 1. Objective and Summary

The main objective of this project is to demonstrate the ability to interact with external web services using the HTTP protocol to consume data from a REST API.

The application queries the **OpenWeatherMap API** to obtain weather conditions in various cities around the world. It then processes the complex JSON format returned by the API and exports only the relevant information (temperature, humidity, wind) to a clean and structured `report_clima.json` file.

**Core Concepts**: HTTP (GET) requests, handling third-party libraries (requests), and JSON data deserialization and serialization.

---

## 2. Technologies and Tools Used

This project is based on the use of specialized libraries for communication and data handling.

* **Language**: Python 3.x
* **Request Module**: `requests` (Standard library for making HTTP requests).
* **Data Module**: `json` (Standard library for working with JSON notation).
* **External API**: OpenWeatherMap API (for obtaining weather data).
* **Design**: Object-Oriented Programming (OOP). The `ClimaAnalyzer` class manages the connection, fetching logic, and processing.

---

## 3. Key Results

The main result is the generation of a clean `reporte_clima.json` file ready for analysis, as well as robust handling of potential errors.

### Robustness and Error Handling

The project demonstrates the ability to handle common errors in API interaction:

* **Configuration**: Verifies the existence and validity of the `API_KEY` in `config.py`.
* **HTTP Errors (4xx/5xx)**: The `fetch_data` function uses `respuesta.raise_for_status()` to detect errors such as `404 Not Found` (for example, when searching for an unrecognized city). 
* **JSON Structure**: Uses `try/except KeyError` blocks to catch errors if the structure of the JSON returned by the API changes or is unexpected, preventing the program from crashing completely.

---

## 4. Project Development (Procedure)

The workflow is designed to be sequential and modular:

1. **Key Configuration**: The script reads the `API_KEY` from a separate `config.py` file, a best practice for handling sensitive credentials.
2. **GET Request**: The `ClimaAnalyzer` instance constructs the URL with the necessary parameters (city, key, metric units).
3. **Response Processing**: After receiving a successful response, the `procesar_json` function selectively extracts the fields of interest (e.g., `main['temp']`, `wind['speed']`, `weather[0]['description']`) and reformats them into a new dictionary.
4. **Final Export**: The `exportar_a_json` method serializes the list of clean dictionaries to the final file, using `json.dump` with a human-readable format (`indent=4`).

---

## 5. Repository and File Structure

The project consists of three files:

```bash
Programacion_con_Python/
└── Proyecto07_Analizador_Clima_API/
    ├── clima_analyzer.py  # Main connection and processing logic.
    ├── config.py # (Ignored by .gitignore) Contains the secret API_KEY.
    ├── reporte_clima.json  # (Generated) IGNORED - Clean final result of the extraction.
    └── README.md            # Project documentation.
```

---

## 6. Conclusions

This project demonstrates mastery of:

* **API Consumption**: Ability to obtain data from external sources via HTTP.
* **JSON Handling**: Ability to work with the standard web data format (deserialization and serialization).
* **Credential Management**: Using the configuration file pattern (`config.py`) to securely handle sensitive information (APIs, tokens).
* **Robust Programming**: Implementing error-handling logic for unexpected network requests and data structures.
