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

1.  **Configuración Segura:** Las credenciales de email (`REMITENTE_EMAIL`, `REMITENTE_PASSWORD`) y los detalles del servidor SMTP se almacenan en el archivo **`config.py`**.
2.  **Construcción del Mensaje (`crear_mensaje`):** Utiliza la clase `MIMEMultipart` y contenido **HTML** para construir un correo profesional y formateado, no solo texto plano. Esto mejora la presentación del reporte.
3.  **Lógica de Envío (`enviar_email`):**
    * Establece una conexión segura con `smtplib.SMTP` y `server.starttls()`.
    * Realiza la autenticación con `server.login()` usando las variables de `config`.
    * Envía el mensaje y maneja errores de autenticación cruciales para la robustez del proceso.

---

## 4. Estructura del Repositorio y Archivos

```
Programacion_con_Python/
└── Proyecto14_Reporte_Email_Automatico/
    ├── reporte_automatico_email.py  <-- Lógica principal (Envío)
    ├── config.py                    <-- Credenciales SMTP (IGNORADO POR GIT)
    └── README.md                    <-- Documentación del proyecto
```
---

## 5. Conclusiones

Este proyecto demuestra un dominio avanzado de:

* **Automatización de Tareas:** Capacidad para integrar servicios de comunicación (Email) en flujos de trabajo de Python.
* **Protocolos de Red:** Entendimiento y uso correcto del protocolo SMTP con cifrado TLS/SSL.
* **Manejo de Contenido:** Habilidad para construir mensajes complejos que utilizan formato **HTML** para una presentación profesional.
* **Seguridad y Mejores Prácticas:** Implementación de la separación de secretos (credenciales) del código fuente, una práctica obligatoria en el desarrollo profesional.

---

# Project N°14: Sending Automatic Reports via Email (Automating Notifications with smtplib)

## 1. Objective and Overview

The objective of this project is to implement an automation routine that sends predefined reports, notifications, or status messages via email.

The project demonstrates Python's ability to interact with internet protocols, specifically the **SMTP** (Simple Mail Transfer Protocol), using the `smtplib` standard library. This is essential for tasks such as sending daily reports, server error alerts, or user confirmations.

**Core Concepts**: Automation, SMTP Protocol, TLS/SSL Encryption (for secure transmission), MIME Multipart (for HTML-formatted emails).

---

## 2. Technologies and Tools Used

This project is based entirely on built-in Python libraries, making it very lightweight and portable.

* **Language**: Python 3.x
* **SMTP Library**: `smtplib` (For connecting to, authenticating with, and sending to the mail server).
* **Email Library**: `email.mime` (To construct the email with headers, subject, and body in HTML/plain format).
* **Security**: `ssl` (Ensures that communication through port 587 is encrypted using TLS).
* **Best Practice**: Use an external `config.py` file to manage sensitive credentials.

---

## 3. Project Development (Structure and Components)

The script is divided into three clear logical components:

1. **Secure Configuration**: Email credentials (`REMITENTE_EMAIL`, `REMITENTE_PASSWORD`) and SMTP server details are stored in the `config.py` file.
2. **Message Construction (`crear_mensaje`)**: Uses the `MIMEMultipart` class and HTML content to construct a professional, formatted email, not just plain text. This improves the report's presentation.
3. **Sending Logic (`enviar_email`)**:
* Establishes a secure connection with `smtplib.SMTP` and `server.starttls()`.
* Perform authentication using `server.login()` with the `config` variables.
* Send the message and handle crucial authentication errors for process robustness.

---

## 4. Repository and File Structure

```bash
Programacion_con_Python/
└── Proyecto14_Reporte_Email_Automatico/
    ├── reporte_automatico_email.py # Main Logic (Sending)
    ├── config.py             # SMTP Credentials (IGNORED)
    └── README.md             # Project Documentation
```

---

## 5. Conclusions

This project demonstrates advanced mastery of:

* **Task Automation**: Ability to integrate communication services (email) into Python workflows.
* **Network Protocols**: Understanding and correct use of the SMTP protocol with TLS/SSL encryption.
* **Content Management**: Ability to construct complex messages using HTML formatting for a professional presentation.
* **Security and Best Practices**: Implementation of source code separation of secrets (*credentials*), a mandatory practice in professional development.
