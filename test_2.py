import tkinter as tk
from tkinter import messagebox
import requests

# Tu clave API de OpenWeather
API_KEY = "5506901f9bc1de3791078b7214f55778"

def obtener_clima():
    ciudad = entrada_ciudad.get()
    if not ciudad:
        messagebox.showwarning("Atención", "Por favor, ingresa una ciudad.")
        return

    url = f"http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={API_KEY}&units=metric&lang=es"
    respuesta = requests.get(url)
    datos = respuesta.json()

    if respuesta.status_code == 200:
        nombre = datos["name"]
        temp = datos["main"]["temp"]
        descripcion = datos["weather"][0]["description"]
        viento = datos["wind"]["speed"]

        resultado.config(text=f"📍 {nombre}\n🌡️ {temp}°C\n☁️ {descripcion}\n💨 Viento: {viento} m/s")
    else:
        messagebox.showerror("Error", "No se pudo obtener el clima. ¿Ciudad válida?")

# --- Interfaz ---
ventana = tk.Tk()
ventana.title("🌤️ Clima App por Pol Monsalvo")
ventana.geometry("300x300")
ventana.resizable(False, False)

tk.Label(ventana, text="Ingrese una ciudad:", font=("Arial", 12)).pack(pady=10)

entrada_ciudad = tk.Entry(ventana, font=("Arial", 12))
entrada_ciudad.pack(pady=5)

tk.Button(ventana, text="Consultar clima", command=obtener_clima, font=("Arial", 12)).pack(pady=10)

resultado = tk.Label(ventana, text="", font=("Arial", 12), justify="center")
resultado.pack(pady=10)

ventana.mainloop()
