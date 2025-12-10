# reporte_automatico_email.py
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import ssl # Módulo para el contexto de seguridad
import config
# from config import *
def crear_mensaje():
    """Construye el objeto MIMEMultipart con el asunto, destinatarios y contenido HTML."""
    
    # Crea el objeto principal (multipart)
    msg = MIMEMultipart('alternative')
    msg['From'] = config.REMITENTE_EMAIL
    msg['To'] = config.DESTINATARIO_EMAIL
    msg['Subject'] = "Reporte de Automatización Generado por Python (Proyecto N°14)"

    # Contenido HTML para un formato profesional
    html_body = """\
    <html>
      <body style="font-family: Arial, sans-serif; color: #333;">
        <h2 style="color: #1976D2;">Notificación de Tarea de Automatización</h2>
        <p>Estimado usuario,</p>
        <p>Este es un reporte automático generado por el script de Python, demostrando la capacidad de enviar correos con formato HTML seguro.</p>
        
        <table style="border-collapse: collapse; width: 60%; margin-top: 15px;">
          <thead>
            <tr style="background-color: #E3F2FD;">
              <th style="border: 1px solid #BBDEFB; padding: 10px; text-align: left;">Tarea</th>
              <th style="border: 1px solid #BBDEFB; padding: 10px; text-align: left;">Estado</th>
              <th style="border: 1px solid #BBDEFB; padding: 10px; text-align: left;">Resultado</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td style="border: 1px solid #E0E0E0; padding: 10px;">Consolidación CSV</td>
              <td style="border: 1px solid #E0E0E0; padding: 10px; color: green;">Éxito</td>
              <td style="border: 1px solid #E0E0E0; padding: 10px;">60 Registros procesados</td>
            </tr>
            <tr>
              <td style="border: 1px solid #E0E0E0; padding: 10px;">Web Scraper</td>
              <td style="border: 1px solid #E0E0E0; padding: 10px; color: orange;">Advertencia</td>
              <td style="border: 1px solid #E0E0E0; padding: 10px;">1 fallo en extracción</td>
            </tr>
          </tbody>
        </table>
        
        <p style="margin-top: 25px;">Si tiene alguna pregunta, contacte al administrador del sistema (Python).</p>
      </body>
    </html>
    """
    
    # Adjuntar la versión HTML al objeto principal
    msg.attach(MIMEText(html_body, 'html'))
    
    return msg

def enviar_email(mensaje):
    """Establece la conexión segura con el servidor SMTP y envía el correo."""
    
    if config.REMITENTE_PASSWORD == "tu_contraseña_de_aplicacion":
        print("¡ERROR DE CONFIGURACIÓN! Por favor, reemplace las variables REMITENTE_EMAIL y REMITENTE_PASSWORD en el código antes de ejecutar.")
        return

    try:
        print(f"Conectando al servidor SMTP ({config.SMTP_SERVER}:{config.SMTP_PORT})...")
        
        # 1. Establecer la conexión
        server = smtplib.SMTP(config.SMTP_SERVER, config.SMTP_PORT)
        
        # 2. Iniciar TLS (Transport Layer Security) para cifrar la conexión
        server.starttls() 
        
        # 3. Autenticación
        server.login(config.REMITENTE_EMAIL, config.REMITENTE_PASSWORD)
        print("Autenticación exitosa.")
        
        # 4. Envío del correo
        texto = mensaje.as_string()
        server.sendmail(config.REMITENTE_EMAIL, config.DESTINATARIO_EMAIL, texto)
        
        print(f"Correo enviado exitosamente a {config.DESTINATARIO_EMAIL}")
        
    except smtplib.SMTPAuthenticationError:
        print("Error de autenticación. Verifique sus credenciales y si está usando una 'Contraseña de Aplicación'.")
    except Exception as e:
        print(f"Error al enviar el correo: {e}")
    finally:
        # 5. Cerrar la conexión
        if 'server' in locals():
            server.quit()
            print("Conexión SMTP cerrada.")

def main():
    mensaje = crear_mensaje()
    enviar_email(mensaje)

if __name__ == "__main__":
    main()