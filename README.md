Vlsy46 es una herramienta de línea de comandos escrita en Python que funciona como un catálogo organizado de comandos de instalación para Termux y Python. Permite consultar rápidamente el comando necesario para instalar paquetes agrupados por categorías como redes, lenguajes, bases de datos, machine learning, seguridad, entre muchas otras.

· Versión: 1.0.2
· Autor: Lucas Sogaray

---

📋 Descripción

Vlsy46 presenta un menú interactivo en consola donde el usuario elige una categoría y obtiene una lista de paquetes junto con el comando exacto para instalarlos.

---

🚀 Instalación y uso

1. Ejecutar:
   
   python3 Vlsy46.py

   o directamente:
   vlsy46
   
5. Selecciona una categoría ingresando su número y presiona Enter.
6. Para salir, elige la opción 0.

---

🗂️ Categorías disponibles

Categoría Descripción
sistema Herramientas básicas del sistema (git, nano, vim, htop, etc.)
red Utilidades de red (curl, wget, openssh, nmap, tor)
lenguaje Lenguajes de programación (nodejs, golang, rust, ruby, php, etc.)
bases de datos SQLite, MariaDB, PostgreSQL y clientes Python
servidores Nginx, Apache, Lighttpd, Caddy, Gunicorn, Uvicorn
multimedia FFmpeg, ImageMagick, Pillow, OpenCV
formatos Manejo de YAML, XML, Excel, PDF, DOCX, etc.
diversion Comandos de entretenimiento (cmatrix, sl, cowsay, figlet...)
datos NumPy, Pandas, Matplotlib, Seaborn, SciPy
web Requests, Flask, Django, FastAPI, Scrapy, Selenium
machine learning Scikit-learn, TensorFlow, Torch, Keras
utilidades Tqdm, PyFiglet, Faker, Rich, Pygments, etc.
seguridad Cryptography, Bcrypt, PyJWT, Passlib, PyOpenSSL
testing Pytest, Tox, Coverage, Hypothesis
automatizacion PyAutoGUI, Keyboard, Pynput, Psutil
publicacion Twine, Build, Wheel, Poetry, Hatch
GUI Kivy, CustomTkinter, PyQt5, PySide6
juegos Pygame, Arcade, Pyglet
CLI Click, Typer, Rich, Colorama, Tabulate
ciencia SymPy, NLTK, spaCy, Biopython, Astropy
Cloud Boto3, Google Cloud Storage, Azure Storage Blob
fechas Arrow, Pendulum, Python-DateUtil, PyTZ

#129 paquetes en total.

---

🖥️ Ejemplo de uso

```
—————————————————————Vlsy46———————————————————————
version: 1.0.2
Creado por Lucas Sogaray

Categorías disponibles:

1. sistema
2. red
3. lenguaje
...
0. Salir

Elige una categoría: 2

=== RED ===

- curl: pkg install curl
- wget: pkg install wget
- openssh: pkg install openssh
- nmap: pkg install nmap
- tor: pkg install tor

Presiona Enter para volver al menú...
```

---

🛠️ Estructura del código

El programa se basa en un diccionario anidado llamado paquetes, donde:

· La clave externa es el nombre de la categoría.
· El valor es otro diccionario con nombre_paquete: comando_de_instalación.

El menú recorre dinámicamente las claves del diccionario, por lo que agregar nuevas categorías o paquetes es tan simple como editar el diccionario.

Ejemplo de extensión

paquetes["nueva_categoria"] = {
    "paquete1": "pkg install paquete1",
    "paquete2": "pip install paquete2",
}


---

⚠️ Notas

· Los comandos no se ejecutan automáticamente; el script solo los muestra para que el usuario los copie y ejecute manualmente.

---

📄 Licencia

MIT licence - ✨

---

👤 Autor

Lucas Sogaray
Versión 1.0.2
