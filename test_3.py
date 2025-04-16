import tkinter as tk
from tkinter import messagebox
import requests
import os
from dotenv import load_dotenv
import folium
import webbrowser

# Cargar clave API desde .env
load_dotenv()
API_KEY = os.getenv("API_KEY")

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
        lat = datos["coord"]["lat"]
        lon = datos["coord"]["lon"]

        # Mostrar resultado en la interfaz
        resultado.config(text=f"📍 {nombre}\n🌡️ {temp}°C\n☁️ {descripcion}\n💨 Viento: {viento} m/s")

        # Crear mapa con folium
        mapa = folium.Map(location=[lat, lon], zoom_start=12)
        folium.Marker([lat, lon], tooltip=f"📍 {nombre}", popup=f"{descripcion}, {temp}°C").add_to(mapa)

        # Guardar y abrir el mapa
        archivo_mapa = "mapa_clima.html"
        mapa.save(archivo_mapa)
        webbrowser.open(f"file://{os.path.abspath(archivo_mapa)}")

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
