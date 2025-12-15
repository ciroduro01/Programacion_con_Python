# Proyecto N°8: Análisis de Merge Sort

## Demostración y Comparativa de Algoritmos O(N log N)

## 1\. Objetivo y Resumen

El objetivo principal de este proyecto es implementar y demostrar el algoritmo de ordenamiento **Merge Sort** y realizar una **comparativa de rendimiento** directa contra un algoritmo cuadrático, como **Bubble Sort**.

El proyecto genera conjuntos de datos de tamaño creciente (hasta N=20.000) y cronometra el tiempo de ejecución de ambos. Esto sirve para **verificar empíricamente** la gran diferencia de eficiencia entre las complejidades O(N log N) (Merge Sort) y O(N^2) (Bubble Sort) a medida que el conjunto de datos se hace grande.

**Concepto Central:** Implementación del patrón **"Divide y Conquistar"** y el **análisis asintótico de complejidad**.

-----

## 2\. Tecnologías y Herramientas Utilizadas

Este proyecto se enfoca en la implementación del algoritmo y el módulo estándar para medición de tiempo.

  * **Lenguaje:** Python 3.x
  * **Módulo de Tiempo:** **`time.perf_counter()`** (Para mediciones de alta precisión).
  * **Algoritmos Implementados:**
      * `merge_sort` (Divide y Conquistar: O(N log N))
      * `bubble_sort` (Solo para fines de comparación: O(N^2))
  * **Técnica Central:** **Recursividad** para la fase de división del Merge Sort.

-----

## 3\. Resultados Clave

El resultado fundamental del programa es una tabla que muestra la diferencia dramática en los tiempos de ejecución, especialmente con tamaños de lista **N** grandes.

### Tabla de Rendimiento

| Tamaño (N) | Merge Sort **(O(N log N))** | Bubble Sort **(O(N^2))** |
| :--- | :--- | :--- |
| **1,000** | ~ 0.005 s | ~ 0.200 s |
| **5,000** | ~ 0.025 s | ~ 4.500 s |
| **20,000** | ~ 0.120 s | **MUY LENTO** |

  * **Conclusión Asintótica:** Mientras que el tiempo de Merge Sort crece linealmente con **N**, el tiempo de Bubble Sort se dispara (cuadráticamente). Con N=20.000, el Bubble Sort es tan lento que el código opta por no ejecutarlo, destacando su ineficiencia.

-----

## 4\. Desarrollo del Proyecto (Procedimiento)

El Merge Sort se implementa mediante dos funciones:

1.  **`merge_sort(lista)` (Divide):** Esta es la función recursiva. Si la lista es mayor a 1, la divide en dos mitades (`izquierda` y `derecha`) y se llama a sí misma recursivamente para ordenar esas mitades.
2.  **`merge(izquierda, derecha)` (Conquistar):** Esta función auxiliar es la que realiza el trabajo de combinar dos listas ya ordenadas en una única lista ordenada, de manera eficiente (O(N)).

**El Proceso de Comparación:**

1.  Se define una lista de **tamaños de prueba** (`tamanos`).
2.  Dentro del bucle de prueba, se crea una copia de la lista aleatoria original (`datos[:]`) para cada algoritmo, asegurando que ambos trabajen sobre datos idénticos y sin ordenar.
3.  La función `cronometrar` envuelve la ejecución para capturar el tiempo.

-----

## 5\. Estructura del Repositorio y Archivos

El proyecto se encuentra en un único archivo de código ejecutable.

```
Programacion_con_Python/
└── Proyecto08_Analisis_Merge_Sort/
    ├── analisis_merge_sort.py  # Implementación de los algoritmos y la lógica de benchmarking.
    └── README.md                 # Documentación del proyecto.
```

-----

## 6\. Conclusiones

Este proyecto demuestra un dominio de:

  * **Algoritmos de Ordenamiento Avanzados:** Implementación funcional del complejo algoritmo Merge Sort.
  * **Divide y Conquistar:** Aplicación exitosa de este patrón de diseño algorítmico.
  * **Análisis de Complejidad:** Habilidad para usar módulos de *timing* para **medir empíricamente** la eficiencia teórica de **O(N log N)** frente a **O(N^2)**.
  * **Recursividad:** Uso de la recursividad para la división de la lista.

-----

# Project N°8: Merge Sort Analysis (Demonstration and Comparison of O(N log N) Algorithms)

## 1. Objective and Summary

The main objective of this project is to implement and demonstrate the **Merge Sort** sorting algorithm and perform a direct performance comparison against a quadratic algorithm, such as **Bubble Sort**.

The project generates increasingly large datasets (up to N=20,000) and times the execution time of both. This serves to empirically verify the significant difference in efficiency between the complexities of O(N log N) (Merge Sort) and O(N^2) (Bubble Sort) as the dataset grows larger.

**Central Concept**: Implementation of the "Divide and Conquer" pattern and asymptotic complexity analysis.

---

## 2. Technologies and Tools Used

This project focuses on the implementation of the algorithm and the standard module for time measurement.

* **Language**: Python 3.x
* **Time Module**: `time.perf_counter()` (For high-precision measurements).
* **Implemented Algorithms**:
* `merge_sort` (Divide and Conquer: O(N log N))
* `bubble_sort` (For comparison purposes only: O(N^2))
* **Core Technique**: Recursion for the division phase of Merge Sort.

---

## 3. Key Results

The program's fundamental result is a table showing the dramatic difference in execution times, especially with large list sizes N.

### Performance Table

| Size (N) | Merge Sort (O(N log N)) | Bubble Sort (O(N^2)) |
| :--- | :--- | :--- |
| 1,000 | ~ 0.005 s | ~ 0.200 s |
| 5,000 | ~ 0.025 s | ~ 4.500 s |
| 20,000 | ~ 0.120 s | VERY SLOW |

* **Asymptotic Conclusion**: While the Merge Sort time increases linearly with N, the Bubble Sort time increases exponentially (quadratically). With N=20,000, the Bubble Sort is so slow that the code chooses not to execute it, highlighting its inefficiency.

---

## 4. Project Development (Procedure)

The Merge Sort is implemented using two functions:

1. **`merge_sort(lista)` (Divide)**: This is the recursive function. If the list is greater than 1, it splits it into two halves (left and right) and calls itself recursively to sort those halves.
2. **`merge(izquierda, derecha)` (Conquer)**: This helper function efficiently (O(N)) combines two already sorted lists into a single sorted list.

**The Comparison Process**:

1. A list of test sizes (`tamanos`) is defined.
2. Inside the test loop, a copy of the original random list (`datos[:]`) is created for each algorithm, ensuring that both work on identical, unsorted data.
3. The `cronometrar` function wraps the execution to capture the time.

---

## 5. Repository and File Structure

The project is contained in a single executable code file.

```bash
Programacion_con_Python/
└── Proyecto08_Analisis_Merge_Sort/
    ├── analisis_merge_sort.py  # Implementation of the algorithms and benchmarking logic.
    └── README.md               # Project documentation.
```

---

## 6. Conclusions

This project demonstrates mastery of:

* **Advanced Sorting Algorithms**: Functional implementation of the complex Merge Sort algorithm.
* **Divide and Conquer**: Successful application of this algorithmic design pattern.
* **Complexity Analysis**: Ability to use timing modules to empirically measure the theoretical efficiency of O(N log N) versus O(N^2).
* **Recursion**: Use of recursion for list division.
