#!/data/data/com.termux/files/usr/bin/env python3

#Diccionario

paquetes = {
    "sistema": {
        "git": "pkg install git",
        "nano": "pkg install nano",
        "vim": "pkg install vim",
        "htop": "pkg install htop",
        "tree": "pkg install tree",
        "neofetch": "pkg install neofetch",
        "tsu": "pkg install tsu",
    },
    "red": {
       "curl": "pkg install curl",
       "wget": "pkg install wget",
       "openssh": "pkg install openssh",
       "nmap": "pkg install nmap",
       "tor": "pkg install tor",
    },
    "lenguaje": {
        "nodejs": "pkg install nodejs",
        "golang": "pkg install golang",
        "rust": "pkg install rust",
        "ruby": "pkg install ruby",
        "php": "pkg install php",
        "clang": "pkg install clang",
        "make": "pkg install make",
        "cmake": "pkg install cmake",
    },
    "bases de datos": {
        "sqlite": "pkg install sqlite",
        "mariadb": "pkg install mariadb",
        "postgresql": "pkg install postgresql",
        "sqlalchemy": "pip install sqlalchemy",
        "pymongo": "pip install pymongo",
        "redis": "pip install redis",
    },
    "servidores": {
        "nginx": "pkg install nginx",
        "apache2": "pkg install apache2",
        "lighttpd": "pkg install lighttpd",
        "caddy": "pkg install caddy",
        "gunicorn": "pip install gunicorn",
        "uvicorn": "pip install uvicorn",
    },
    "multimedia": {
        "ffmpeg": "pkg install ffmpeg",
        "imagemagick": "pkg install imagemagick",
        "pillow": "pip install pillow",
        "opencv-python": "pip install opencv-python",
    },
    "formatos": {
        "hbf-hyper": "pip install hbf-hyper",
        "pyyaml": "pip install pyyaml",
        "xmltodict": "pip install xmltodict",
        "openpyxl": "pip install openpyxl",
        "pypdf": "pip install pypdf",
        "python-docx": "pip install python-docx",
        "fpdf2": "pip install fpdf2",
    },
    "diversion": {
        "cmatrix": "pkg install cmatrix",
        "sl": "pkg install sl",
        "cowsay": "pkg install cowsay",
        "fortune": "pkg install fortune",
        "figlet": "pkg install figlet",
        "toilet": "pkg install toilet",
    },
    "datos": {
        "numpy": "pip install numpy",
        "pandas": "pip install pandas",
        "matplotlib": "pip install matplotlib",
        "seaborn": "pip install seaborn",
        "scipy": "pip install scipy",
    },
    "web": {
        "requests": "pip install requests",
        "flask": "pip install flask",
        "django": "pip install django",
        "fastapi": "pip install fastapi",
        "beautifulsoup4": "pip install beautifulsoup4",
        "scrapy": "pip install scrapy",
        "selenium": "pip install selenium",
    },
    "machine learning": {
        "scikit-learn": "pip install scikit-learn",
        "tensorflow": "pip install tensorflow",
        "torch": "pip install torch",
        "keras": "pip install keras",
    },
    "utilidades": {
        "tqdm": "pip install tqdm",
        "pyfiglet": "pip install pyfiglet",
        "emoji": "pip install emoji",
        "faker": "pip install faker",
        "python-dotenv": "pip install python-dotenv",
        "termcolor": "pip install termcolor",
        "pygments": "pip install pygments",
        "art": "pip install art",
        "humanize": "pip install humanize",
        "validators": "pip install validators",
        "python-slugify": "pip install python-slugify",
    },
    "seguridad": {
        "cryptography": "pip install cryptography",
        "bcrypt": "pip install bcrypt",
        "pyjwt": "pip install pyjwt",
        "passlib": "pip install passlib",
        "itsdangerous": "pip install itsdangerous",
        "pyopenssl": "pip install pyopenssl",
    },
    "testing": {
        "pytest": "pip install pytest",
        "tox": "pip install tox",
        "coverage": "pip install coverage",
        "pytest-cov": "pip install pytest-cov",
        "hypothesis": "pip install hypothesis",
    },
    "automatizacion": {
        "pyautogui": "pip install pyautogui",
        "keyboard": "pip install keyboard",
        "pynput": "pip install pynput",
        "psutil": "pip install psutil",
    },
    "publicacion": {
        "twine": "pip install twine",
        "build": "pip install build",
        "wheel": "pip install wheel",
        "setuptools": "pip install setuptools",
        "pip-tools": "pip install pip-tools",
        "bump2version": "pip install bump2version",
        "hatch": "pip install hatch",
        "poetry": "pip install poetry",
    },
    "GUI": {
        "kivy": "pip install kivy",
        "customtkinter": "pip install customtkinter",
        "pyqt5": "pip install pyqt5",
        "pyside6": "pip install pyside6",
    },
    "juegos": {
        "pygame": "pip install pygame",
        "arcade": "pip install arcade",
        "pyglet": "pip install pyglet",
    },
    "CLI": {
        "click": "pip install click",
        "typer": "pip install typer",
        "rich": "pip install rich",
        "colorama": "pip install colorama",
        "tabulate": "pip install tabulate",
    },
    "ciencia": {
        "sympy": "pip install sympy",
        "nltk": "pip install nltk",
        "spacy": "pip install spacy",
        "biopython": "pip install biopython",
        "astropy": "pip install astropy",
    },
    "Cloud": {
        "boto3": "pip install boto3",
        "google-cloud-storage": "pip install google-cloud-storage",
        "azure-storage-blob": "pip install azure-storage-blob",
    },
    "fechas": {
        "arrow": "pip install arrow",
        "pendulum": "pip install pendulum",
        "python-dateutil": "pip install python-dateutil",
        "pytz": "pip install pytz",
    },
}


#Menu

print("—————————————————————Vlsy46———————————————————————")
print("version: 1.0.1")
print("Creado por Lucas Sogaray")

while True:

    print("\nCategorías disponibles:\n")
    categorias = list(paquetes.keys())
    for i, categoria in enumerate(categorias, start=1):
        print(f"{i}. {categoria}")
    print("0. Salir")

    try:
        opcion = int(input("\nElige una categoría: "))
    except ValueError:
        print("Escribe un número, por favor.")
        continue

    if opcion == 0:
        print("¡Hasta luego!")
        break

    if 1 <= opcion <= len(categorias):
        categoria_elegida = categorias[opcion - 1]
        print(f"\n=== {categoria_elegida.upper()} ===\n")
        for nombre, comando in paquetes[categoria_elegida].items():
            print(f"- {nombre}: {comando}")
        input("\nPresiona Enter para volver al menú...")
    else:
        print("Opción no válida.")
