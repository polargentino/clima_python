from flask import Flask, render_template, request
import requests
import os
import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv
from datetime import datetime

# Cargar variables del archivo .env
load_dotenv()

app = Flask(__name__)

# Clave de la API del clima y configuración de email
API_KEY = os.getenv("API_KEY")
EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASS = os.getenv("EMAIL_PASS")
DESTINATARIO = os.getenv("DESTINATARIO")


def get_weather(city):
    """Llama a la API de OpenWeather y devuelve datos relevantes"""
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric&lang=es"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        clima = {
            'ciudad': data['name'],
            'pais': data['sys']['country'],
            'temp': data['main']['temp'],
            'descripcion': data['weather'][0]['description'],
            'icono': data['weather'][0]['icon'],
            'sensacion': data['main']['feels_like'],
            'humedad': data['main']['humidity'],
            'viento': data['wind']['speed']
        }
        return clima
    return None


def enviar_email(clima):
    """Envía el resumen del clima por correo electrónico"""
    cuerpo = (
        f"Clima actual en {clima['ciudad']}, {clima['pais']}:\n"
        f"Temperatura: {clima['temp']}°C\n"
        f"Descripción: {clima['descripcion']}\n"
        f"Sensación térmica: {clima['sensacion']}°C\n"
        f"Humedad: {clima['humedad']}%\n"
        f"Viento: {clima['viento']} m/s"
    )
    mensaje = MIMEText(cuerpo)
    mensaje["Subject"] = f"Clima en {clima['ciudad']} 🌤️"
    mensaje["From"] = EMAIL_USER
    mensaje["To"] = DESTINATARIO

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as servidor:
        servidor.login(EMAIL_USER, EMAIL_PASS)
        servidor.send_message(mensaje)


def guardar_historial(ciudad):
    """Guarda la ciudad buscada con fecha y hora en historial.txt"""
    ahora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("historial.txt", "a") as f:
        f.write(f"{ahora} - {ciudad}\n")


@app.route("/", methods=["GET", "POST"])
def index():
    clima = None
    enviado = False

    if request.method == "POST":
        ciudad = request.form.get("ciudad")
        accion = request.form.get("accion")

        clima = get_weather(ciudad)
        if clima:
            guardar_historial(ciudad)  # ✅ Guardar historial

            if accion == "email":
                enviar_email(clima)     # ✅ Enviar email
                enviado = True

    return render_template("index_1.html", clima=clima, enviado=enviado)

if __name__ == "__main__":
    app.run(debug=True)
