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