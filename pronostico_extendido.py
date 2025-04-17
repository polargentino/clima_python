import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")

def obtener_pronostico(ciudad):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={ciudad}&appid={API_KEY}&units=metric&lang=es"
    respuesta = requests.get(url)
    
    if respuesta.status_code != 200:
        print("❌ Error al obtener el pronóstico.")
        return

    datos = respuesta.json()
    print(f"📍 Pronóstico extendido para {ciudad}:\n")
    
    # Muestra un resumen cada 8 horas (8 x 3h = 24h)
    for i in range(0, len(datos["list"]), 8):
        dia = datos["list"][i]
        fecha = dia["dt_txt"]
        temp = dia["main"]["temp"]
        clima = dia["weather"][0]["description"]
        print(f"📅 {fecha}")
        print(f"🌡️ Temp: {temp}°C")
        print(f"☁️ Clima: {clima}\n")

if __name__ == "__main__":
    ciudad = input("🔍 Ingrese la ciudad: ")
    obtener_pronostico(ciudad)

