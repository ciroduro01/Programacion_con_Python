# consolidador_csv.py
import csv
import os
import glob 

# --- CONFIGURACIÓN ---
CARPETA_FUENTE = "reportes_ventas"
ARCHIVO_SALIDA = "reporte_consolidado.csv"
COLUMNAS_SALIDA = [
    "ID_Venta", 
    "Producto", 
    "Cantidad", 
    "Monto_Unitario", 
    "Monto_Total", # Este es el campo calculado
    "Fecha", 
    "Sucursal"
]
# --- FIN CONFIGURACIÓN ---


def consolidar_reportes():
    """Busca todos los archivos CSV, los lee, procesa y consolida los datos."""
    datos_consolidados = []
    
    # 1. Búsqueda automatizada de archivos
    # Usamos glob para encontrar todos los archivos que terminan en .csv en la carpeta fuente
    rutas_archivos = glob.glob(os.path.join(CARPETA_FUENTE, "*.csv"))
    
    if not rutas_archivos:
        print(f"Error: No se encontraron archivos CSV en la carpeta '{CARPETA_FUENTE}'.")
        return

    print(f"Encontrados {len(rutas_archivos)} reportes para consolidar.")

    for ruta in rutas_archivos:
        nombre_archivo = os.path.basename(ruta)
        print(f"\n Procesando: {nombre_archivo}")
        
        try:
            # 2. Apertura y Lectura estructurada
            with open(ruta, mode='r', newline='', encoding='utf-8') as archivo:
                # DictReader lee cada fila como un diccionario usando los encabezados como claves
                lector = csv.DictReader(archivo)
                
                for fila_original in lector:
                    
                    try:
                        # 3. Conversión de tipos y manejo de errores (Limpieza)
                        cantidad = int(fila_original['Cantidad'])
                        monto_unitario = float(fila_original['Monto_Unitario'])
                        
                        # 4. Cálculo del Nuevo Campo
                        monto_total = round(cantidad * monto_unitario, 2)
                        
                        # 5. Construcción del Registro Final con la estructura de salida
                        registro_limpio = {
                            "ID_Venta": fila_original['ID_Venta'],
                            "Producto": fila_original['Producto'],
                            "Cantidad": cantidad,
                            "Monto_Unitario": monto_unitario,
                            "Monto_Total": monto_total, 
                            "Fecha": fila_original['Fecha'],
                            "Sucursal": fila_original['Sucursal']
                        }
                        
                        datos_consolidados.append(registro_limpio)
                        
                    except ValueError as ve:
                        print(f"Error de tipo de dato en fila (no es número): {ve}. Saltando fila.")
                        continue 
                    except KeyError as ke:
                        print(f"Error de encabezado: Falta la columna {ke} en el archivo. Saltando archivo.")
                        break

        except FileNotFoundError:
            print(f"Error: El archivo {nombre_archivo} no fue encontrado.")
        except Exception as e:
            print(f"Error desconocido al leer {nombre_archivo}: {e}")

    # 6. Escritura del Reporte Consolidado
    escribir_reporte_final(datos_consolidados)

def escribir_reporte_final(datos):
    """Escribe la lista consolidada de diccionarios en un nuevo archivo CSV."""
    if not datos:
        print("No hay datos válidos para escribir en el archivo final.")
        return

    try:
        # Abrir archivo para escritura
        with open(ARCHIVO_SALIDA, mode='w', newline='', encoding='utf-8') as archivo_salida:
            # DictWriter requiere la lista de encabezados (fieldnames)
            escritor = csv.DictWriter(archivo_salida, fieldnames=COLUMNAS_SALIDA)
            
            # Escribir el encabezado y las filas
            escritor.writeheader()
            escritor.writerows(datos)
            
        print(f"\n ¡Éxito! Datos de {len(datos)} registros consolidados y guardados en '{ARCHIVO_SALIDA}'.")
    except Exception as e:
        print(f"Error al escribir el archivo de salida: {e}")

if __name__ == "__main__":
    consolidar_reportes()