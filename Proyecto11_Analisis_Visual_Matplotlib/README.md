# Proyecto N°11: Análisis Visual de Datos de Ventas

## Visualización de Datos con la Biblioteca Matplotlib

## 1\. Objetivo y Resumen

El objetivo de este proyecto es tomar conjuntos de datos y transformarlos en **representaciones visuales** claras y efectivas. El proyecto se centra en la implementación y personalización de gráficos utilizando la biblioteca **Matplotlib**, el estándar de facto en Python para la creación de gráficos estáticos.

La aplicación genera dos tipos de gráficos comunes en el análisis de ventas:

1.  **Gráfico de Barras:** Para comparar las ventas totales de diferentes sucursales.
2.  **Gráfico Circular (*Pie Chart*):** Para mostrar la distribución porcentual de los productos vendidos.

**Concepto Central:** **Visualización de Datos** para la interpretación y comunicación de métricas de negocio.

-----

## 2\. Tecnologías y Herramientas Utilizadas

Este proyecto se basa en el ecosistema de Data Science de Python.

  * **Lenguaje:** Python 3.x
  * **Librería Principal:** **Matplotlib** (Específicamente el módulo `matplotlib.pyplot` como `plt`).
  * **Módulo de Utilidad:** **`collections.Counter`** (Para calcular rápidamente las frecuencias de los productos en la simulación de datos).
  * **Técnicas Clave:**
      * **Programación Orientada a Funciones:** El código está modularizado con funciones específicas (`generar_grafico_barras`, `generar_grafico_circular`) para cada tipo de gráfico.
      * **Personalización:** Uso de parámetros como `figsize`, `plt.title`, `plt.xlabel`, `plt.ylabel`, y `autopct` para dar un acabado profesional a los gráficos.

-----

## 3\. Resultados Clave

El resultado del proyecto son dos gráficos exportados que permiten una rápida comprensión de las tendencias de ventas.

### Gráfico 1: Ventas por Sucursal (Barras)

  * **Propósito:** Comparación de magnitudes.
  * **Funcionalidad Destacada:** Demuestra el uso de `plt.bar()` y la adición de etiquetas de datos (`plt.text`) directamente sobre cada barra para una lectura precisa.
    ![Gráfico de Barras de Ventas por Sucursal](assets/Ventas_Totales_por_Sucursal.jpg)

### Gráfico 2: Distribución de Productos (Circular)

  * **Propósito:** Mostrar proporciones de un total.
  * **Funcionalidad Destacada:** Demuestra el uso de la función `autopct='%1.1f%%'` para mostrar los porcentajes dentro de las "rebanadas" y el parámetro `explode` para resaltar el producto más vendido, mejorando el impacto visual.
    ![Gráfico Circular de Distribución de Productos](assets/Participación_Porcentual_por_Producto.jpg)

-----

## 4\. Desarrollo del Proyecto (Procedimiento)

El flujo de trabajo se centra en la preparación de datos y el llamado a las funciones de `matplotlib`.

1.  **Simulación de Datos:** En ausencia de un archivo de datos real, se utilizan `random` y `collections.Counter` para generar dos conjuntos de datos que imiten los resultados de un análisis de ventas.
2.  **Función `generar_grafico_barras`:**
      * Llama a `plt.bar()` con las etiquetas de las sucursales y sus valores de ventas.
      * Añade `plt.xlabel` y `plt.ylabel` para asegurar que el gráfico sea autoexplicativo.
3.  **Función `generar_grafico_circular`:**
      * Convierte el `Counter` de productos en listas separadas para etiquetas y tamaños.
      * Calcula el índice del producto más vendido para aplicar el efecto `explode`.
      * Llama a `plt.pie()` utilizando el formato de porcentaje y la personalización de colores/sombras.
4.  **Ejecución:** La función `main()` orquesta las llamadas y finalmente utiliza `plt.show()` para renderizar y mostrar ambos gráficos al usuario.

-----

## 5\. Estructura del Repositorio y Archivos

```
Programacion_con_Python/
└── Proyecto11_Analisis_Visual_Matplotlib/
    ├── analisis_ventas_matplotlib.py  # Implementación de las funciones de graficación.
    ├── assets/
    │   ├── Ventas_Totales_por_Sucursal.png        # Gráfico de barras generado.
    │   └── Participación_Porcentual_por_Producto.png      # Gráfico circular generado.
    └── README.md                     # Documentación del proyecto.
```

-----

## 6\. Conclusiones

Este proyecto demuestra un dominio de:

  * **Visualización de Datos:** Capacidad para seleccionar y generar gráficos adecuados (Barras vs. Circular) según el tipo de pregunta de negocio.
  * **Uso de Matplotlib:** Dominio de las funciones básicas de `pyplot` para la creación y la personalización de gráficos.
  * **Comunicación de Datos:** Habilidad para añadir títulos, etiquetas y *key highlights* (como `explode`) para hacer que los datos sean más accesibles y procesables.
  * **Manipulación de Datos:** Uso de herramientas de utilidad (`Counter`) para preparar los datos para la visualización.

-----

# Project N°11: Visual Analysis of Sales Data (Data Visualization with the Matplotlib Library)

## 1. Objective and Summary

The objective of this project is to take datasets and transform them into clear and effective visual representations. The project focuses on the implementation and customization of charts using the Matplotlib library, the standard in Python for creating static charts.

The application generates two common chart types used in sales analysis:

1. **Bar Chart**: To compare total sales across different branches.
2. **Pie Chart**: To show the percentage distribution of products sold.

**Core Concept**: Data visualization for the interpretation and communication of business metrics.

---

## 2. Technologies and Tools Used

This project is based on the Python Data Science ecosystem.

* **Language**: Python 3.x
* **Main Library**: Matplotlib (Specifically the `matplotlib.pyplot` module as `plt`).
* **Utility Module**: `collections.Counter` (For quickly calculating product frequencies in the data simulation).
* **Key Techniques**:
* **Function-Oriented Programming**: The code is modularized with specific functions (`generar_grafico_barras`, `generar_grafico_circular`) for each chart type.
* **Customization**: Use of parameters such as `figsize`, `plt.title`, `plt.xlabel`, `plt.ylabel`, and `autopct` to give the charts a professional finish.

---

## 3. Key Results

The project results in two exported charts that allow for a quick understanding of sales trends.

### Chart 1: Sales by Branch (Bar Chart)
* **Purpose**: Comparison of magnitudes.
* **Key Feature**: Demonstrates the use of `plt.bar()` and the addition of data labels (`plt.text`) directly above each bar for accurate reading.
    ![Sales by Branch bar chart](assets/Ventas_Totales_por_Sucursal.jpg)

### Chart 2: Product Distribution (Pie Chart)
* **Purpose**: To show proportions of a total.
* **Key Feature**: Demonstrates the use of the `autopct='%1.1f%%'` function to display percentages within the "slices" and the `explode` parameter to highlight the top-selling product, enhancing visual impact.
    ![Product Distribution Pie Chart](assets/Participación_Porcentual_por_Producto.jpg)

---

## 4. Project Development (Procedure)

The workflow focuses on data preparation and calling `matplotlib` functions.

1. **Data Simulation**: In the absence of a real data file, `random` and `collections.Counter` are used to generate two datasets that mimic the results of a sales analysis.
2. `generar_grafico_barras` Function:
* calls `plt.bar()` with the branch labels and their sales values.
* adds `plt.xlabel` and `plt.ylabel` to ensure the chart is self-explanatory.
3. `generar_grafico_circular` Function:
* converts the product `Counter` into separate lists for labels and sizes.
* calculates the best-selling product index to apply the `explode` effect.
* calls `plt.pie()` using the percentage format and custom colors/shades.
4. **Execution**: The `main()` function orchestrates the calls and finally uses `plt.show()` to render and display both graphs to the user.

---

## 5. Repository and File Structure

```bash
Programacion_con_Python/
└── Proyecto11_Analisis_Visual_Matplotlib/
    ├── analisis_ventas_matplotlib.py  # Implementation of the plotting functions.
    ├── assets/
    │   ├── Ventas_Totales_por_Sucursal.png      # Generated bar chart.
    │   └── Participación_Porcentual_por_Producto.png  # Generated pie chart.
    └── README.md                    # Project documentation.
```

---

## 6. Conclusions

This project demonstrates mastery of:

* **Data Visualization**: Ability to select and generate appropriate charts (Bar vs. Pie) based on the type of business question.
* **Use of Matplotlib**: Mastery of basic `pyplot` functions for creating and customizing charts.
* **Data Communication**: Ability to add titles, labels, and key highlights (such as `explode`) to make data more accessible and actionable.
* **Data Manipulation**: Use of utility tools (`Counter`) to prepare data for visualization.
