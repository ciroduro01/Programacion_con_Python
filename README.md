# Portafolio de Proyectos: "Programación con Python" 

## Resumen Ejecutivo
Este portafolio de 15 proyectos demuestra un dominio integral del desarrollo en Python, desde la eficiencia algorítmica y los fundamentos de la Programación Orientada a Objetos (OOP) hasta la construcción de aplicaciones **Full-Stack** y *pipelines* de datos automatizados. Cada proyecto está diseñado para construir un seguimiento de diversas herramientas de Python que culmina en el desarrollo de sistemas de producción, como una API RESTful con **Flask** y un blog profesional con el *framework* **Django**.

---

## 1. Fundamentos y Estructuras de Datos

**Foco:** Refuerzo de la lógica de programación, patrones de diseño (OOP, Recursividad) y selección de estructuras de datos eficientes.

| Proyecto | Concepto Central | Habilidades Clave |
| --- | --- | --- |
| **P1** Analizador de Palabras | Análisis de Texto / Estructuras Avanzadas | Uso eficiente de `collections.Counter`. |
| **P4** Simulador Bancario | Programación Orientada a Objetos (OOP) | **Encapsulación** y **Composición** de Clases (`Cliente` tiene una `Cuenta`) . |
| **P5** Explorador de Directorios | Aplicación de **Recursividad** | Recorrido eficiente de estructuras jerárquicas (Árboles). |
| **P3** Comparador de Ordenamiento O(N^2) | Análisis de Complejidad | Implementación y medición empírica de Bubble/Insertion Sort. |
| **P8** Análisis de Merge Sort O(N log N) | Patrón **Divide y Conquistar** | Prueba de la eficiencia de O(N log N) con grandes volúmenes de datos. |

---

## 2. Persistencia y Arquitectura de Datos

**Foco:** Dominio de diferentes capas de persistencia, desde archivos locales hasta Bases de Datos Relacionales (SQL) y la abstracción con ORMs.

| Proyecto | Concepto Central | Habilidades Clave |
| --- | --- | --- |
| **P2** Gestor de Librería | Persistencia de Datos con **JSON** | Serialización/Deserialización y simulación de Clave Primaria (ISBN). |
| **P6** Gestor de Tareas | **CRUD** con **SQLite** Manual | Ejecución de sentencias SQL (`INSERT`, `SELECT`, etc.) y manejo seguro de transacciones (`sqlite3`). |
| **P9** Inventario con **SQLAlchemy** | **Mapeo Objeto-Relacional (ORM)** | Abstracción de SQL mediante la manipulación de objetos de Python. |

---

## 3. Procesamiento, Automatización y Análisis

**Foco:** Construcción de flujos de trabajo (*pipelines*) para la ingesta, limpieza, análisis y comunicación de datos.

| Proyecto | Concepto Central | Habilidades Clave |
| --- | --- | --- |
| **P10** Consolidador CSV | **Data Pipeline** (ETL) | Automatización, limpieza de datos, y manejo profesional de `csv.DictReader`. |
| **P11** Análisis Visual | **Visualización** con Matplotlib | Generación de gráficos (Barras, Circular) y comunicación de métricas. |
| **P7** Analizador de Clima | Consumo de **API REST** | Peticiones **HTTP** con `requests` y gestión segura de `API_KEY`. |
| **P12** Web Scraper | Extracción de Datos de HTML | Uso de **`BeautifulSoup`** y **Selectores CSS** para *parsing*. |
| **P14** Reporte Automático | Automatización de **Comunicaciones** | Uso de protocolo **SMTP** con cifrado TLS/SSL para envío de reportes HTML. |

---

## 4. Desarrollo Web y Arquitectura Backend

**Foco:** Diseño y construcción de sistemas de servidor, aplicando los conocimientos de OOP y Bases de Datos en un entorno web.

| Proyecto | Concepto Central | Habilidades Clave |
| --- | --- | --- |
| **P13** API REST con **Flask** | Construcción de **Backend** CRUD | Implementación de *endpoints* REST con **Flask** e integración con **Flask-SQLAlchemy**. |
| **P15** Blog Profesional con **Django** | Aplicación **Full-Stack** | Dominio del patrón **MVT** (Model-View-Template) y la estructura de proyectos de gran escala. |

---

## Para utilizar este repositorio...

Para ejecutar los proyectos en este repositorio, se recomienda utilizar un entorno virtual para gestionar las dependencias de manera aislada.

### Requisitos

* Python 3.8+
* Git (para clonar el repositorio)

### Pasos de Configuración

1. **Clonar el Repositorio**

```bash
git clone https://github.com/ciroduro01/Programacion_con_Python
cd Programacion_con_Python

```

2. **Crear y Activar un Entorno Virtual (Recomendado)**
```bash
# Crear el entorno virtual
python -m venv venv

# Activar en Windows
.\venv\Scripts\activate

# Activar en macOS/Linux
source venv/bin/activate

```

3. **Instalar Dependencias**

Cada proyecto web o de análisis (P7, P9, P11, P12, P13, P15) requiere librerías de terceros (ej. `requests`, `SQLAlchemy`, `Flask`, `Django`).

**Instrucción:** Navega a la carpeta del proyecto que deseas ejecutar (ej. `Proyecto13_API_REST_Flask`) y consulta el `README.md` específico para la lista de dependencias que debes instalar manualmente vía `pip install`.

4. **Ejecutar el Proyecto**
La mayoría de los proyectos se ejecutan con:
```bash
python nombre_del_script.py

```

---

## Licencia

Este proyecto está bajo la Licencia **MIT**.

Eres libre de modificar, distribuir y usar el código para fines personales y comerciales, siempre y cuando se incluya la nota de copyright original.

[Ver Licencia](LICENSE)

---

# "Programming with Python" Projects Portfolio

## Repository Overview
This portfolio of 15 projects demonstrates a comprehensive mastery of Python development, from algorithmic efficiency and the fundamentals of Object-Oriented Programming (OOP) to building **full-stack applications** and automated data **pipelines**. Each project is designed to build a track record of various Python tools, culminating in the development of production systems, such as a RESTful API with **Flask** and a professional blog with the **Django** framework.

---

## 1. Fundamentals and Data Structures

**Focus:** Reinforcing programming logic, design patterns (OOP, Recursion), and selecting efficient data structures.

| Project | Core Concept | Key Skills |
| --- | --- | --- |
| **P1** Word Analyzer | Text Analysis / Advanced Structures | Efficient use of `collections.Counter` |
| **P4** Banking Simulator | Object-Oriented Programming (OOP) | **Encapsulation** and **Class** Composition (`Cliente` has a `Cuenta`). |
| **P5** Directory Explorer | Use of **Recursion**. | Efficient traversal of hierarchical structures (trees). |
| **P3** Sort Comparator O(N^2) | Complex Analysis. | Implementation and empirical measurement of Bubble/Insertion Sort. |
| **P8** Merge Sort Analysis O(N log N) | **Divide** and **Conquer** Pattern. | Testing the efficiency of O(N log N) with large volumes of data. |

---

## 2. Persistence and Data Architecture

**Focus**: Mastery of different persistence layers, from local files to Relational Databases (SQL) and abstraction with ORMs.

| Project | Core Concept | Key Skills |
| --- | --- | --- |
| **P2** Library Manager | Data persistence with **JSON**. | Serialization/Deserialization and Primary Key (ISBN) simulation. |
| **P6** Task Manager | **CRUD** with **SQLite** | Execution of SQL statements (`INSERT`, `SELECT`, etc.) and secure transaction management (`sqlite3`). |
| **P9** Inventory with **SQLAlchemy** | **Object-Relational Mapping (ORM)** | Abstraction of SQL through Python object manipulation. |

---

## 3. Processing, Automation, and Analysis

**Focus**: Building workflows (*pipelines*) for data ingestion, cleaning, analysis, and communication.

| Project | Core Concept | Key Skills |
| --- | --- | --- |
| **P10** CSV Consolidator | **Data Pipeline** (ETL) | Automation, data cleaning, and professional handling of `csv.DictReader`. |
| **P11** Visual Analysis | **Visualization** with Matplotlib | Generation of charts (bar, pie) and communication of metrics. |
| **P7** Weather Analyzer | **API REST** consumption | **HTTP** and using `requests` with secure `API_KEY` management. |
| **P12** Web Scraper | Extraction of HTML data | Use of `BeautifulSoup` and **CSS selectors** for parsing. |
| **P14** Automatic Report | Automation of Communications. | Use of **SMTP** protocol with TLS/SSL encryption for sending HTML reports. |

---

## 4. Web Development and Backend Architecture

**Focus**: Design and construction of server systems, applying OOP and Database knowledge in a web environment.

| Project | Core Concept | Key Skills |
| --- | --- | --- |
| **P13** REST API with **Flask** | CRUD Backend Construction | Implementation of REST endpoints with **Flask** and integration with **Flask-SQLAlchemy**. |
| **P15** Professional Blog with **Django** | Full-Stack Application | Mastery of the **MVT** (Model-View-Template) pattern and large-scale project structure. |

---

## To use this repository...

To run projects in this repository, it is recommended to use a virtual environment to manage dependencies in isolation.

### Requirements

* Python 3.8+
* Git (to clone the repository)

### Setup Steps

1. Clone the Repository

```bash
git clone https://github.com/ciroduro01/Programacion_con_Python
cd Programacion_con_Python

```

2. **Create and Activate a Virtual Environment (Recommended)**
```bash
# Create the virtual environment
python -m venv venv

# Activate on Windows
.\venv\Scripts\activate

# Activate on macOS/Linux
source venv/bin/activate

```

3. **Install Dependencies**
Each web or analytics project (P7, P9, P11, P12, P13, P15) requires third-party libraries (e.g., `requests`, `SQLAlchemy`, `Flask`, `Django`).

**Instructions**: Navigate to the project folder you want to run (e.g., `Proyecto13_API_REST_Flask`) and consult the specific README.md file for the list of dependencies you must manually install using `pip install`.

4. **Running the Project**
Most projects are run with:
```bash
python script_name.py

```

---

## License

This project is licensed under the **MIT** License.

You are free to modify, distribute, and use the code for personal and commercial purposes, provided you include the original copyright notice.

[Read License](LICENSE)

---
