# -*- coding: utf-8 -*-
# Nota: El magic comment arriba asegura que los acentos se lean correctamente.
import json
import os
import sys

NOMBRE_ARCHIVO = "libreria.json"

# --- MÓDULO DE PERSISTENCIA (JSON) ---

def cargar_datos():
    """
    Intenta cargar los datos de la librería desde el archivo JSON.
    Si el archivo no existe o está vacío, retorna un diccionario vacío.
    """
    if not os.path.exists(NOMBRE_ARCHIVO):
        print(f"Archivo '{NOMBRE_ARCHIVO}' no encontrado. Inicializando librería vacía.")
        return {}
    
    try:
        with open(NOMBRE_ARCHIVO, 'r', encoding='utf-8') as archivo:
            datos = json.load(archivo)
            print(f"Datos cargados exitosamente desde '{NOMBRE_ARCHIVO}'.")
            return datos
    except json.JSONDecodeError:
        print("Advertencia: El archivo JSON está vacío o corrupto. Inicializando librería vacía.")
        return {}
    except Exception as e:
        print(f"Error al cargar datos: {e}")
        return {}

def guardar_datos(libreria):
    """
    Guarda el diccionario completo de la librería en el archivo JSON.
    """
    try:
        with open(NOMBRE_ARCHIVO, 'w', encoding='utf-8') as archivo:
            # indent=4 para formato legible; ensure_ascii=False para guardar acentos.
            json.dump(libreria, archivo, indent=4, ensure_ascii=False)
            print(f"Datos guardados exitosamente en '{NOMBRE_ARCHIVO}'.")
    except Exception as e:
        print(f"Error al guardar datos: {e}")


# --- MÓDULO DE OPERACIONES AUXILIARES ---

def mostrar_libro(isbn, detalles):
    """Función auxiliar para imprimir los detalles de un solo libro."""
    print("---------------------------------")
    print(f"  ISBN: {isbn}")
    print(f"  Título: {detalles['titulo']}")
    print(f"  Autor: {detalles['autor']}")
    print(f"  Año: {detalles['año']}")
    print(f"  Inventario: {detalles['cantidad']} copias")
    print("---------------------------------")


# --- MÓDULO DE OPERACIONES (CRUD) ---

def agregar_libro(libreria):
    """Añade un libro nuevo o actualiza la cantidad si el ISBN existe."""
    print("\n--- AÑADIR NUEVO LIBRO ---")
    isbn = input("Ingrese el ISBN (código único del libro): ").strip()
    
    if not isbn:
        print("El ISBN no puede estar vacío.")
        return

    if isbn in libreria:
        print(f"Libro ya encontrado: '{libreria[isbn]['titulo']}'.")
        try:
            cantidad_adicional = int(input("Ingrese la cantidad de copias a añadir: "))
            if cantidad_adicional > 0:
                libreria[isbn]['cantidad'] += cantidad_adicional
                print(f"Inventario actualizado. Cantidad total: {libreria[isbn]['cantidad']}")
            else:
                print("No se añadió ninguna copia.")
        except ValueError:
            print("Entrada inválida. La cantidad debe ser un número entero.")
        return
    
    else:
        print("Nuevo libro detectado. Ingrese los detalles:")
        titulo = input("Título: ").strip()
        autor = input("Autor: ").strip()
        try:
            año = int(input("Año de Publicación: "))
            cantidad = int(input("Cantidad de copias a ingresar: "))
            
            if cantidad <= 0:
                print("La cantidad inicial debe ser mayor que cero.")
                return

            libreria[isbn] = {
                "titulo": titulo,
                "autor": autor,
                "año": año,
                "cantidad": cantidad
            }
            print(f"Libro '{titulo}' añadido exitosamente a la librería.")
        except ValueError:
            print("Entrada inválida. El año y la cantidad deben ser números enteros.")


def buscar_libro(libreria):
    """Busca libros por término de búsqueda en Título o Autor."""
    print("\n--- BUSCAR LIBRO ---")
    termino = input("Ingrese Título o Autor a buscar: ").strip().lower()

    if not termino:
        print("El término de búsqueda no puede estar vacío.")
        return

    libros_encontrados = {}
    
    for isbn, detalles in libreria.items():
        titulo_lower = detalles['titulo'].lower()
        autor_lower = detalles['autor'].lower()
        
        # Lógica de búsqueda lineal
        if termino in titulo_lower or termino in autor_lower:
            libros_encontrados[isbn] = detalles

    if libros_encontrados:
        print(f"\n Se encontraron {len(libros_encontrados)} resultados para '{termino}':")
        for isbn, detalles in libros_encontrados.items():
            mostrar_libro(isbn, detalles)
    else:
        print(f"No se encontraron libros que coincidan con '{termino}'.")


def listar_libros(libreria):
    """Lista todos los libros actualmente en el inventario."""
    if not libreria:
        print("\n La librería está vacía. Añade algunos libros primero.")
        return

    total_libros_fisicos = 0
    
    print("\n--- INVENTARIO COMPLETO DE LA LIBRERÍA ---")
    print(f"Número total de títulos únicos: {len(libreria)}")
    
    for isbn, detalles in libreria.items():
        mostrar_libro(isbn, detalles)
        total_libros_fisicos += detalles['cantidad']
        
    print(f"\n Total de copias físicas en stock: {total_libros_fisicos}")
    print("------------------------------------------")


def eliminar_libro(libreria):
    """Elimina un libro completo del inventario usando su ISBN."""
    print("\n--- ELIMINAR LIBRO DEL INVENTARIO ---")
    isbn = input("Ingrese el ISBN del libro que desea ELIMINAR: ").strip()

    if not isbn:
        print("El ISBN no puede estar vacío.")
        return

    if isbn in libreria:
        titulo_a_eliminar = libreria[isbn]['titulo']
        
        confirmacion = input(f"¿Está seguro que desea eliminar '{titulo_a_eliminar}' y TODAS sus copias? (sí/no): ").lower()
        
        if confirmacion == 'sí' or confirmacion == 'si':
            del libreria[isbn]
            print(f"El libro '{titulo_a_eliminar}' (ISBN: {isbn}) ha sido eliminado permanentemente.")
        else:
            print("Eliminación cancelada.")
    else:
        print(f"No se encontró ningún libro con el ISBN: {isbn}")


# --- FUNCIÓN PRINCIPAL (MENÚ) ---

def main():
    # 1. Cargar datos al inicio
    libreria = cargar_datos()

    while True:
        print("\n\n--- MENÚ PRINCIPAL ---")
        print("1. Añadir/Actualizar Libro")
        print("2. Buscar Libro (Título/Autor)")
        print("3. Listar Inventario Completo")
        print("4. Eliminar Libro (por ISBN)")
        print("5. Salir y Guardar")
        
        opcion = input("Seleccione una opción: ").strip()

        if opcion == '1':
            agregar_libro(libreria)
        elif opcion == '2':
            buscar_libro(libreria)
        elif opcion == '3':
            listar_libros(libreria)
        elif opcion == '4':
            eliminar_libro(libreria)
        elif opcion == '5':
            # 2. Guardar datos al salir
            guardar_datos(libreria)
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()