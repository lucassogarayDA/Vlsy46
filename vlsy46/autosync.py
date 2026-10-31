"""Sincronización segura del catálogo remoto de Vlsy46."""

import json
import os
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

URL_CATALOGO = (
    "https://raw.githubusercontent.com/"
    "lucassogarayDA/Vlsy46/main/catalogo.json"
)
DIRECTORIO_CACHE = Path(
    os.environ.get("VLSY46_CACHE_DIR", str(Path.home() / ".cache" / "vlsy46"))
)
ARCHIVO_CACHE = DIRECTORIO_CACHE / "catalogo_cache.json"
TIMEOUT = 8
MAX_BYTES = 2 * 1024 * 1024


class ErrorCatalogo(Exception):
    """Error al descargar, validar o guardar un catálogo."""


def validar_catalogo(datos):
    if not isinstance(datos, dict):
        raise ErrorCatalogo("El documento remoto no es un objeto JSON.")

    if datos.get("schema_version") != 1:
        raise ErrorCatalogo("Versión de formato de catálogo no compatible.")

    version = datos.get("catalog_version")
    if not isinstance(version, int) or isinstance(version, bool) or version < 1:
        raise ErrorCatalogo("La versión del catálogo no es válida.")

    paquetes = datos.get("packages")
    if not isinstance(paquetes, dict) or not paquetes:
        raise ErrorCatalogo("El catálogo no contiene categorías válidas.")

    if len(paquetes) > 200:
        raise ErrorCatalogo("El catálogo supera el límite de categorías.")

    for categoria, elementos in paquetes.items():
        if not isinstance(categoria, str) or not categoria.strip():
            raise ErrorCatalogo("Se encontró una categoría sin nombre.")
        if not isinstance(elementos, dict) or len(elementos) > 1000:
            raise ErrorCatalogo(f"Categoría inválida: {categoria}")

        for nombre, comando in elementos.items():
            if not isinstance(nombre, str) or not nombre.strip():
                raise ErrorCatalogo(f"Paquete sin nombre en {categoria}.")
            if not isinstance(comando, str) or not comando.strip():
                raise ErrorCatalogo(f"Comando inválido para {nombre}.")
            if len(nombre) > 120 or len(comando) > 500:
                raise ErrorCatalogo(f"Entrada demasiado larga: {nombre}")

    return datos


def cargar_cache():
    """Carga el último catálogo aceptado; devuelve None si no es válido."""
    try:
        with ARCHIVO_CACHE.open("r", encoding="utf-8") as archivo:
            return validar_catalogo(json.load(archivo))
    except (OSError, json.JSONDecodeError, ErrorCatalogo):
        return None


def descargar_catalogo():
    """Descarga y valida el catálogo publicado en GitHub."""
    solicitud = Request(
        URL_CATALOGO,
        headers={"User-Agent": "Vlsy46-AutoSync/1.0", "Accept": "application/json"},
    )
    try:
        with urlopen(solicitud, timeout=TIMEOUT) as respuesta:
            contenido = respuesta.read(MAX_BYTES + 1)
        if len(contenido) > MAX_BYTES:
            raise ErrorCatalogo("El catálogo remoto supera el tamaño permitido.")
        datos = json.loads(contenido.decode("utf-8"))
        return validar_catalogo(datos)
    except HTTPError as error:
        raise ErrorCatalogo(f"GitHub respondió con HTTP {error.code}.") from error
    except URLError as error:
        raise ErrorCatalogo("No se pudo conectar con GitHub.") from error
    except (TimeoutError, OSError) as error:
        raise ErrorCatalogo("La conexión falló o agotó el tiempo de espera.") from error
    except UnicodeDecodeError as error:
        raise ErrorCatalogo("El catálogo remoto no usa UTF-8 válido.") from error
    except json.JSONDecodeError as error:
        raise ErrorCatalogo("GitHub devolvió un JSON inválido.") from error


def guardar_cache(datos):
    """Guarda el catálogo aceptado mediante reemplazo atómico."""
    validar_catalogo(datos)
    temporal = ARCHIVO_CACHE.with_suffix(".json.tmp")
    try:
        ARCHIVO_CACHE.parent.mkdir(parents=True, exist_ok=True)
        with temporal.open("w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, ensure_ascii=False, indent=2)
            archivo.write("\n")
        os.replace(temporal, ARCHIVO_CACHE)
    except OSError as error:
        try:
            temporal.unlink(missing_ok=True)
        except OSError:
            pass
        raise ErrorCatalogo("No se pudo guardar el catálogo local.") from error
