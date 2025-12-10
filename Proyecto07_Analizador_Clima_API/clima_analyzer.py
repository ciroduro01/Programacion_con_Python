# clima_analyzer.py
import requests
import json
import sys

# IMPORTANTE: Asegurarse de tener el archivo config.py en el mismo directorio
# El archivo config.py debe contener: API_KEY = "TU_CLAVE_AQUÍ"
try:
    import config
    API_KEY = config.API_KEY
    if not API_KEY or API_KEY == "TU_CLAVE_SECRETA_DE_OPENWEATHERMAP":
        raise ValueError("La API_KEY en config.py no ha sido configurada.")
except (ImportError, ValueError, AttributeError) as e:
    print(f"Error crítico en configuración: {e}")
    print("Asegúrate de que 'config.py' existe y contiene una API_KEY válida.")
    sys.exit(1)


class ClimaAnalyzer:
    """Clase para gestionar la conexión, el procesamiento de JSON y la exportación de datos de clima."""
    def __init__(self, api_key):
        self.api_key = api_key
        self.url_base = "http://api.openweathermap.org/data/2.5/weather"
        self.datos_procesados = []

    def fetch_data(self, ciudad):
        """
        Realiza una petición GET a la API del clima y procesa la respuesta.
        """
        parametros = {
            'q': ciudad,
            'appid': self.api_key,
            'units': 'metric',  # Celsius
            'lang': 'es'        # Español
        }

        print(f"\n Solicitando datos para: {ciudad}...")
        
        try:
            # 1. Petición GET
            respuesta = requests.get(self.url_base, params=parametros)
            
            # 2. Manejo de Errores HTTP: Lanza excepción para códigos 4xx/5xx
            respuesta.raise_for_status() 
            
            # 3. Deserialización: JSON a diccionario de Python
            datos_json = respuesta.json()
            
            # 4. Procesamiento
            self._procesar_y_guardar(ciudad, datos_json)
            
            return True

        except requests.exceptions.HTTPError as e:
            # Captura errores como 404 (ciudad no existe) o 401 (API Key inválida)
            print(f"Error HTTP ({respuesta.status_code}) al buscar {ciudad}: {e}")
        except requests.exceptions.ConnectionError:
            print("Error de Conexión: Verifique su red o la URL de la API.")
        except requests.exceptions.RequestException as e:
            print(f"Error desconocido en la petición: {e}")
        
        return False

    def _procesar_y_guardar(self, ciudad, datos_json):
        """Método interno para extraer los datos relevantes del JSON complejo."""
        
        try:
            # Extracción segura de datos clave
            datos_clima = {
                'Ciudad': ciudad,
                'Temperatura_C': datos_json['main']['temp'],
                'Sensacion_Termica_C': datos_json['main']['feels_like'],
                'Humedad_Porcentaje': datos_json['main']['humidity'],
                'Viento_Velocidad_m/s': datos_json['wind']['speed'],
                'Descripcion_Clima': datos_json['weather'][0]['description'].capitalize() 
            }
            
            self.datos_procesados.append(datos_clima)
            print(f"Datos de {ciudad} procesados correctamente.")
        except KeyError as e:
            print(f"Error de estructura JSON en {ciudad}: Falta la clave {e}.")


    def exportar_a_json(self, nombre_archivo="reporte_clima.json"):
        """Exporta la lista de diccionarios procesados a un archivo JSON."""
        if not self.datos_procesados:
            print("\n No hay datos procesados para exportar.")
            return

        try:
            with open(nombre_archivo, 'w', encoding='utf-8') as f:
                # Serializa el objeto de Python a JSON en el archivo (indent=4 para legibilidad)
                json.dump(self.datos_procesados, f, indent=4, ensure_ascii=False)
            print(f"\n Éxito: Datos exportados a {nombre_archivo}")
            return True
        except IOError:
            print(f"Error al escribir en el archivo {nombre_archivo}.")
            return False

# --- FUNCIÓN PRINCIPAL (MAIN) ---

def main():
    # Lista de ciudades a analizar
    ciudades_a_buscar = [
        "Buenos Aires", 
        "Tokio", 
        "Londres", 
        "Rio de Janeiro",
        "Ciudad Que No Existe" # Prueba de manejo de errores 404
    ]

    # Crear la instancia de la clase
    analizador = ClimaAnalyzer(api_key=API_KEY)
    
    print("Iniciando Analizador de Clima con API")

    # Bucle para procesar cada ciudad
    for ciudad in ciudades_a_buscar:
        analizador.fetch_data(ciudad)
    
    # Exportar los datos procesados al archivo JSON
    analizador.exportar_a_json()

if __name__ == "__main__":
    main()