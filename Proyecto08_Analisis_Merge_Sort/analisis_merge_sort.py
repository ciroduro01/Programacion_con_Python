# analisis_merge_sort.py
import time
import random

# --- Implementación Merge Sort (O(N log N)) ---

def merge(izquierda, derecha):
    """
    Función auxiliar que combina dos listas ya ordenadas.
    """
    resultado = []
    i = j = 0

    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] < derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1

    # Agrega los elementos restantes de cualquiera de las listas
    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])
    
    return resultado

def merge_sort(lista):
    """
    Función principal: Divide la lista recursivamente (Divide y Conquistar).
    """
    # CASO BASE
    if len(lista) <= 1:
        return lista

    # División
    mitad = len(lista) // 2
    izquierda = lista[:mitad]
    derecha = lista[mitad:]

    # Llamadas recursivas para ordenar y Mezclar
    lista_izquierda_ordenada = merge_sort(izquierda)
    lista_derecha_ordenada = merge_sort(derecha)
    
    return merge(lista_izquierda_ordenada, lista_derecha_ordenada)


# --- Implementación Bubble Sort (O(N²)) para comparación ---

def bubble_sort(lista):
    """
    Implementación simple del Bubble Sort (O(N²)).
    """
    n = len(lista)
    lista_copia = lista[:]
    
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista_copia[j] > lista_copia[j + 1]:
                lista_copia[j], lista_copia[j + 1] = lista_copia[j + 1], lista_copia[j]
    return lista_copia


# --- Funciones de Utilidad y Cronometraje ---

def crear_datos_aleatorios(tamano):
    """Crea una lista de números enteros aleatorios para la prueba."""
    return [random.randint(1, 100000) for _ in range(tamano)]

def cronometrar(func, datos):
    """Ejecuta una función de ordenamiento y devuelve el tiempo en segundos."""
    inicio = time.perf_counter()
    func(datos)
    fin = time.perf_counter()
    return fin - inicio


def main():
    print("Análisis Comparativo de Algoritmos de Ordenamiento")
    
    tamanos = [1000, 5000, 10000, 20000] 

    print("\n| Tamaño (N) | Merge Sort (O(N log N)) | Bubble Sort (O(N²)) |")
    print("|------------|-------------------------|---------------------|")

    for tamano in tamanos:
        datos = crear_datos_aleatorios(tamano)
        
        tiempo_merge = cronometrar(merge_sort, datos[:])
        
        if tamano <= 10000:
            tiempo_bubble = cronometrar(bubble_sort, datos[:])
        else:
            tiempo_bubble = "MUY LENTO (>1s)"
        
        # Imprimir los resultados en formato de tabla
        print(f"| {tamano:<10} | {tiempo_merge:^23.6f}s | {tiempo_bubble:^19} |")
        
        if tamano > 10000 and isinstance(tiempo_bubble, str):
             print(f"Nota: La prueba de Bubble Sort se detuvo para N={tamano} debido a su complejidad O(N²).")

    print("\nConclusión (Big O Notation):")
    print("La diferencia en el tiempo de ejecución demuestra que los algoritmos O(N log N)")
    print("son exponencialmente más rápidos que los O(N²) para grandes volúmenes de datos.")


if __name__ == "__main__":
    main()