# 🌧️ Proyecto: Clima en Python

Este proyecto es una aplicación en Python para consultar el pronóstico del clima utilizando la API de OpenWeatherMap. Ideal para practicar conceptos de APIs, entornos virtuales, interfaces gráficas, y visualización de datos.

---

## 🔎 Objetivo
Desarrollar una aplicación que, ingresando una ciudad, muestre su estado del clima actual y lo complemente con visualizaciones como una GUI o un mapa interactivo.

---

## 🧪 Requisitos
- Python 3.x
- Librerías:
  - `requests`
  - `python-dotenv`
  - `folium` (opcional para la visualización del mapa)
  - `tkinter` (para GUI)

Instalá las dependencias con:
```bash
pip install -r requirements.txt
```

---

## 🔢 Instalación
1. Cloná el repositorio:
```bash
git clone https://github.com/tu-usuario/clima_python.git
cd clima_python
```

2. Creá y activá el entorno virtual:
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate    # Windows
```

3. Instalá las dependencias:
```bash
pip install -r requirements.txt
```

---

## 🔐 API Key
1. Registrate gratis en [OpenWeatherMap](https://home.openweathermap.org/users/sign_up).
2. Obtené tu API Key desde [API Keys](https://home.openweathermap.org/api_keys).
3. Creá un archivo `.env` en la raíz del proyecto:
```env
API_KEY=TU_API_KEY
```

---

## 📁 Estructura del Proyecto
```
clima_python/
├── assets/                 # Imágenes y recursos
├── test.py                 # Script principal (versión CLI)
├── clima_gui.py            # Versión con interfaz gráfica tkinter
├── mapa.py                 # Visualización en mapa con folium
├── .env                    # Clave de API (no subir al repo)
├── .gitignore              # Archivos ignorados por git
├── requirements.txt        # Dependencias del proyecto
```

---

## 🎨 Opciones de visualización
### 1. Consola (CLI)
Ejecutá `test.py` y mostrá los datos del clima en la terminal.

### 2. GUI con Tkinter 💻

Ventajas:
- 100% Python
- Visual
- Ideal para entrevistas

Ejecutá:
```bash
python clima_gui.py
```

![Captura GUI](assets/GUI_tkinder.png)

### 3. Mapa interactivo 🌍 con Folium

Muestra la ubicación de la ciudad consultada en un mapa.

```bash
python mapa.py
```

Esto abrirá un navegador con el mapa generado. Usamos:
- `folium`
- `webbrowser`

---

## 🚫 Evitá subir datos sensibles
Agregá esto a tu `.gitignore`:
```gitignore
.env
venv/
__pycache__/
*.pyc
*.log
```

---

## 🌟 Mejoras implementadas
| Mejora                           | Descripción                                                  | Dificultad |
|----------------------------------|--------------------------------------------------------------|------------|
| Ocultar API Key (.env)           | Seguridad en el código                                       | Fácil      |
| Interfaz gráfica con tkinter     | Versión de escritorio amigable                              | Media      |
| Requisitos en requirements.txt   | Entorno replicable                                           | Fácil      |
| Mapa con ubicación (folium)      | Visualización profesional de datos geográficos              | Media      |

---

## 🚀 Ideas para futuras mejoras
| Mejora                           | Tecnología                       | Impacto Visual / Técnico |
|----------------------------------|----------------------------------|--------------------------|
| Enviar clima por mail diario     | smtplib / yagmail + cron         | Alta                     |
| Modo oscuro / claro              | Estilos en tkinter               | Media                    |
| Mostrar íconos del clima reales | Carga dinámica de imágenes PNG    | Media                    |
| Publicar versión web             | Flask / Render / Replit          | Alta                     |

---

## 🏙️ Deployment (Próximamente)
Subida a Render o Replit como versión web de la app.

---

## 📈 Tecnologías utilizadas
- Python 3
- OpenWeatherMap API
- tkinter (GUI)
- folium (mapas)
- dotenv
- requests

---

## 🎓 Autor
**Pol** – [GitHub](https://github.com/tu-usuario)

---

## 🙌 Contribuciones
Ideas, mejoras o errores detectados son bienvenidos. ¡Forkeá y enviá tu PR!

---

## ✨ Agradecimientos
Gracias a ChatGPT por colaborar con los snippets de código, sugerencias de buenas prácticas y mejoras progresivas del proyecto.

---

> Este README se actualiza junto al progreso del proyecto para reflejar nuevas funcionalidades e integraciones. 🚀

