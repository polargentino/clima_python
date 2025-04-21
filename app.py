from flask import Flask, render_template, request
import requests
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

API_KEY = os.getenv("API_KEY")

@app.route("/", methods=["GET", "POST"])
def clima():
    clima_data = None
    if request.method == "POST":
        ciudad = request.form.get("ciudad")
        if ciudad:
            url = f"https://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={API_KEY}&units=metric&lang=es"
            response = requests.get(url)
            if response.status_code == 200:
                datos = response.json()
                clima_data = {
                    "ciudad": datos["name"],
                    "pais": datos["sys"]["country"],
                    "temperatura": datos["main"]["temp"],
                    "descripcion": datos["weather"][0]["description"].capitalize(),
                    "icono": datos["weather"][0]["icon"]
                }
            else:
                clima_data = {"error": "Ciudad no encontrada o error con la API."}
    return render_template("index.html", clima=clima_data)

if __name__ == "__main__":
    app.run(debug=True)

'''
_python/app.py
 * Serving Flask app 'app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 639-827-319
127.0.0.1 - - [21/Apr/2025 17:17:37] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [21/Apr/2025 17:17:39] "GET /static/style.css HTTP/1.1" 200 -
127.0.0.1 - - [21/Apr/2025 17:17:40] "GET /favicon.ico HTTP/1.1" 404 -
127.0.0.1 - - [21/Apr/2025 17:18:06] "POST / HTTP/1.1" 200 -
127.0.0.1 - - [21/Apr/2025 17:18:12] "POST / HTTP/1.1" 200 -
127.0.0.1 - - [21/Apr/2025 17:18:12] "GET /static/style.css HTTP/1.1" 304 -
127.0.0.1 - - [21/Apr/2025 17:18:45] "POST / HTTP/1.1" 200 -
127.0.0.1 - - [21/Apr/2025 17:18:45] "GET /static/style.css HTTP/1.1" 304 -
127.0.0.1 - - [21/Apr/2025 17:22:18] "POST / HTTP/1.1" 200 -
127.0.0.1 - - [21/Apr/2025 17:22:18] "GET /static/style.css HTTP/1.1" 304 -
127.0.0.1 - - [21/Apr/2025 17:22:43] "POST / HTTP/1.1" 200 -
127.0.0.1 - - [21/Apr/2025 17:22:43] "GET /static/style.css HTTP/1.1" 304 -
'''
