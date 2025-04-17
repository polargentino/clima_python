from dotenv import load_dotenv
import os
import smtplib
from email.message import EmailMessage
import requests

# Cargar variables de entorno
load_dotenv()

API_KEY = os.getenv("API_KEY")
EMAIL = os.getenv("EMAIL_USER")
EMAIL_PASSWORD = os.getenv("EMAIL_PASS")
DESTINATARIO = os.getenv("DESTINATARIO")
CIUDAD = "Monte vera"  # podés modificarla o pasarla como variable también

def obtener_clima(ciudad):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={API_KEY}&units=metric&lang=es"
    respuesta = requests.get(url)
    datos = respuesta.json()

    if respuesta.status_code == 200:
        nombre = datos["name"]
        temp = datos["main"]["temp"]
        descripcion = datos["weather"][0]["description"]
        viento = datos["wind"]["speed"]
        return f"📍 {nombre}\n🌡️ {temp}°C\n☁️ {descripcion}\n💨 Viento: {viento} m/s"
    else:
        return "❌ No se pudo obtener el clima."

def enviar_mail(mensaje):
    correo = EmailMessage()
    correo.set_content(mensaje)
    correo["Subject"] = "☀️ Clima diario"
    correo["From"] = EMAIL
    correo["To"] = DESTINATARIO

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(EMAIL, EMAIL_PASSWORD)
        smtp.send_message(correo)

if __name__ == "__main__":
    resumen_clima = obtener_clima(CIUDAD)
    enviar_mail(resumen_clima)