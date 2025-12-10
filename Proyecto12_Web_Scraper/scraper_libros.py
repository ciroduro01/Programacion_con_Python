# scraper_libros.py
import requests
from bs4 import BeautifulSoup
import time 

URL_BASE = "http://books.toscrape.com/"
URL_PAGINA = URL_BASE + "catalogue/page-1.html" 

def obtener_html(url):
    """Realiza la petición HTTP GET y devuelve el contenido HTML."""
    try:
        # Definir un User-Agent
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
        respuesta = requests.get(url, headers=headers)
        
        # Lanza una excepción si la respuesta no fue exitosa (código 4xx o 5xx)
        respuesta.raise_for_status() 
        
        return respuesta.text
    except requests.exceptions.RequestException as e:
        print(f"Error al realizar la petición a {url}: {e}")
        return None

def extraer_datos_pagina(html_content):
    """Analiza el HTML y extrae el título, precio y rating de cada libro."""
    if html_content is None:
        return []
    
    # Inicializa el parser BeautifulSoup
    sopa = BeautifulSoup(html_content, 'html.parser')
    libros_extraidos = []
    
    # Selector CSS para encontrar todas las tarjetas de libro
    tarjetas_libros = sopa.select('article.product_pod')

    for libro in tarjetas_libros:
        try:
            # 1. Extracción del Título (desde el atributo 'title' de la etiqueta <a>)
            titulo_elemento = libro.select_one('h3 > a')
            titulo = titulo_elemento['title'] if titulo_elemento else "N/A"
            
            # 2. Extracción y Limpieza del Precio
            precio_elemento = libro.select_one('p.price_color')
            # Limpiar el símbolo de moneda ('£' y 'Â' que a veces aparece)
            precio_texto = precio_elemento.get_text().replace('£', '').replace('Â', '') if precio_elemento else "0.00"
            precio = float(precio_texto.strip())

            # 3. Extracción del Rating (Calificación)
            rating_elemento = libro.select_one('p.star-rating')
            # El rating es la segunda clase CSS (ej. ['star-rating', 'Three'])
            rating = rating_elemento['class'][1] if rating_elemento and len(rating_elemento['class']) > 1 else "N/A"
            
            libros_extraidos.append({
                'titulo': titulo,
                'precio': precio,
                'rating': rating
            })
            
        except Exception as e:
            # Manejo de errores para no detener el proceso si una tarjeta está malformada
            print(f"Advertencia: Error al procesar un libro. Saltando. Detalle: {e}")
            continue 

    return libros_extraidos

def main():
    print("Proyecto N°12: Web Scraper de Libros (requests + BeautifulSoup)")
    
    # 1. Obtener el HTML
    html = obtener_html(URL_PAGINA)
    
    if html:
        # 2. Extraer los datos
        datos_libros = extraer_datos_pagina(html)
        
        if datos_libros:
            print(f"\n Extracción exitosa. Encontrados {len(datos_libros)} libros en la página 1.")
            print("\n--- EJEMPLO DE RESULTADO ---")
            
            # Mostrar los primeros 5 resultados
            for i, libro in enumerate(datos_libros[:5]):
                print(f"{i+1}. Título: {libro['titulo'][:60]}...")
                print(f"   Precio: ${libro['precio']:.2f} | Rating: {libro['rating']}")
            
            print("---------------------------")
        else:
            print("No se pudieron extraer datos de la página. Verifique selectores o conexión.")

if __name__ == "__main__":
    main()