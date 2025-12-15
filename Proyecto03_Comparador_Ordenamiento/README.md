# Proyecto N°3: Comparador de Algoritmos de Ordenamiento

## Análisis de Rendimiento $O(N^2)$

## 1\. Objetivo y Resumen

El objetivo principal de este proyecto es **medir y comparar el rendimiento en tiempo real** de algoritmos de ordenamiento de complejidad cuadrática (O(N^2)), como **Bubble Sort** y **Insertion Sort**.

La aplicación genera grandes listas de números aleatorios y cronometra el tiempo exacto que le toma a cada algoritmo ordenar la misma lista, permitiendo al usuario visualizar la diferencia de eficiencia.

**Valor Clave:** Demostrar la implementación correcta de algoritmos de ordenamiento y, crucialmente, la capacidad de realizar **análisis empírico de complejidad temporal**.

-----

## 2\. Tecnologías y Herramientas Utilizadas

Este proyecto utiliza bibliotecas estándar de Python esenciales para la generación de datos aleatorios y la medición del tiempo.

  * **Lenguaje:** Python 3.x
  * **Módulo de Tiempo:** **`time`** (para obtener la hora de inicio y fin y calcular la duración).
  * **Módulo de Datos:** **`random`** (para generar listas de números enteros de forma aleatoria).
  * **Algoritmos Implementados:**
      * `ordenamiento_burbuja` (Bubble Sort)
      * `ordenamiento_insercion` (Insertion Sort)

-----

## 3\. Resultados Clave

El resultado principal del programa es un **Reporte Final de Rendimiento** que lista los tiempos de ejecución para cada algoritmo, ordenados del más rápido al más lento.

### Reporte de Ejemplo

```
--- REPORTE FINAL DE RENDIMIENTO ---
#1: Ordenamiento por Inserción  -> 2.876543 s
#2: Ordenamiento de Burbuja     -> 4.512345 s

Prueba realizada con N = 10000 elementos.
------------------------------------------------
```

  * **Confirmación de $O(N^2)$:** Para grandes valores de $N$ (ej. 10.000 a 20.000), los tiempos de ejecución serán notables (varios segundos), verificando empíricamente que ambos algoritmos pertenecen a la misma clase de complejidad (O(N^2)).
  * **Eficiencia Relativa:** Generalmente, la **Inserción** suele ser ligeramente más rápida que **Burbuja** para listas aleatorias, lo cual se refleja en el reporte.

-----

## 4\. Desarrollo del Proyecto (Procedimiento)

El script sigue una metodología clara de prueba y medición:

1.  **Generación de Datos:** Se utiliza la función `generar_lista_aleatoria(N)` para crear una lista de tamaño $N$ que sirve como caso de prueba.
2.  **Medición Segura:** La función `medir_tiempo` asegura que el algoritmo se ejecute sobre una **copia** de la lista base, garantizando que todos los algoritmos reciban el mismo conjunto de datos inicial (sin ordenar).
3.  **Implementación Pura:** Los algoritmos de ordenamiento están implementados de manera pura (sin usar la función `sort()` de Python) para medir su lógica interna.
4.  **Ejecución de Pruebas:** Se crea un diccionario que mapea nombres de algoritmos a sus funciones, permitiendo ejecutar el proceso de medición de forma dinámica y generar los resultados en una lista de tuplas.

-----

## 5\. Estructura del Repositorio y Archivos

El proyecto se encuentra en un único archivo de código ejecutable:

```
Programacion_con_Python/
└── Proyecto03_Comparador_Ordenamiento/
    ├── comparador_ordenamiento.py  # Script de generación, implementación y medición.
    └── README.md                   # Documentación del proyecto.
```

-----

## 6\. Conclusiones

Este proyecto demuestra un entendimiento profundo de:

  * **Análisis de Algoritmos:** Habilidad para implementar y analizar empíricamente la complejidad temporal, observando cómo los algoritmos $O(N^2)$ se comportan con un conjunto de datos grande.
  * **Estructuras de Datos y Algoritmos:** Implementación funcional de los métodos clásicos de ordenamiento por **Burbuja** e **Inserción**.
  * **Metodología de Pruebas:** Uso del módulo `time` y copias de datos para garantizar pruebas de rendimiento justas y comparables.

-----

# Project N°3: Sorting Algorithm Comparator (Performance Analysis O(N^2))

## 1. Objective and Summary

The main objective of this project is to measure and compare the real-time performance of quadratic complexity (O(N^2)) sorting algorithms, such as Bubble Sort and Insertion Sort.

The application generates large lists of random numbers and times the exact time it takes each algorithm to sort the same list, allowing the user to visualize the difference in efficiency.

**Key Value**: To demonstrate the correct implementation of sorting algorithms and, crucially, the ability to perform empirical analysis of time complexity.

---

## 2. Technologies and Tools Used

This project uses essential standard Python libraries for generating random data and measuring time.

* **Language**: Python 3.x
* **Time Module**: `time` (to obtain the start and end times and calculate the duration).
* **Data Module**: `random` (to generate lists of random integers).
* **Implemented Algorithms**:
* Bubble Sort (`ordenamiento_burbuja`)
* Insertion Sort (`ordenamiento_insercion`)

---

## 3. Key Results

The program's main output is a Final Performance Report (*Reporte Final de Rendimiento*) that lists the execution times for each algorithm, ordered from fastest to slowest.

### Example Report (English translation)

```bash
--- FINAL PERFORMANCE REPORT ---
#1: Insertion Sort -> 2.876543 s
#2: Bubble Sort -> 4.512345 s

Test performed with N = 10000 elements.

------------------------------------------------
```

* **Confirmation of O(N²)**: For large values ​​of N (e.g., 10,000 to 20,000), execution times will be significant (several seconds), empirically verifying that both algorithms belong to the same complexity class (O(N²)).
* **Relative Efficiency**: Generally, Insertion Sort is slightly faster than Bubble Sort for random lists, which is reflected in the report.

---

## 4. Project Development (Procedure)

The script follows a clear testing and measurement methodology:

1. **Data Generation**: The function `generar_lista_aleatoria(N)` is used to create a list of size N, which serves as a test case.
2. **Reliable Measurement**: The function `medir_tiempo` ensures that the algorithm runs on a copy of the base list, guaranteeing that all algorithms receive the same initial (unsorted) dataset.
3. **Pure Implementation**: The sorting algorithms are implemented in a pure form (without using Python's `sort()` function) to measure their internal logic.
4. **Test Execution**: A dictionary is created that maps algorithm names to their functions, allowing the measurement process to be executed dynamically and the results to be generated in a list of tuples.

---

## 5. Repository and File Structure

The project is contained in a single executable code file:

```bash
Programacion_con_Python/
└── Proyecto03_Comparador_Ordenamiento/
    ├── comparador_ordenamiento.py  # Generation, implementation, and measurement script.
    └── README.md   # Project documentation.
```

---

## 6. Conclusions

This project demonstrates a deep understanding of:

* **Algorithm Analysis**: Ability to implement and empirically analyze time complexity, observing how O(N²) algorithms behave with a large dataset.
* **Data Structures and Algorithms**: Functional implementation of classic bubble sort and insertion sort methods.
* **Testing Methodology**: Use of the `time` module and data copies to ensure fair and comparable performance tests.
