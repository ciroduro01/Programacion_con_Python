import string
from collections import Counter
import sys

def leer_archivo(nombre_archivo):
    """
    Abre y lee el contenido de un archivo de texto.
    
    Args:
        nombre_archivo (str): El nombre del archivo a leer.
        
    Returns:
        str: El contenido del archivo como una sola cadena, o cadena vacía si hay un error.
    """
    try:
        # Usa 'with open' para garantizar que el archivo se cierre automáticamente
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            contenido = archivo.read()
            return contenido
    except FileNotFoundError:
        print(f"\n ERROR: El archivo '{nombre_archivo}' no se encontró.")
        # Retorna None o cadena vacía para indicar un fallo
        return ""
    except Exception as e:
        print(f"\n ERROR inesperado al leer el archivo: {e}")
        return ""

def limpiar_texto(texto):
    """
    Normaliza el texto: convierte a minúsculas, elimina puntuación 
    y retorna una lista de palabras.
    
    Args:
        texto (str): La cadena de texto a limpiar.
        
    Returns:
        list: Una lista de palabras limpias.
    """
    # 1. Convertir a minúsculas
    texto = texto.lower()
    
    # 2. Reemplazar caracteres de puntuación por espacios
    # Utilizamos string.punctuation para obtener todos los símbolos comunes
    for caracter in string.punctuation:
        texto = texto.replace(caracter, ' ')
        
    # 3. Dividir la cadena en una lista de palabras. 
    # split() maneja múltiples espacios generados por la limpieza
    palabras = texto.split() 
    
    # 4. Filtrar cualquier cadena vacía que pueda haber quedado
    return [palabra for palabra in palabras if palabra]

def contar_frecuencias(lista_palabras):
    """
    Cuenta la frecuencia de cada palabra usando collections.Counter.
    
    Args:
        lista_palabras (list): Lista de palabras limpias.
        
    Returns:
        Counter: Un objeto Counter con las frecuencias de palabras.
    """
    # Counter es la estructura de datos ideal para este propósito
    return Counter(lista_palabras) 

def generar_reporte(frecuencias, N=10):
    """
    Imprime un informe estructurado de las métricas y las palabras más comunes.
    
    Args:
        frecuencias (Counter): Objeto Counter con las frecuencias.
        N (int): Número de palabras top a mostrar.
    """
    if not frecuencias:
        print("No se encontraron palabras para analizar. El archivo estaba vacío o el contenido no pudo ser procesado.")
        return
        
    # Métricas generales
    total_palabras = sum(frecuencias.values())
    palabras_unicas = len(frecuencias)
    
    print("\n--- INFORME DEL ANALIZADOR DE TEXTO ---")
    print(f"Archivo procesado con éxito.")
    print(f"Total de palabras: {total_palabras}")
    print(f"Palabras únicas: {palabras_unicas}")
    print("--------------------------------------")
    
    # Top N más comunes usando el método most_common()
    top_palabras = frecuencias.most_common(N) 

    print(f"\n TOP {N} PALABRAS MÁS COMUNES:")
    for palabra, cuenta in top_palabras:
        print(f"  - {palabra}: {cuenta}")
    print("--------------------------------------")

def main():
    """
    Función principal que orquesta el flujo de trabajo del programa.
    """
    # Pide al usuario el nombre del archivo de forma interactiva
    nombre_archivo = input("Ingrese el nombre del archivo de texto (ej. texto.txt): ")
    
    # 1. Leer el archivo y obtener el contenido
    contenido = leer_archivo(nombre_archivo)
    
    # Si la lectura falló (contenido es cadena vacía), termina el programa
    if not contenido:
        # sys.exit(1) indica un cierre con error
        sys.exit(1) 
    
    # 2. Limpiar el texto
    palabras_limpias = limpiar_texto(contenido)
    
    # 3. Contar las frecuencias
    frecuencias = contar_frecuencias(palabras_limpias)
    
    # 4. Generar el reporte final
    generar_reporte(frecuencias, N=10)

if __name__ == "__main__":
    main()