# Proyecto N°14: Envío de Reportes Automáticos por Email
## Automatización de Notificaciones con `smtplib`

## 1. Objetivo y Resumen

El objetivo de este proyecto es implementar una rutina de **automatización** que envíe reportes, notificaciones o mensajes de estado predefinidos a través de correo electrónico.

El proyecto demuestra la habilidad de Python para interactuar con protocolos de internet, específicamente el protocolo **SMTP** (Simple Mail Transfer Protocol), utilizando la biblioteca estándar **`smtplib`**. Esto es esencial para tareas como enviar informes diarios, alertas de errores de servidor o confirmaciones de usuario.

**Conceptos Centrales:** **Automatización**, **Protocolo SMTP**, **Cifrado TLS/SSL** (para la seguridad del envío), **MIMEMultipart** (para correos con formato HTML).

---

## 2. Tecnologías y Herramientas Utilizadas

Este proyecto se basa completamente en librerías integradas de Python, lo que lo hace muy ligero y portátil.

* **Lenguaje:** Python 3.x
* **Biblioteca SMTP:** **`smtplib`** (Para la conexión, autenticación y envío al servidor de correo).
* **Biblioteca Email:** **`email.mime`** (Para construir el correo con encabezados, asunto y cuerpo en formato HTML/plano).
* **Seguridad:** **`ssl`** (Asegura que la comunicación a través del puerto 587 se cifre usando TLS).
* **Mejor Práctica:** Uso de un archivo **`config.py`** externo para gestionar las credenciales sensibles.

---

## 3. Desarrollo del Proyecto (Estructura y Componentes)

El *script* está dividido en tres componentes lógicos claros:

1.  **Configuración Segura:** Las credenciales de email (`REMITENTE_EMAIL`, `REMITENTE_PASSWORD`) y los detalles del servidor SMTP se almacenan en el archivo **`config.py`**. Esto aísla los secretos del código principal, permitiendo que el desarrollador pueda añadir `config.py` al archivo **`.gitignore`** para **nunca subir sus credenciales a GitHub**.
2.  **Construcción del Mensaje (`crear_mensaje`):** Utiliza la clase `MIMEMultipart` y contenido **HTML** para construir un correo profesional y formateado, no solo texto plano. Esto mejora la presentación del reporte.
3.  **Lógica de Envío (`enviar_email`):**
    * Establece una conexión segura con `smtplib.SMTP` y `server.starttls()`.
    * Realiza la autenticación con `server.login()` usando las variables de `config`.
    * Envía el mensaje y maneja errores de autenticación cruciales para la robustez del proceso.

---

## 4. Estructura del Repositorio y Archivos

Programacion_con_Python/
└── Proyecto14_Reporte_Email_Automatico/
    ├── reporte_automatico_email.py  <-- Lógica principal (Envío)
    ├── config.py                    <-- Credenciales SMTP (IGNORADO POR GIT)
    └── README.md                    <-- Documentación del proyecto

---

## 5. Conclusiones

Este proyecto demuestra un dominio avanzado de:

* **Automatización de Tareas:** Capacidad para integrar servicios de comunicación (Email) en flujos de trabajo de Python.
* **Protocolos de Red:** Entendimiento y uso correcto del protocolo SMTP con cifrado TLS/SSL.
* **Manejo de Contenido:** Habilidad para construir mensajes complejos que utilizan formato **HTML** para una presentación profesional.
* **Seguridad y Mejores Prácticas:** Implementación de la separación de secretos (credenciales) del código fuente, una práctica obligatoria en el desarrollo profesional.

---