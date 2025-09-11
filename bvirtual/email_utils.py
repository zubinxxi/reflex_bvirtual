import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Leer las variables de entorno
SENDER_EMAIL = os.getenv("EMAIL_SENDER")
SENDER_PASSWORD = os.getenv("EMAIL_PASSWORD")
SMTP_HOST = os.getenv("EMAIL_SERVER_HOST")
SMTP_PORT = os.getenv("EMAIL_SERVER_PORT") # Provee un valor por defecto si no existe

def send_password_reset_email(to_email: str, new_password: str):
    """
    Función para enviar un correo con la nueva contraseña.
    """
    if not SENDER_EMAIL or not SENDER_PASSWORD:
        print("Error: Las variables de entorno para el correo no están configuradas.")
        return False

    try:
        # Crea el mensaje de correo
        msg = MIMEMultipart("alternative")
        msg["Subject"] = "Recuperación de Contraseña"
        msg["From"] = SENDER_EMAIL
        msg["To"] = to_email

        text = f"Hola, tu nueva contraseña es: {new_password}\n\nPor favor, cámbiala lo antes posible."
        html = f"""\
        <html>
        <body>
            <p>Hola,</p>
            <p>Tu nueva contraseña es: <strong>{new_password}</strong></p>
            <p>Por favor, cambia tu contraseña lo antes posible por una que puedas recordar.</p>
        </body>
        </html>
        """
        part1 = MIMEText(text, "plain")
        part2 = MIMEText(html, "html")
        msg.attach(part1)
        msg.attach(part2)

        # Conéctate al servidor SMTP
        server = smtplib.SMTP(SMTP_HOST, SMTP_PORT)
        #server.set_debuglevel(1)  # Habilita el modo de depuración para ver la comunicación

        #server.ehlo()  # Identifica el cliente al servidor
        server.starttls() # Actualiza la conexión a TLS
        #server.ehlo() # Vuelve a identificar el cliente después de la actualización

        
        server.login(SENDER_EMAIL, SENDER_PASSWORD)

        # Envía el correo
        server.sendmail(SENDER_EMAIL, to_email, msg.as_string())
        server.quit()

        print(f"Correo enviado exitosamente a {to_email}")
        return True

    except Exception as e:
        print(f"Error al enviar el correo: {e}")
        return False