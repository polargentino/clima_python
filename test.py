import requests

def obtener_clima(ciudad, api_key):
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

# 🔧 Personaliza esto
mi_api_key = "TU_API_KEY_AQUÍ"
ciudad = "Buenos Aires"

obtener_clima(ciudad, mi_api_key)
