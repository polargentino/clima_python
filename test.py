import requests
from dotenv import load_dotenv
import os

load_dotenv()  # Carga las variables del archivo .env

def obtener_clima(ciudad):
    api_key = os.getenv("API_KEY")
    url = f"http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}&units=metric&lang=es"
    respuesta = requests.get(url)
    datos = respuesta.json()

    if respuesta.status_code == 200:
        print(f"📍 Ciudad: {datos['name']}")
        print(f"🌡️ Temperatura: {datos['main']['temp']} °C")
        print(f"☁️ Condición: {datos['weather'][0]['description']}")
        print(f"💨 Viento: {datos['wind']['speed']} m/s")
    else:
        print("Error al obtener los datos del clima. Verifica la ciudad o tu clave API.")

# 🌎 Ciudad deseada
ciudad = "Buenos Aires"
obtener_clima(ciudad)

