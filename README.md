# Vlsy46

Vlsy46 es una herramienta de línea de comandos escrita en Python para explorar un catálogo interactivo de paquetes de Termux y Python. Organiza los paquetes por categorías, permite buscarlos, mantiene el catálogo sincronizado y puede iniciar instalaciones confirmadas desde la propia interfaz.

- **Versión:** 2.0.0
- **Tipo de lanzamiento:** Major Update
- **Autor:** Lucas Sogaray
- **Lenguaje:** Python 3
- **Dependencias externas para ejecutar Vlsy46:** ninguna

## Novedades de la versión 2.0.0

### Catálogo ampliado: 250 paquetes

El catálogo remoto incluye **250 paquetes distribuidos en 34 categorías**. Combina herramientas disponibles mediante el gestor de paquetes de Termux (`pkg`) con paquetes de Python instalables mediante `pip`.

Las categorías abarcan, entre otras, sistema, redes, lenguajes, bases de datos, servidores, multimedia, formatos, datos, desarrollo, compilación, documentación, configuración, terminal y testing.

Cada entrada relaciona el nombre del paquete con su comando de instalación. La disponibilidad y compatibilidad de cada paquete dependen de Termux, la versión de Python, la arquitectura y las dependencias que requiera.

### AutoSync: sincronización del catálogo

AutoSync permite consultar y actualizar el catálogo remoto sin tener que editar manualmente la lista local.

- **Comprobación automática:** al iniciar Vlsy46 en una terminal interactiva.
- **Comprobación manual:** selecciona la opción `U` en el menú principal.
- **Comparación de cambios:** informa cuántos paquetes son nuevos, cuántos comandos cambiaron y cuántos paquetes fueron retirados.
- **Confirmación antes de aplicar:** los cambios no se guardan hasta que el usuario los acepta.
- **Validación del catálogo:** comprueba la estructura, la versión del esquema y los datos recibidos antes de aceptarlos.
- **Caché local:** guarda el último catálogo aceptado para conservarlo entre ejecuciones y poder seguir usando los datos disponibles si no hay conexión.
- **Guardado seguro:** escribe primero un archivo temporal y después reemplaza la caché.

AutoSync actualiza los datos del catálogo; **no instala paquetes por sí solo**.

### Package Runner: instala desde el catálogo

Package Runner permite iniciar la instalación de un paquete directamente desde su categoría.

1. Entra en una categoría.
2. Selecciona el número del paquete.
3. Revisa el gestor, el nombre y el comando que se ejecutará.
4. Confirma la operación escribiendo `s`, `si` o `sí`. La opción predeterminada es no.
5. Vlsy46 inicia el gestor correspondiente y muestra el resultado de la operación.

Se admiten dos gestores:

- **Termux (`pkg`):** ejecuta instalaciones con `pkg install`.
- **Python (`pip`):** ejecuta `python -m pip install` usando el mismo intérprete de Python con el que se inició Vlsy46.

Por seguridad, el comando del catálogo se valida y se convierte en argumentos separados para el proceso. No se ejecuta mediante una shell, y no se aceptan cadenas con comandos adicionales.

### Otras funciones

- Menú interactivo con recuento de categorías y paquetes.
- Vista de paquetes y comandos dentro de cada categoría.
- Búsqueda global por nombre de paquete o categoría, sin distinguir mayúsculas y minúsculas.
- Interfaz con colores ANSI, desactivados cuando la salida no es una terminal interactiva o está definida la variable `NO_COLOR`.
- Validación de entradas y manejo de cancelaciones con `Ctrl+C` o fin de entrada.
- Limpieza de pantalla adaptada al sistema cuando corresponde.

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

Para actualizar una copia existente desde la rama principal:

```bash
git pull origin main
```

No hace falta instalar dependencias adicionales de Python para ejecutar el catálogo. Los gestores `pkg` y `pip` se necesitan cuando se desea instalar paquetes desde Package Runner.

## Cómo usar el menú

- **Número de categoría:** abre la categoría correspondiente.
- **Número de paquete:** muestra los detalles e inicia el flujo de Package Runner.
- **B:** abre la búsqueda global.
- **U:** comprueba si hay una actualización del catálogo.
- **0:** vuelve desde una categoría o sale del programa, según la pantalla.

Al abrir una categoría, selecciona un paquete para revisar su comando. Package Runner siempre solicita confirmación antes de ejecutar la instalación.

## Estructura del proyecto

```text
Vlsy46/
├── Vlsy46.py
├── catalogo.py
├── catalogo.json
├── autosync.py
└── README.md
```

- **`Vlsy46.py`:** interfaz, menú, búsqueda, selección de paquetes y Package Runner.
- **`catalogo.py`:** catálogo local de respaldo y carga de la última caché aceptada.
- **`catalogo.json`:** catálogo remoto versionado que AutoSync consulta.
- **`autosync.py`:** descarga, validación y almacenamiento de la caché del catálogo.
- **`catalogo_cache.json`:** archivo local generado al aceptar una actualización; no es necesario crearlo manualmente.

## Agregar o modificar paquetes

El catálogo remoto se mantiene en `catalogo.json`. Cada categoría contiene nombres de paquetes asociados a comandos compatibles con los gestores admitidos.

Ejemplo de una categoría:

```json
{
  "mi_categoria": {
    "paquete-termux": "pkg install paquete-termux",
    "paquete-python": "pip install paquete-python"
  }
}
```

Al publicar cambios en el catálogo remoto, incrementa `catalog_version` para que AutoSync pueda detectar la actualización. Mantén `schema_version` en el valor compatible con la versión actual de Vlsy46.

## Seguridad y compatibilidad

Vlsy46 no instala paquetes automáticamente. Package Runner muestra qué gestor y paquete se utilizarán y requiere confirmación explícita antes de ejecutar la instalación.

Las instalaciones pueden modificar el entorno de Termux o Python, consumir almacenamiento, requerir conexión o necesitar dependencias adicionales. Revisa cada paquete antes de confirmar. No todos los paquetes de Python publicados en PyPI son compatibles con Android o Termux, especialmente los que necesitan componentes nativos.

AutoSync solo actualiza el catálogo después de validar los datos y recibir confirmación. Si no puede consultar el catálogo remoto, Vlsy46 puede utilizar el catálogo local o la última caché aceptada.

## Licencia

MIT

## Autor

Lucas Sogaray


## Instalación desde PyPI

Cuando la versión 2.0.0 esté publicada en PyPI, se podrá instalar con:

```bash
python -m pip install vlsy46
vlsy46
```

El paquete incluye el catálogo inicial. AutoSync puede consultar el catálogo remoto y guarda su caché en el directorio de usuario `~/.cache/vlsy46` (o en la ruta indicada por `VLSY46_CACHE_DIR`). La caché no se escribe dentro de los archivos instalados del paquete.
