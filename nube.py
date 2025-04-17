import requests
import smtplib
import os
from email.mime.text import MIMEText
from dotenv import load_dotenv

# Cargar variables desde .env
load_dotenv()

API_KEY = os.getenv("API_KEY")
EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASS = os.getenv("EMAIL_PASS")
DESTINATARIO = os.getenv("DESTINATARIO")

CIUDAD = "Monte vera"

def obtener_pronostico_extendido():
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={CIUDAD}&appid={API_KEY}&units=metric&lang=es"
    respuesta = requests.get(url)
    datos = respuesta.json()

    if respuesta.status_code != 200:
        return "❌ No se pudo obtener el pronóstico."

    pronostico = f"📍 Pronóstico extendido para {CIUDAD}:\n\n"
    for i in range(0, 40, 8):  # Cada 8 registros ~1 por día
        item = datos["list"][i]
        fecha = item["dt_txt"].split()[0]
        temp = item["main"]["temp"]
        desc = item["weather"][0]["description"]
        viento = item["wind"]["speed"]
        pronostico += f"📅 {fecha}\n🌡️ {temp}°C - ☁️ {desc} - 💨 Viento: {viento} m/s\n\n"
    
    return pronostico

def enviar_email(pronostico):
    mensaje = MIMEText(pronostico, "plain", "utf-8")
    mensaje["Subject"] = "🌦️ Pronóstico Extendido Diario"
    mensaje["From"] = EMAIL_USER
    mensaje["To"] = DESTINATARIO

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(EMAIL_USER, EMAIL_PASS)
            server.send_message(mensaje)
        print("✅ Email enviado con éxito.")
    except Exception as e:
        print("❌ Error al enviar el correo:", e)

# Ejecutar
pronostico = obtener_pronostico_extendido()
enviar_email(pronostico)
