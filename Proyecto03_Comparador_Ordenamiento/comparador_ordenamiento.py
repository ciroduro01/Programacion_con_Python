import time
import random
import sys

# --- 1. FUNCIONES DE UTILIDAD ---

def generar_lista_aleatoria(N):
    """Genera una lista de N enteros aleatorios."""
    # Números entre 1 y 100,000
    return [random.randint(1, 100000) for _ in range(N)]

def medir_tiempo(algoritmo, lista):
    """
    Mide el tiempo de ejecución de un algoritmo de ordenamiento
    sobre una copia de la lista.
    """
    # Crear una copia de la lista original
    lista_copia = lista[:] 
    
    inicio = time.time()
    algoritmo(lista_copia)
    fin = time.time()
    
    return fin - inicio

# --- 2. IMPLEMENTACIONES DE ALGORITMOS O(N^2) ---

def ordenamiento_burbuja(lista):
    """Implementación del algoritmo Bubble Sort."""
    n = len(lista)
    for i in range(n):
        # Optimización: si no hubo intercambios en un ciclo, la lista está ordenada
        intercambiado = False
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                intercambiado = True
        if not intercambiado:
            break

def ordenamiento_seleccion(lista):
    """Implementación del algoritmo Selection Sort."""
    n = len(lista)
    for i in range(n):
        # Asumir que el elemento actual es el mínimo
        min_idx = i
        for j in range(i + 1, n):
            # Encontrar el índice del verdadero mínimo
            if lista[j] < lista[min_idx]:
                min_idx = j
                
        # Intercambiar el elemento mínimo encontrado con el elemento en la posición i
        lista[i], lista[min_idx] = lista[min_idx], lista[i]

# --- 3. FUNCIÓN COMPARADORA Y REPORTE ---

def comparar_algoritmos(N):
    """
    Compara el rendimiento de los algoritmos de ordenamiento.
    """
    print(f"--- INICIO DE LA COMPARACIÓN DE ALGORITMOS ---")
    print(f"Generando una lista de {N} elementos aleatorios...")
    
    try:
        # Generar una única lista base
        lista_base = generar_lista_aleatoria(N)
    except MemoryError:
        print(f"Error: No hay suficiente memoria para generar una lista de {N} elementos.")
        return

    # Definición de los algoritmos a probar
    algoritmos = [
        ("Bubble Sort (O(N^2))", ordenamiento_burbuja),
        ("Selection Sort (O(N^2))", ordenamiento_seleccion),
    ]
    
    resultados = []
    
    print("-" * 40)

    for nombre, algoritmo_func in algoritmos:
        print(f"Ejecutando {nombre}...")
        try:
            tiempo_ejecucion = medir_tiempo(algoritmo_func, lista_base)
            resultados.append((nombre, tiempo_ejecucion))
            print(f"   -> Tiempo: {tiempo_ejecucion:.4f} segundos")
        except RecursionError:
            print(f"   -> ERROR: El algoritmo {nombre} falló por recursión (evitar para este proyecto).")
        except Exception as e:
            print(f"   -> ERROR INESPERADO en {nombre}: {e}")

    # Mostrar Reporte Final
    print("\n\n--- REPORTE FINAL DE RENDIMIENTO ---")
    
    # Ordenar los resultados por tiempo (el más rápido primero)
    resultados.sort(key=lambda x: x[1]) 
    
    for i, (nombre, tiempo) in enumerate(resultados):
        print(f"#{i+1}: {nombre.ljust(25)} -> {tiempo:.6f} s")
        
    print(f"\n Prueba realizada con N = {N} elementos.")
    print("------------------------------------------------")


# --- 4. FUNCIÓN MAIN ---

if __name__ == "__main__":
    # N = 10000 o 20000 es un buen tamaño para que O(N^2) tarde unos segundos.
    
    # Manejo de argumentos opcional para cambiar el tamaño de N
    N_TEST = 10000 
    if len(sys.argv) > 1:
        try:
            N_TEST = int(sys.argv[1])
            if N_TEST <= 0:
                raise ValueError
        except ValueError:
            print("El argumento N debe ser un número entero positivo.")
            sys.exit(1)
            
    comparar_algoritmos(N=N_TEST)