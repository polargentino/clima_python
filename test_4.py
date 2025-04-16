import tkinter as tk
from tkinter import messagebox
import requests
import os
import smtplib
from dotenv import load_dotenv
import folium
import webbrowser
from email.message import EmailMessage

# Cargar variables del entorno
load_dotenv()
API_KEY = os.getenv("API_KEY")
EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASS = os.getenv("EMAIL_PASS")
DESTINATARIO = os.getenv("DESTINATARIO")

# Variables globales para almacenar últimos datos
info_clima = ""

def obtener_clima():
    global info_clima

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

        # Info en pantalla
        info_clima = f"📍 {nombre}\n🌡️ {temp}°C\n☁️ {descripcion}\n💨 Viento: {viento} m/s"
        resultado.config(text=info_clima)

        # Mostrar botón para enviar
        boton_enviar.pack(pady=5)

        # Crear y abrir mapa
        mapa = folium.Map(location=[lat, lon], zoom_start=12)
        folium.Marker([lat, lon], tooltip=f"📍 {nombre}", popup=f"{descripcion}, {temp}°C").add_to(mapa)
        archivo_mapa = "mapa_clima.html"
        mapa.save(archivo_mapa)
        webbrowser.open(f"file://{os.path.abspath(archivo_mapa)}")

    else:
        messagebox.showerror("Error", "No se pudo obtener el clima. ¿Ciudad válida?")

def enviar_por_mail():
    if not info_clima:
        messagebox.showwarning("Atención", "Primero consulta el clima.")
        return

    try:
        mensaje = EmailMessage()
        mensaje["Subject"] = "🌤️ Clima del día"
        mensaje["From"] = EMAIL_USER
        mensaje["To"] = DESTINATARIO
        mensaje.set_content(info_clima)

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(EMAIL_USER, EMAIL_PASS)
            smtp.send_message(mensaje)

        messagebox.showinfo("Enviado", "📩 El clima fue enviado exitosamente.")
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo enviar el mail: {e}")

# --- Interfaz ---
ventana = tk.Tk()
ventana.title("🌤️ Clima App por Pol Monsalvo")
ventana.geometry("300x350")
ventana.resizable(False, False)

tk.Label(ventana, text="Ingrese una ciudad:", font=("Arial", 12)).pack(pady=10)
entrada_ciudad = tk.Entry(ventana, font=("Arial", 12))
entrada_ciudad.pack(pady=5)
tk.Button(ventana, text="Consultar clima", command=obtener_clima, font=("Arial", 12)).pack(pady=10)

resultado = tk.Label(ventana, text="", font=("Arial", 12), justify="center")
resultado.pack(pady=10)

# Botón oculto al inicio
boton_enviar = tk.Button(ventana, text="📧 Enviar por mail", command=enviar_por_mail, font=("Arial", 12))

ventana.mainloop()
