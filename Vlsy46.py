#!/usr/bin/env python3

import os
import re
import shutil
import subprocess
import sys

from catalogo import paquetes, VERSION_CATALOGO
from autosync import ErrorCatalogo, descargar_catalogo, guardar_cache


COLORES = {
    "cian": "\033[96m",
    "verde": "\033[92m",
    "amarillo": "\033[93m",
    "rojo": "\033[91m",
    "gris": "\033[90m",
    "negrita": "\033[1m",
    "reset": "\033[0m",
}

COLORES_ACTIVOS = sys.stdout.isatty() and os.environ.get("NO_COLOR") is None


def estilo(texto, *colores):
    if not COLORES_ACTIVOS:
        return str(texto)
    prefijo = "".join(COLORES[color] for color in colores)
    return f"{prefijo}{texto}{COLORES['reset']}"


def limpiar():
    if not sys.stdout.isatty():
        return

    comando = "cls" if os.name == "nt" else "clear"
    if shutil.which(comando):
        os.system(comando)


def leer_entrada(mensaje):
    try:
        return input(mensaje).strip()
    except (EOFError, KeyboardInterrupt):
        print("\n" + estilo("Operación cancelada. ¡Hasta luego!", "amarillo"))
        raise SystemExit(0)


def pausar(mensaje):
    leer_entrada(estilo(mensaje, "amarillo"))


def mostrar_encabezado():
    print(estilo("╔══════════════════════════════════════════════╗", "cian"))
    print(estilo("║                    Vlsy46                    ║", "cian", "negrita"))
    print(estilo("║                   versión 1.2.0              ║", "gris"))
    print(estilo("║              Creado por Lucas Sogaray        ║", "gris"))
    print(estilo("╚══════════════════════════════════════════════╝", "cian"))


def buscar_paquetes(consulta):
    coincidencias = []
    consulta = consulta.casefold()

    for categoria, lista_paquetes in paquetes.items():
        for nombre, comando in lista_paquetes.items():
            if consulta in nombre.casefold() or consulta in categoria.casefold():
                coincidencias.append((nombre, comando, categoria))

    return coincidencias


def mostrar_busqueda():
    limpiar()
    mostrar_encabezado()
    print("\n" + estilo("BÚSQUEDA GLOBAL", "cian", "negrita"))
    print(estilo("Busca por nombre de paquete o categoría.", "gris"))
    consulta = leer_entrada("\n" + estilo("Buscar: ", "amarillo"))

    if not consulta:
        pausar("\nLa búsqueda está vacía. Presiona Enter para continuar...")
        return

    resultados = buscar_paquetes(consulta)
    limpiar()
    mostrar_encabezado()
    print("\n" + estilo(f"RESULTADOS PARA: {consulta}", "cian", "negrita"))
    print(estilo("────────────────────────────────────────────────", "gris"))

    if not resultados:
        print("\n" + estilo("No se encontraron coincidencias.", "rojo"))
    else:
        print(
            f"\n{estilo('Coincidencias:', 'gris')} "
            f"{estilo(len(resultados), 'verde', 'negrita')}\n"
        )
        for nombre, comando, categoria in resultados:
            print(f"  {estilo('•', 'amarillo')} {estilo(nombre, 'verde', 'negrita')}")
            print(f"    {estilo('Categoría:', 'gris')} {categoria}")
            print(f"    {estilo(comando, 'cian')}\n")

    print(estilo("────────────────────────────────────────────────", "gris"))
    pausar("Presiona Enter para volver al catálogo...")


def mostrar_menu():
    categorias = list(paquetes.keys())
    total_paquetes = sum(len(lista) for lista in paquetes.values())

    mostrar_encabezado()
    print("\n" + estilo("CATÁLOGO DE PAQUETES", "cian", "negrita"))
    print(estilo("────────────────────────────────────────────────", "gris"))
    print(
        f"{estilo('Categorías:', 'gris')} {estilo(len(categorias), 'amarillo', 'negrita')}"
        f"  |  {estilo('Paquetes:', 'gris')} {estilo(total_paquetes, 'verde', 'negrita')}\n"
    )

    for numero, categoria in enumerate(categorias, start=1):
        cantidad = len(paquetes[categoria])
        numero_texto = estilo(f"{numero:>2}.", "amarillo")
        categoria_texto = estilo(f"{categoria:<22}", "verde")
        cantidad_texto = estilo(f"[{cantidad} paquetes]", "gris")
        print(f"  {numero_texto} {categoria_texto} {cantidad_texto}")

    print("\n  " + estilo("B. Buscar paquetes", "cian", "negrita"))
    print("  " + estilo("U. Buscar actualizaciones", "amarillo", "negrita"))
    print("  " + estilo("0. Salir", "rojo"))
    print(estilo("────────────────────────────────────────────────", "gris"))
    return categorias


def analizar_comando_instalacion(comando):
    """Acepta únicamente comandos simples de instalación pkg o pip."""
    coincidencia = re.fullmatch(
        r"(pkg|pip) install ([A-Za-z0-9][A-Za-z0-9._+:-]*)",
        comando.strip(),
    )
    if not coincidencia:
        return None

    gestor, paquete = coincidencia.groups()
    return gestor, paquete


def ejecutar_instalacion(comando):
    """Ejecuta una instalación sin pasar por un intérprete de comandos."""
    analizado = analizar_comando_instalacion(comando)
    if analizado is None:
        print(estilo("Comando no permitido. Solo se aceptan instalaciones pkg o pip.", "rojo"))
        pausar("Presiona Enter para continuar...")
        return

    gestor, paquete = analizado
    if gestor == "pkg":
        argumentos = ["pkg", "install", paquete]
        comando_visible = f"pkg install {paquete}"
    else:
        argumentos = [sys.executable, "-m", "pip", "install", paquete]
        comando_visible = f"{sys.executable} -m pip install {paquete}"

    print("\n" + estilo("PACKAGE RUNNER", "cian", "negrita"))
    print(f"{estilo('Gestor:', 'gris')} {gestor}")
    print(f"{estilo('Paquete:', 'gris')} {paquete}")
    print(f"{estilo('Comando:', 'gris')} {comando_visible}")
    print(estilo("El instalador puede modificar el entorno de Termux/Python.", "amarillo"))
    respuesta = leer_entrada(estilo("¿Ejecutar la instalación? [s/N]: ", "amarillo"))
    if respuesta.casefold() not in ("s", "si", "sí"):
        print(estilo("Instalación cancelada.", "amarillo"))
        pausar("Presiona Enter para continuar...")
        return

    print("\n" + estilo("Iniciando instalación...", "cian", "negrita"))
    try:
        resultado = subprocess.run(argumentos, check=False)
    except FileNotFoundError:
        print(estilo(f"No se encontró el ejecutable necesario para {gestor}.", "rojo"))
    except OSError as error:
        print(estilo(f"No se pudo iniciar el instalador: {error}", "rojo"))
    else:
        if resultado.returncode == 0:
            print(estilo("\\nInstalación finalizada correctamente.", "verde", "negrita"))
        else:
            print(estilo(f"\\nEl instalador terminó con código {resultado.returncode}.", "rojo"))
    pausar("Presiona Enter para volver a los paquetes...")


def mostrar_categoria(categoria):
    lista_paquetes = list(paquetes[categoria].items())

    while True:
        limpiar()
        mostrar_encabezado()
        print("\\n" + estilo(categoria.upper(), "cian", "negrita"))
        print(estilo("Selecciona un paquete para ver su comando o instalarlo.", "gris"))
        print(estilo("────────────────────────────────────────────────", "gris"))
        print(f"{estilo('Paquetes disponibles:', 'gris')} {estilo(len(lista_paquetes), 'verde', 'negrita')}\\n")

        for numero, (nombre, comando) in enumerate(lista_paquetes, start=1):
            print(f"  {estilo(f'{numero:>3}.', 'amarillo')} {estilo(nombre, 'verde', 'negrita')}")
            print(f"       {estilo(comando, 'cian')}")

        print("\\n  " + estilo("0. Volver", "rojo"))
        print(estilo("────────────────────────────────────────────────", "gris"))
        opcion = leer_entrada(estilo("Selecciona un paquete: ", "amarillo"))

        if opcion == "0":
            return
        if not opcion.isdigit() or not 1 <= int(opcion) <= len(lista_paquetes):
            pausar("Selección no válida. Presiona Enter para continuar...")
            continue

        nombre, comando = lista_paquetes[int(opcion) - 1]
        limpiar()
        mostrar_encabezado()
        print("\\n" + estilo(f"PAQUETE: {nombre}", "cian", "negrita"))
        print(f"{estilo('Comando del catálogo:', 'gris')} {comando}")
        ejecutar_instalacion(comando)


def sincronizar_catalogo(origen):
    global paquetes, VERSION_CATALOGO

    print("\n" + estilo("AUTOSYNC", "cian", "negrita"))
    print(estilo("Consultando el catálogo remoto...", "gris"))

    try:
        remoto = descargar_catalogo()
    except ErrorCatalogo as error:
        print(estilo(f"No se pudo comprobar: {error}", "rojo"))
        if origen == "manual":
            pausar("Presiona Enter para volver al menú...")
        return

    version_remota = remoto["catalog_version"]
    if version_remota <= VERSION_CATALOGO:
        if version_remota == VERSION_CATALOGO:
            print(estilo("Ya tienes la versión más reciente del catálogo.", "verde"))
        else:
            print(estilo("El catálogo remoto tiene una versión anterior. No se aplicaron cambios.", "amarillo"))
        if origen == "manual":
            pausar("Presiona Enter para volver al menú...")
        return

    nuevos = []
    modificados = []
    retirados = []
    for categoria, elementos in remoto["packages"].items():
        actuales = paquetes.get(categoria, {})
        for nombre, comando in elementos.items():
            if nombre not in actuales:
                nuevos.append((categoria, nombre))
            elif actuales[nombre] != comando:
                modificados.append((categoria, nombre))
    for categoria, elementos in paquetes.items():
        remotos = remoto["packages"].get(categoria, {})
        for nombre in elementos:
            if nombre not in remotos:
                retirados.append((categoria, nombre))

    print(estilo(f"Actualización disponible: catálogo {VERSION_CATALOGO} → {version_remota}", "verde", "negrita"))
    print(f"Paquetes nuevos: {len(nuevos)}")
    print(f"Comandos modificados: {len(modificados)}")
    print(f"Paquetes retirados: {len(retirados)}")
    for categoria, nombre in nuevos[:12]:
        print(estilo(f"  + {categoria}/{nombre}", "verde"))
    for categoria, nombre in modificados[:12]:
        print(estilo(f"  ~ {categoria}/{nombre}", "amarillo"))
    for categoria, nombre in retirados[:12]:
        print(estilo(f"  - {categoria}/{nombre}", "rojo"))
    if len(nuevos) + len(modificados) + len(retirados) > 12:
        print(estilo("Se muestran hasta 12 elementos por tipo.", "gris"))

    respuesta = leer_entrada(estilo("¿Aplicar esta actualización? [s/N]: ", "amarillo"))
    if respuesta.casefold() not in ("s", "si", "sí"):
        print(estilo("Actualización cancelada. Se conserva el catálogo actual.", "amarillo"))
    else:
        try:
            guardar_cache(remoto)
        except ErrorCatalogo as error:
            print(estilo(str(error), "rojo"))
        else:
            paquetes = remoto["packages"]
            VERSION_CATALOGO = version_remota
            print(estilo("Catálogo actualizado correctamente.", "verde", "negrita"))

    if origen == "manual":
        pausar("Presiona Enter para volver al menú...")


def main():
    global paquetes
    if sys.stdout.isatty():
        sincronizar_catalogo("inicio")

    while True:
        limpiar()
        categorias = mostrar_menu()
        opcion = leer_entrada("\n" + estilo("Selecciona una categoría, B para buscar o U para actualizar: ", "amarillo"))

        if opcion == "0":
            print("\n" + estilo("¡Hasta luego!", "verde", "negrita"))
            break

        if opcion.casefold() == "b":
            mostrar_busqueda()
            continue

        if opcion.casefold() == "u":
            sincronizar_catalogo("manual")
            continue

        if not opcion.isdigit():
            pausar("\nEntrada no válida. Escribe un número, B o U. Presiona Enter...")
            continue

        numero = int(opcion)
        if 1 <= numero <= len(categorias):
            mostrar_categoria(categorias[numero - 1])
        else:
            pausar("\nOpción fuera del menú. Presiona Enter para continuar...")


if __name__ == "__main__":
    try:
        main()
    except BrokenPipeError:
        pass
