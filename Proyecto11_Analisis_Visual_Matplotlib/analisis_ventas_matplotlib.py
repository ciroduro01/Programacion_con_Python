# analisis_ventas_matplotlib.py
import matplotlib.pyplot as plt
import random
from collections import Counter

# --- 1. SIMULACIÓN DE DATOS ---

# Datos para Gráfico de Barras (Ventas por Sucursal)
SUCURSALES = ['Sucursal A', 'Sucursal B', 'Sucursal C', 'Sucursal D']
# Genera un número aleatorio de unidades vendidas para cada sucursal
VENTAS_SUCURSAL = [random.randint(250, 700) for _ in SUCURSALES]

# Datos para Gráfico Circular (Distribución de Productos)
# Simula 300 ventas y cuenta cuántas son de cada tipo de producto
PRODUCTOS_VENDIDOS = [random.choice(['Laptop', 'Monitor', 'Teclado', 'Mouse', 'Webcam']) for _ in range(300)]
CONTEO_PRODUCTOS = Counter(PRODUCTOS_VENDIDOS) 


# --- 2. FUNCIONES DE VISUALIZACIÓN ---

def generar_grafico_barras(etiquetas, valores, titulo, eje_x, eje_y):
    """Genera un gráfico de barras comparativo (Gráfico 1)."""
    
    plt.figure(figsize=(9, 6)) # Tamaño de la figura
    
    # Crear el gráfico de barras
    barras = plt.bar(etiquetas, valores, color='#4CAF50')
    
    # Personalización: Títulos y Etiquetas
    plt.title(titulo, fontsize=16, fontweight='bold')
    plt.xlabel(eje_x, fontsize=12)
    plt.ylabel(eje_y, fontsize=12)
    
    # Mostrar el valor exacto encima de cada barra
    for bar in barras:
        yval = bar.get_height()
        # Añade la etiqueta de texto con el valor
        plt.text(bar.get_x() + bar.get_width()/2.0, yval + 15, int(yval), ha='center', va='bottom', fontsize=10)
        
    plt.tight_layout() 
    plt.grid(axis='y', linestyle='--', alpha=0.5)
    plt.show()

def generar_grafico_circular(datos_conteo, titulo):
    """Genera un gráfico circular para mostrar la distribución porcentual (Gráfico 2)."""
    
    etiquetas = list(datos_conteo.keys())
    tamaños = list(datos_conteo.values())
    
    colores = ['#FF9999', '#66B2FF', '#99FF99', '#FFCC99', '#C2C2F0']
    
    # Define la 'explosión' para el producto más vendido
    max_count = max(tamaños)
    max_index = tamaños.index(max_count)
    explode = [0] * len(etiquetas)
    explode[max_index] = 0.1 # Separa la rebanada más grande
    
    plt.figure(figsize=(8, 8))
    
    # Crear el gráfico circular
    plt.pie(tamaños, 
            labels=etiquetas, 
            autopct='%1.1f%%', # Formato de porcentaje
            startangle=90, 
            colors=colores, 
            explode=explode,
            shadow=True,
            wedgeprops={'edgecolor': 'black'}) 

    # Personalización
    plt.title(titulo, fontsize=16, fontweight='bold')
    plt.axis('equal') # Asegura que el círculo sea un círculo
    plt.show()


# --- 3. FUNCIÓN PRINCIPAL (MAIN) ---

def main():
    print("Proyecto N°11: Análisis Visual de Datos con Matplotlib")

    # Generar Gráfico de Barras
    print("\nGenerando Gráfico 1: Comparativa de Ventas por Sucursal...")
    generar_grafico_barras(SUCURSALES, VENTAS_SUCURSAL, 
                           "Ventas Totales por Sucursal (Unidades)", 
                           "Sucursal", "Total de Unidades Vendidas")
    
    # Generar Gráfico Circular
    print("Generando Gráfico 2: Distribución de Productos...")
    generar_grafico_circular(CONTEO_PRODUCTOS, "Participación Porcentual por Producto")
    
    print("\nAnálisis visual completado. Cierre las ventanas de los gráficos para finalizar.")


if __name__ == "__main__":
    main()