# Vlsy46

Vlsy46 es una herramienta de línea de comandos escrita en Python que funciona como un catálogo interactivo de paquetes y comandos de instalación para Termux. Organiza los paquetes por categorías y permite consultar sus comandos sin tener que recordar su sintaxis.

- **Versión:** 1.2.0
- **Autor:** Lucas Sogaray
- **Lenguaje:** Python 3
- **Dependencias externas:** ninguna para ejecutar el catálogo

## Características

- Catálogo organizado en categorías.
- Menú interactivo con recuento de categorías y paquetes.
- Vista detallada de los paquetes de cada categoría.
- **Búsqueda global** por nombre de paquete o por categoría.
- **Package Runner:** permite seleccionar un paquete desde su categoría, revisar el comando y confirmar su instalación mediante `pkg` o `pip`.
- Interfaz con colores ANSI para distinguir títulos, opciones, comandos y mensajes.
- Los colores se desactivan cuando la salida no es una terminal interactiva o cuando está definida la variable de entorno `NO_COLOR`.
- Validación de las opciones ingresadas y manejo de cancelaciones con `Ctrl+C` o fin de entrada.
- Limpieza de pantalla adaptada a Windows y otros sistemas, cuando corresponde.

## Instalación y uso

Clona el repositorio:

```bash
git clone https://github.com/lucassogarayDA/Vlsy46.git
cd Vlsy46
```

Ejecuta el programa con Python 3:

```bash
python3 Vlsy46.py
```

En Termux también puedes usar:

```bash
python Vlsy46.py
```

No hace falta instalar paquetes adicionales de Python para ejecutar Vlsy46.

## Cómo usar el menú

- Ingresa el número de una categoría para ver sus paquetes.
- Dentro de una categoría, selecciona el número de un paquete para revisar su comando e iniciar una instalación confirmada.
- Escribe **0** para volver al catálogo desde la lista de paquetes.
- Escribe **B** para abrir la búsqueda global.
- En la búsqueda, escribe el nombre de un paquete o una parte del nombre de una categoría.
- Escribe **0** para salir.
- Presiona Enter en las pantallas de resultados para volver al catálogo.

La búsqueda no distingue entre mayúsculas y minúsculas. Si no encuentra coincidencias, muestra un aviso.

## Estructura del proyecto

```text
Vlsy46/
├── Vlsy46.py
├── catalogo.py
└── README.md
```

- **`Vlsy46.py`:** contiene la interfaz, el menú, la búsqueda y el manejo de entradas.
- **`catalogo.py`:** contiene el diccionario `paquetes`, organizado por categorías. Cada paquete se asocia con el comando que permite instalarlo.

El menú obtiene las categorías y los recuentos directamente del catálogo, por lo que se actualizan al agregar o quitar entradas.

## Agregar paquetes o categorías

Edita `catalogo.py` y agrega una entrada al diccionario `paquetes`.

Ejemplo de una categoría nueva:

```python
paquetes["mi_categoria"] = {
    "paquete1": "pkg install paquete1",
    "paquete2": "pip install paquete2",
}
```

También puedes agregar un paquete dentro de una categoría existente:

```python
paquetes["utilidades"]["mi_paquete"] = "pip install mi_paquete"
```

Asegúrate de que el comando corresponda al gestor y al entorno donde se utilizará.

## Importante

Vlsy46 no ejecuta instalaciones automáticamente. Package Runner muestra el comando y solicita confirmación antes de iniciar `pkg install` o `python -m pip install`. Los comandos se ejecutan como argumentos separados, sin utilizar una shell.

Las instalaciones pueden modificar el entorno de Termux/Python y requerir conexión, espacio o dependencias adicionales. Revisa el paquete y confirma solo si deseas instalarlo. La compatibilidad de cada paquete depende del dispositivo y del entorno.

## Licencia

MIT

## Autor

Lucas Sogaray
