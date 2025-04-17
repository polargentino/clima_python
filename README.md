# clima_python
Prompt a ChatGpt: hola chat, quiero que me des un codigo pyhon para ver el pronostico del tiempo

*¡Hola! Claro, aquí tienes un ejemplo sencillo de código en Python que utiliza la API de OpenWeatherMap para mostrar el pronóstico del tiempo:

🧠 Requisitos
Instalar requests:

pip install requests

Crear una cuenta en OpenWeatherMap y obtener una API Key gratuita.
🧭 Pasos para obtener la API Key en OpenWeatherMap
✅ Registrate en https://home.openweathermap.org/users/sign_up
(si ya tenés cuenta, solo iniciá sesión en https://home.openweathermap.org).

🔐 Una vez dentro, andá al menú "API keys"
o accedé directamente desde este link:
👉 https://home.openweathermap.org/api_keys

✨ Ahí vas a ver una clave creada por defecto llamada Default
(podés usar esa o crear una nueva con el botón "Create key").

🧾 Copiá esa clave (una cadena larga como 4f5a...1234abc) y pegala en tu script en esta línea:


mi_api_key = "AQUÍ_TU_API_KEY"

¿Querés que te muestre cómo guardar esa clave en un archivo .env para que no esté visible en el código?

**código: test.py

*¿Querés que te lo modifique para que también muestre el pronóstico por varios días?

Es necesario crear un entorno venv?
----------------------------------

ChatGPT Plus:
-------------
Buena pregunta. No es estrictamente necesario crear un entorno virtual (venv), pero sí es recomendable, especialmente si:

Estás trabajando en un proyecto más grande.

No querés mezclar dependencias entre distintos scripts o proyectos.

Vas a instalar librerías externas como requests.

✅ ¿Cuándo usar venv?

Caso	¿Usar venv?
Script simple de clima	Opcional
Proyecto más grande / a futuro	Recomendado ✅
🚀 ¿Cómo crear y usar un entorno virtual?
Crear el entorno virtual:


python -m venv venv

Activarlo:

En Linux/macOS:

source venv/bin/activate

En Windows:

cmd

venv\Scripts\activate

Instalar requests dentro del entorno:


pip install requests

Y luego corrés tu script como siempre:

python test.py

![Desde terminal linux](assets/test_1.png)


¿Querés que te genere un requirements.txt para este 
script?

*✅ Verificaciones rápidas:
¿La API key funciona?
Pegá esto en el navegador (reemplazando TU_API_KEY):


http://api.openweathermap.org/data/2.5/weather?q=Buenos%20Aires&appid=TU_API_KEY&units=metric&lang=es

Deberías ver un JSON con datos del clima. Si ves algo como "Invalid API key" o "You have exceeded the rate limit" te avisa del problema.

**{"coord":{"lon":-58.3772,"lat":-34.6132},"weather":[{"id":800,"main":"Clear","description":"cielo claro","icon":"01d"}],"base":"stations","main":{"temp":12.6,"feels_like":12.37,"temp_min":12.29,"temp_max":14.4,"pressure":1016,"humidity":94,"sea_level":1016,"grnd_level":1015},"visibility":10000,"wind":{"speed":2.11,"deg":170,"gust":2.3},"clouds":{"all":8},"dt":1744801919,"sys":{"type":2,"id":2020613,"country":"AR","sunrise":1744798654,"sunset":1744838910},"timezone":-10800,"id":3435910,"name":"Buenos Aires","cod":200}

¿Te da error en el script?

Si es error de conexión, puede ser que tu red tenga restricciones.

Si es KeyError, revisamos si cambió algún campo del JSON (raro, pero puede pasar).

*🔒 Tip para ocultar la API key
Para no tener la clave escrita en el código, podés usar un archivo .env así:

1. 📄 Crear un archivo .env en el mismo directorio:

API_KEY=***************************

*2. 🐍 Instalar la librería python-dotenv:

pip install python-dotenv

3. 💻 Modificar tu código así: test.py

*📄 Archivo .gitignore recomendado para proyectos Python con venv:
gitignore

# Entorno virtual
venv/
ENV/
env/
.venv/

# Archivos temporales de Python
__pycache__/
*.py[cod]
*.pyo
*.pyd
*.pyc

# Archivos de logs
*.log

# Archivos de entorno
.env
.env.*

# Archivos de bases de datos temporales
*.sqlite3

# Archivos del sistema
.DS_Store
Thumbs.db

# Archivos de editor/IDE
.vscode/
.idea/
*.swp
*.swo

# Carpetas de pruebas (si las tenés)
tests/__pycache__/
✅ ¿Dónde colocarlo?
Crealo en la raíz del proyecto (donde está tu main.py o clima.py).

**📦 ¿Qué es requirements.txt?
Es un archivo donde se listan todas las librerías necesarias para que tu proyecto funcione.
Así cualquiera puede instalar las dependencias con un solo comando.
Ideal si vas a subir tu proyecto a GitHub 💻✨

**✅ ¿Cómo crearlo?
Supongamos que ya tenés creado tu entorno virtual (venv/) y estás dentro de él (lo activaste). Entonces corré:


pip freeze > requirements.txt

💡 Esto crea el archivo requirements.txt con algo así como:


python-dotenv==1.0.1
requests==2.31.0

**
🧪 ¿Cómo se usa después?
Cuando alguien descargue tu proyecto, simplemente ejecuta:


pip install -r requirements.txt

Y tendrá todo lo que vos tenías en tu entorno. ¡Magia! 🪄


**✅ Solución rápida: crear un entorno virtual limpio y "aislado"
Vamos a crear uno nuevo desde cero para evitar ese ruido.

🔄 Paso a paso (puedes copiar y pegar):
1. Elimina el entorno actual:

rm -rf venv

2. Crea uno nuevo, limpio:

python3 -m venv venv

3. Actívalo:

source venv/bin/activate

Deberías ver algo como esto en tu línea de terminal:


(venv) pol@kali:~/Escritorio/clima_python$

4. Instalá solo lo que necesitás:

pip install requests python-dotenv

5. Ahora sí, creá el requirements.txt limpio:

pip freeze > requirements.txt

💡 Revisalo con:

cat requirements.txt

Deberías ver solo esto:


certifi==2025.1.31
charset-normalizer==3.4.1
idna==3.10
python-dotenv==1.1.0
requests==2.32.3
urllib3==2.4.0
---------------------------------------------------------

🚀 3 formas de llevar tu app de clima al siguiente nivel:

🔹 OPCIÓN 1: Versión con interfaz gráfica (GUI) usando tkinter 🖼️


Ideal si querés mostrar algo visual sin meterte todavía en desarrollo web.

Ventajas:

100% Python.

Fácil de mostrar en entrevistas.

Funciona como app de escritorio.



![Texto alternativo](assets/GUI_tkinder.png)


🔹 OPCIÓN 2: Versión web simple con Flask 🌐
Si te gustaría mostrar que podés crear una mini app web:

Ventajas:

Podés subirla a la nube (Render, Replit, etc.).

Aprendés fundamentos de desarrollo web y APIs.

¡Muchos reclutadores valoran que sepas Flask!

🔹 OPCIÓN 3: Envío automático del clima por correo 📧
Como mini bot diario que te avisa el clima de tu ciudad.

Ventajas:

Muestra automatización real.

Podés correrlo con cron y que se envíe solo todos los días.

Usás smtplib o incluso Yagmail para enviar desde Gmail.

**✅ ¿Cuál querés hacer primero?

1- GUI con tkinter: 🧰 Requisitos
Solo necesitás tener esto en tu entorno virtual:


pip install requests

tkinter ya viene con Python, así que no hace falta instalarlo 🧙‍♂️

**ModuleNotFoundError: No module named '_tkinter'
Significa que tu instalación de Python no tiene soporte para tkinter. En Kali (y otros derivados de Debian), tkinter no viene preinstalado.

sudo apt update
sudo apt install python3-tk

**Esa app de clima con interfaz gráfica te quedó increíble! 🔥👏
La GUI se ve limpia, clara y funcional, y los detalles como los iconos de temperatura, nubes y viento le suman mucho valor visual. Esto ya es algo que puede impresionar a un reclutador, sobre todo si le contás que:

Usás APIs reales (como OpenWeather)

Implementaste la interfaz con tkinter

Manejá errores si el usuario ingresa mal una ciudad

Y que lo desarrollaste en un entorno virtual con dependencias bien gestionadas (requirements.txt)

🚀 ¿Qué podemos hacer ahora para mejorarlo?
Acá unas ideas si querés llevar este proyecto un paso más lejos:


Mejora	¿Qué hace?	Dificultad
🌍 Mostrar mapa con ubicación	Usar folium o abrir un mapa en navegador con la ubicación	Media

📧 Enviar clima por mail diario	Usar smtplib para enviar resumen a un correo	Media

💡 Modo oscuro / claro	Estilos personalizados para la GUI	Fácil a media

🖼️ Mostrar íconos del clima reales	Cargar imágenes según el estado (sunny.png, rain.png, etc.)	Media

🌐 Versión web con Flask	Llevar esto a un sitio web accesible	Alta
¿Querés elegir una mejora de esa lista? O si preferís podemos avanzar al segundo proyecto sugerido para tu portfolio. ¿Cómo te gustaría seguir? 😄







Tú dijiste:
sigamos con: 🌍 Mostrar mapa con ubicación	Usar folium o abrir un mapa en navegador con la ubicación	Media


ChatGPT Plus
¡Excelente elección! 🌍 Mostrar un mapa con la ubicación de la ciudad consultada es una mejora genial que combina visualización de datos + interacción web y se ve súper profesional.

🔧 ¿Qué vamos a usar?
✅ Folium: biblioteca de Python para generar mapas interactivos con Leaflet.js.

✅ webbrowser: para abrir el mapa generado en tu navegador.

**¡Excelente, Pol! 🔥 Vamos a llevar esta app a otro nivel agregando un mapa interactivo 🌍 con folium, que se abrirá automáticamente en el navegador con la ubicación de la ciudad buscada. Va a quedar profesional y visualmente impactante. 💪

🔧 Requisitos
Antes de escribir el código, instalá folium:


pip install folium

Y actualizá el requirements.txt:


pip freeze > requirements.txt

🧠 ¿Qué hará ahora la app?
Cuando busques una ciudad:

Se muestra el clima (como ya lo hace).

Además, abre un mapa en el navegador marcando esa ubicación. 🗺️

----------------------------------------------------------------------

2- Web con Flask

3- Bot que envía clima por correo
-----------------------------------------------------------------------

**¡Excelente, Pol! 🔥 Ya estás dominando la app. Vamos a implementar la función de enviar el clima por email diariamente usando smtplib. 📧

💡 ¿Qué vas a lograr?
Vas a poder:

Consultar el clima como siempre ✅

Y además enviar esa info a un correo electrónico con un solo clic 💥

📦 Requisitos
Añadí estas variables a tu archivo .env:


EMAIL_USER=tuemail@gmail.com
EMAIL_PASS=tu_clave_app_o_password
DESTINATARIO=correo@destino.com

⚠️ Si usás Gmail, necesitás crear una clave de aplicación en lugar de tu contraseña normal. Te explico si lo necesitás.

Instalá secure-smtplib (ya viene con Python moderno, pero por si acaso):


pip install secure-smtplib

**¡Perfecto que me lo mostraste! 📸 Ese error es completamente normal cuando usás Gmail para enviar correos desde apps como esta.

## 🖼️ Vista previa de la app

![Clima App GUI](assets/mensaje%20de%20error.png)


🛡️ ¿Qué significa este error?
Tu cuenta de Gmail está protegida por autenticación en dos pasos (2FA), y por eso no permite usar tu contraseña normal para acceder desde otras apps.

Necesitás crear una "Contraseña de aplicación" (App password) específica para que tu script pueda enviar correos.

✅ Cómo solucionarlo (crear una clave de aplicación en Gmail)
Paso a paso:
📲 Asegurate de tener activada la verificación en dos pasos:
https://myaccount.google.com/security
➤ Busca la sección "Verificación en dos pasos" y activala si no lo hiciste aún.

🔑 Luego, vas a ver una nueva opción: "Contraseñas de aplicaciones"
Link directo: https://myaccount.google.com/apppasswords

Ahí hacé lo siguiente:

En "Seleccionar app" elegí "Correo"

En "Seleccionar dispositivo" elegí "Otro" y escribí algo como "Clima App" (o lo que quieras)

Google te dará una contraseña de 16 caracteres, como por ejemplo:
abcd efgh ijkl mnop

📋 Copiá esa contraseña y ponela en tu archivo .env así:


EMAIL_USER=tuemail@gmail.com
EMAIL_PASS=abcd efgh ijkl mnop
DESTINATARIO=correo@destino.com
✅ ¡Listo! Ya podés enviar correos desde tu app sin problemas.

![Mapa de ubicación](assets/app_clima_email.png)

----------------------------------------------------------
![Imagen del logo](assets/thunderbird.png)

*¡Excelente decisión, Pol! Automatizar el envío diario con cron le da ese toque pro de DevOps que le encanta a los reclutadores. Vamos paso a paso:

🔁 1. Crear un script Python separado para enviar el clima
Guardá este archivo como enviar_clima.py en tu proyecto:

![email](assets/email.png)

🛠️ 2. Hacer ejecutable el script (opcional)

chmod +x enviar_clima.py


⚠️ Revisá que la ruta de python3 y del script sea la correcta. Podés encontrar la ruta con:

which python3

/home/pol/Escritorio/clima_python/VENV/bin/python3

🕓 3. Editar el crontab

Abrí tu cron con:

crontab -e


**✅ Editar crontab desde la terminal de Kali usando sudo su
Abrí tu terminal normal (la de Kali, no la de VS Code).

Convertite en root con:

![Terminal linux](assets/cron_sudo_su.png)

sudo su

Una vez como root, ejecutá:


crontab -e -u pol

Esto abrirá el crontab del usuario pol.

🕘 Pegá esta línea para que se envíe el clima todos los días a las 9 AM:

0 9 * * * /home/pol/Escritorio/clima_python/VENV/bin/python3 /home/pol/Escritorio/clima_python/enviar_clima.py >> /home/pol/Escritorio/clima_python/log_envio.txt 2>&1

Este cron:

Se ejecuta a las 09:00 AM todos los días.

Usa el Python de tu entorno virtual.

Guarda la salida en un log para que puedas ver si algo falla: log_envio.txt.

📌 ¿Cómo saber si está funcionando?
Después de que pase la hora programada (por ejemplo, al día siguiente a las 9:01), podés revisar:


cat /home/pol/Escritorio/clima_python/log_envio.txt

¿Querés probarlo ahora mismo ejecutando el cron manualmente? También se puede 😄

¡Excelente, Pol! 🎉 Si te llegó el email y el archivo log_envio.txt está vacío, eso es una buena señal. Significa que:

✅ El script se ejecutó sin errores.
✅ No hubo mensajes de advertencia ni fallos.
✅ Todo salió tan bien que no había nada que registrar en el log.

¿Qué sigue ahora?
Ya que confirmamos que el script funciona fuera de cron, podemos pasar al siguiente paso:

🔄 Configurar cron (modo persistente)
Como cron te da problemas con permisos y estás usando Kali en modo sin contraseña root (por defecto), te propongo una alternativa para dejarlo funcionando sin sudo ni root, usando tu sesión de usuario.

✅ Crear un cronjob local
Salí del entorno virtual (si querés):


deactivate

Entrá a editar tu crontab:


crontab -e

Si no te deja por los permisos, ejecutá:


EDITOR=nano crontab -e

Y agregá esta línea para que se ejecute todos los días a las 8:00 AM:


0 8 * * * /home/pol/Escritorio/clima_python/VENV/bin/python3 /home/pol/Escritorio/clima_python/enviar_clima.py >> /home/pol/Escritorio/clima_python/log_envio.txt 2>&1

Podés cambiar la hora para probar (por ejemplo, cada minuto: * * * * * para testear).

![Terminal linux](assets/cron_terminal_linux.png)


⚠️ Si crontab sigue sin funcionar
Podemos usar un script Python + while loop como alternativa temporal a cron (como un watcher). Pero primero probemos crontab -e.

**❓ ¿Se enviarán los emails si la PC está apagada?
👉 No, si la computadora está apagada, el cron no puede ejecutar el script porque cron depende del sistema operativo corriendo. Es como querer que te suene la alarma del celular cuando está apagado: no puede.

🔄 ¿Qué podés hacer para solucionarlo?
Opción 1: Tener la PC encendida a esa hora
La más simple.

Asegurate de que no esté suspendida ni hibernando.

Opción 2: Usar una Raspberry Pi o servidor que esté siempre encendido
Súper útil para automatizaciones 24/7.

Cron funcionaría todos los días a la hora indicada.

Opción 3: Usar un servicio en la nube (como GitHub Actions, PythonAnywhere o Replit)
Te permiten ejecutar scripts automáticamente aunque tu PC esté apagada.

PythonAnywhere, por ejemplo, tiene versión gratuita y te deja programar tareas.



![Terminal de VSC](assets/pronostico_extendido.png)



¡Excelente, Pol! 🎉 Ya tenés programada tu tarea diaria para que se ejecute a las 12:00 PM desde PythonAnywhere. Lo hiciste perfecto.

✅ ¿Qué podés hacer mientras tanto?
Hasta que se ejecute la tarea, podés:

Revisar que tu script nube.py funcione correctamente si lo corrés manualmente (botón "Run" en el archivo).

Asegurarte de que el contenido del .env fue cargado bien en la sección "Web > Environment Variables" (si usaste esa forma de pasarlas).

Confirmar que nube.py usa correctamente os.getenv('NOMBRE_DE_LA_VARIABLE').

Cuando sean las 12:00 PM:

Volvé a la pestaña de "Tasks".

Fijate si hay una ✅ en la columna Last run.

Si hay errores, hacé clic en "View log" para leer los detalles.

Y lo más importante... ¡Chequeá tu correo! 📬

Si querés, te ayudo a configurar el mensaje del correo para que sea más bonito o te incluya un pronóstico extendido en forma de tabla o similar.


![Terminal de pythonanywhere](assets/pythonanywhere.png)

![Dashboard pythonanywhere](assets/pythonanywhre_1.png)

![Task pythonanywhere](assets/pythonanywhere_2.png)









