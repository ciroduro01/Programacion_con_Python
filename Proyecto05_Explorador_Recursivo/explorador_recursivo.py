# explorador_recursivo.py
import os
import sys

# Lista global para almacenar los archivos encontrados y sus tamaños
archivos_encontrados = []

# --- Funciones de Utilidad ---

def formatear_bytes(bytes_valor):
    """Convierte bytes a un formato legible (KB, MB, GB)."""
    if bytes_valor < 1024:
        return f"{bytes_valor:.2f} Bytes"
    elif bytes_valor < 1024 * 1024:
        return f"{bytes_valor / 1024:.2f} KB"
    elif bytes_valor < 1024 * 1024 * 1024:
        return f"{bytes_valor / (1024 * 1024):.2f} MB"
    else:
        return f"{bytes_valor / (1024 * 1024 * 1024):.2f} GB"

# --- Función Recursiva Central ---

def recorrer_directorio(ruta_actual):
    """
    Recorre un directorio y todos sus subdirectorios de forma recursiva,
    calculando el tamaño total.
    """
    tamano_total = 0.0

    # 1. CASO BASE 1: Si es un ARCHIVO
    if os.path.isfile(ruta_actual):
        try:
            tamano = os.path.getsize(ruta_actual)
            # Guardamos la información del archivo encontrado
            archivos_encontrados.append((ruta_actual, tamano))
            return tamano
        except OSError:
            # Manejo de permisos o archivos inaccesibles
            return 0.0

    # 2. PASO RECURSIVO: Si es un DIRECTORIO
    elif os.path.isdir(ruta_actual):
        print(f"Buscando en: {ruta_actual}") 
        
        try:
            # Iterar sobre el contenido del directorio
            for elemento in os.listdir(ruta_actual):
                ruta_completa = os.path.join(ruta_actual, elemento)
                
                #Llamada recursiva: La función se llama a sí misma
                tamano_total += recorrer_directorio(ruta_completa)
                
        except PermissionError:
            # Caso Base 2: Error de permisos (detiene la recursión en esta rama)
            print(f"Omite (Permiso Denegado): {ruta_actual}")
        except Exception as e:
            print(f"Error al procesar {ruta_actual}: {e}")
            
    return tamano_total

# --- Función de Reporte ---

def generar_reporte(ruta_inicial, tamano_total):
    """Imprime el resumen de la búsqueda recursiva."""
    print("\n" + "=" * 50)
    print(f"REPORTE DE EXPLORACIÓN RECURSIVA")
    print(f"Ruta Inicial: {ruta_inicial}")
    print("=" * 50)
    
    if not archivos_encontrados:
        print("No se encontraron archivos o el directorio está vacío.")
        return

    print(f"Total de archivos encontrados: {len(archivos_encontrados)}")
    print(f"Tamaño total: {formatear_bytes(tamano_total)}")
    print("=" * 50)
    
    # Mostrar los 5 archivos más grandes encontrados
    print("\nTop 5 Archivos más Grandes:")
    # Ordenar por tamaño (segundo elemento de la tupla) de forma descendente
    archivos_encontrados.sort(key=lambda x: x[1], reverse=True)
    
    for ruta, tamano in archivos_encontrados[:5]:
        print(f"- {formatear_bytes(tamano).ljust(10)}: {ruta}")
    print("-" * 50)

# --- FUNCIÓN PRINCIPAL (MAIN) ---

def main():
    if len(sys.argv) < 2:
        # Pide la ruta al usuario si no se proporciona como argumento
        ruta = input("Ingrese la ruta del directorio a explorar (ej: . o /ruta/completa): ").strip()
    else:
        # Usa el argumento de la línea de comandos
        ruta = sys.argv[1]

    if not os.path.isdir(ruta):
        print(f"Error: La ruta '{ruta}' no es un directorio válido o no existe.")
        return

    print(f"Iniciando exploración recursiva en: {ruta}")
    
    #Llamada inicial a la función recursiva
    tamano_total_bytes = recorrer_directorio(ruta)
    
    # Generar el resumen final
    generar_reporte(ruta, tamano_total_bytes)


if __name__ == "__main__":
    # La máxima profundidad de la recursión se maneja automáticamente por Python,  pero puede ser ajustada si se trabaja con árboles muy profundos.
    # sys.setrecursionlimit(2000)
    main()