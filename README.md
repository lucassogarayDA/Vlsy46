# Vlsy46

Vlsy46 es una herramienta de línea de comandos escrita en Python que funciona como un catálogo interactivo de paquetes y comandos de instalación para Termux. Organiza los paquetes por categorías y permite consultar sus comandos sin tener que recordar su sintaxis.

- **Versión:** 1.0.2
- **Autor:** Lucas Sogaray
- **Lenguaje:** Python 3
- **Dependencias externas:** ninguna para ejecutar el catálogo

## Características

- Catálogo organizado en categorías.
- Menú interactivo con recuento de categorías y paquetes.
- Vista detallada de los paquetes de cada categoría.
- **Búsqueda global** por nombre de paquete o por categoría.
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

- Ingresa el número de una categoría para ver sus paquetes y comandos.
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

Vlsy46 **no ejecuta comandos ni instala paquetes automáticamente**. Solo muestra los comandos para que puedas revisarlos y decidir si quieres copiarlos y ejecutarlos manualmente.

Comprueba siempre que cada comando sea adecuado para tu dispositivo, versión de Termux o entorno de Python antes de ejecutarlo.

## Licencia

MIT

## Autor

Lucas Sogaray
