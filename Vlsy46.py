#!/usr/bin/env python3

import os
import shutil
import sys

from catalogo import paquetes


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
    print(estilo("║                   versión 1.1.0              ║", "gris"))
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
    print("  " + estilo("0. Salir", "rojo"))
    print(estilo("────────────────────────────────────────────────", "gris"))
    return categorias


def mostrar_categoria(categoria):
    lista_paquetes = paquetes[categoria]

    limpiar()
    mostrar_encabezado()
    print("\n" + estilo(categoria.upper(), "cian", "negrita"))
    print(estilo("────────────────────────────────────────────────", "gris"))
    print(
        f"{estilo('Paquetes disponibles:', 'gris')} "
        f"{estilo(len(lista_paquetes), 'verde', 'negrita')}\n"
    )

    for nombre, comando in lista_paquetes.items():
        print(f"  {estilo('•', 'amarillo')} {estilo(nombre, 'verde', 'negrita')}")
        print(f"    {estilo(comando, 'cian')}")

    print("\n" + estilo("────────────────────────────────────────────────", "gris"))
    pausar("Presiona Enter para volver al catálogo...")


def main():
    while True:
        limpiar()
        categorias = mostrar_menu()
        opcion = leer_entrada("\n" + estilo("Selecciona una categoría o B para buscar: ", "amarillo"))

        if opcion == "0":
            print("\n" + estilo("¡Hasta luego!", "verde", "negrita"))
            break

        if opcion.casefold() == "b":
            mostrar_busqueda()
            continue

        if not opcion.isdigit():
            pausar("\nEntrada no válida. Escribe un número o B. Presiona Enter...")
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
