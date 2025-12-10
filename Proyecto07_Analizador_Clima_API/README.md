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
  * **Módulo de Peticiones:** **`requests`** (Biblioteca estándar de facto para realizar peticiones HTTP).
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
    ├── reporte_clima.json  # (Generado) Resultado final limpio de la extracción.
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