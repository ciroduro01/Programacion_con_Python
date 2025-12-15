# Proyecto N°10: Consolidación y Limpieza de Reportes CSV

## Automatización de *Data Pipeline* y Transformación de Datos Tabulares

## 1\. Objetivo y Resumen

El objetivo principal de este proyecto es automatizar el proceso de **lectura, limpieza, transformación y consolidación** de múltiples archivos de datos tabulares (CSV) en un único reporte final.

La aplicación demuestra la creación de un flujo de trabajo (data pipeline) que:

1.  Busca automáticamente todos los reportes de ventas en la carpeta fuente.
2.  Procesa cada transacción, asegurando que los campos numéricos sean válidos.
3.  Añade una columna calculada (**`Monto_Total`**).
4.  Consolida toda la información en un solo archivo de salida.

**Concepto Central:** **Manejo profesional de I/O de Archivos CSV** y **Garantía de Integridad de Datos**.

-----

## 2\. Tecnologías y Herramientas Utilizadas

Este proyecto se enfoca en módulos estándar de Python para el manejo de archivos y el sistema operativo.

  * **Lenguaje:** Python 3.x
  * **Módulo de Archivos:** **`csv`** (Uso de `DictReader` y `DictWriter` para un manejo estructurado de los datos).
  * **Módulo del Sistema:**
      * **`glob`**: Para buscar de forma automática todos los archivos CSV dentro de un directorio.
      * **`os`**: Para manejo de rutas de archivos.
  * **Técnica Central:** **Limpieza y Conversión de Tipos de Datos** (casting de `str` a `float`/`int`) con manejo de errores `try/except`.

-----

## 3\. Resultados Clave

El resultado final es el archivo **`reporte_consolidado.csv`**, que combina todas las transacciones individuales y contiene una métrica clave calculada.

### Transformación de Datos

El *script* realiza una **Transformación de Datos** (`T` en ETL) crítica:

  * **Cálculo Derivado:** Por cada fila leída, se calcula y se agrega la columna **`Monto_Total`** utilizando la fórmula: `Monto_Total = Cantidad * Monto_Unitario`.
  * **Homogeneización:** Todos los reportes con diferentes nombres de archivo y periodos se unifican bajo una estructura de encabezados común.
  * **Manejo de Errores:** Las filas con errores de formato (ej. texto donde debería ir un número) son identificadas y saltadas, permitiendo que el proceso continúe sin fallar.

-----

## 4\. Desarrollo del Proyecto (Procedimiento)

El *script* sigue un flujo de trabajo lineal y robusto:

1.  **Descubrimiento Automático:** `glob.glob()` se utiliza para encontrar dinámicamente todos los archivos `.csv` en la carpeta `reportes_ventas`, eliminando la necesidad de listar cada archivo manualmente.
2.  **Lectura por Diccionario (`DictReader`):** Cada archivo se abre, y el `csv.DictReader` permite procesar las filas como diccionarios, lo que hace el código más legible al acceder a los datos por nombre de columna (ej. `fila['Cantidad']`) en lugar de por índice.
3.  **Conversión y Cálculo:** Dentro del bucle de procesamiento, se intenta convertir `Cantidad` y `Monto_Unitario` a tipos numéricos. Si la conversión es exitosa, se calcula el `Monto_Total`. Si falla (ej. `ValueError`), el bloque `try/except` imprime una advertencia y salta la fila.
4.  **Escritura Final (`DictWriter`):** Una vez que todos los datos han sido recolectados y limpiados en una lista, el `csv.DictWriter` escribe el contenido al archivo de salida, garantizando que el orden de las columnas (`COLUMNAS_SALIDA`) sea el deseado.

-----

## 5\. Estructura del Repositorio y Archivos

El proyecto está organizado en una carpeta de entrada y un archivo de salida principal:

```
Programacion_con_Python/
└── Proyecto10_Consolidador_CSV/
    ├── consolidador_csv.py     # Lógica principal del data pipeline.
    ├── reportes_ventas/
    │   ├── sucursal_a_jun.csv  # Datos de entrada 1
    │   ├── sucursal_b_jun.csv  # Datos de entrada 2
    │   └── sucursal_c_jul.csv  # Datos de entrada 3
    ├── reporte_consolidado.csv # (Generado) IGNORADO - Archivo de salida final.
    └── README.md               # Documentación del proyecto.
```

-----

## 6\. Conclusiones

Este proyecto demuestra un dominio avanzado de:

  * **Flujos de Datos (Pipelines):** Habilidad para construir un proceso automatizado desde la ingestión hasta la exportación de datos.
  * **Manejo de Archivos CSV:** Uso de las herramientas `csv` (DictReader/DictWriter) de manera eficiente para el trabajo estructurado con datos tabulares.
  * **Transformación de Datos:** Capacidad para generar nuevas métricas (`Monto_Total`) a partir de datos crudos.
  * **Programación Robusta:** Implementación de bloques de control de errores (`try/except`) para asegurar que el *pipeline* no falle ante datos sucios o mal formados.

-----

# Project N°10: CSV Report Consolidation and Cleaning (Data Pipeline Automation and Tabular Data Transformation)

## 1. Objective and Summary

The main objective of this project is to automate the process of reading, cleaning, transforming, and consolidating multiple tabular data files (CSV) into a single final report.

The application demonstrates the creation of a data pipeline that:

1. Automatically searches for all sales reports in the source folder.
2. Processes each transaction, ensuring that the numeric fields are valid.
3. Adds a calculated column (`Monto_Total` or *Total_Amount*).
4. Consolidates all the information into a single output file.

**Core Concept**: Professional CSV File I/O Management and Data Integrity Assurance.

---

## 2. Technologies and Tools Used

This project focuses on standard Python modules for file handling and operating system integration.

* **Language**: Python 3.x
* **File Module**: CSV (Using `DictReader` and `DictWriter` for structured data handling).
* **System Module**:
* `glob`: To automatically search for all CSV files within a directory.
* `os`: For file path management.
* **Core Technique**: Data Type Cleaning and Conversion (casting from `str` to `float/int`) with `try/except` error handling.

---

## 3. Key Results

The final result is the `reporte_consolidado.csv` file, which combines all individual transactions and contains a calculated key metric.

### Data Transformation
The script performs a critical Data Transformation (T in ETL):

* **Derived Calculation**: For each row read, the Total_Amount (`Monto_Total`) column is calculated and added using the formula: Total_Amount = Quantity * Unit_Amount (`Monto_Total = Cantidad * Monto_Unitario`).
* **Homogenization**: All reports with different file names and time periods are unified under a common header structure.
* **Error Handling**: Rows with formatting errors (e.g., text where a number should be) are identified and skipped, allowing the process to continue without failure.

---

## 4. Project Development (Procedure)
The script follows a linear and robust workflow:

1. **Automatic Discovery**: `glob.glob()` is used to dynamically find all `.csv` files in the sales_reports (`reportes_ventas`) folder, eliminating the need to list each file manually.
2. **Dictionary Reading (`DictReader`)**: Each file is opened, and `csv.DictReader` allows the rows to be processed as dictionaries, making the code more readable by accessing data by column name (e.g., `row['Quantity']` or `fila['Cantidad']`) instead of by index.
3. **Conversion and Calculation**: Within the processing loop, `Quantity` (or `Cantidad`) and `Unit_Price` (or `Monto_Unitario`) are converted to numeric types. If the conversion is successful, the Total_Amount (`Monto_Total`) is calculated. If it fails (e.g., `ValueError`), the `try/except` block prints a warning and skips the row.
4- **Final Writing (DictWriter)**: Once all the data has been collected and cleaned into a list, the `csv.DictWriter` writes the content to the output file, ensuring that the column order (OUTPUT_COLUMNS or `COLUMNAS_SALIDA`) is as desired.

---

## 5. Repository and File Structure

The project is organized into an input folder and a main output file:

```bash
Programacion_con_Python/
└── Proyecto10_Consolidador_CSV/

    ├── consolidador_csv.py  # Main logic of the data pipeline.
    ├── reportes_ventas/
    │   ├── sucursal_a_jun.csv# Input data 1
    │   ├── sucursal_b_jun.csv # Input data 2
    │   └── sucursal_c_jul.csv   # Input data 3
    ├── reporte_consolidado.csv # (Generated) IGNORED - Final output file.
    └── README.md             # Project documentation.
```

---

## 6. Conclusions

This project demonstrates an advanced mastery of:

* **Data Pipelines**: The ability to build an automated process from data ingestion to data export.
* **CSV File Handling**: Efficient use of CSV tools (DictReader/DictWriter) for structured work with tabular data.
* **Data Transformation**: Ability to generate new metrics (Total_Amount or *Monto_Total*) from raw data.
* **Robust Programming**: Implementation of error-handling blocks (try/except) to ensure the pipeline does not fail due to corrupted or malformed data.
