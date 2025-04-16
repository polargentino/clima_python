import requests
from dotenv import load_dotenv
import os

# Carga la API key desde el archivo .env
load_dotenv()

def obtener_clima(ciudad):
    api_key = os.getenv("API_KEY")
    url = f"http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}&units=metric&lang=es"
    respuesta = requests.get(url)
    datos = respuesta.json()

    if respuesta.status_code == 200:
        print(f"\n📍 Ciudad: {datos['name']}")
        print(f"🌡️ Temperatura: {datos['main']['temp']} °C")
        print(f"☁️ Condición: {datos['weather'][0]['description']}")
        print(f"💨 Viento: {datos['wind']['speed']} m/s")
    else:
        print("\n❌ Error al obtener los datos del clima. Verifica la ciudad o tu clave API.")

# 👉 Entrada del usuario
ciudad = input("📌 Ingresá el nombre de una ciudad: ").strip()
obtener_clima(ciudad)

'''

📌 Ingresá el nombre de una ciudad: rio negro

📍 Ciudad: Rio Negro
🌡️ Temperatura: 17.85 °C
☁️ Condición: nubes
💨 Viento: 0.75 m/s
'''