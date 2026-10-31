#!/data/data/com.termux/files/usr/bin/env python3

import os
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

COLORES_ACTIVOS = sys.stdout.isatty()


def estilo(texto, *colores):
    if not COLORES_ACTIVOS:
        return str(texto)
    prefijo = "".join(COLORES[color] for color in colores)
    return f"{prefijo}{texto}{COLORES['reset']}"


def limpiar():
    os.system("clear")


def mostrar_encabezado():
    print(estilo("╔══════════════════════════════════════════════╗", "cian"))
    print(estilo("║                    Vlsy46                    ║", "cian", "negrita"))
    print(estilo("║                   versión 1.0.2              ║", "gris"))
    print(estilo("║              Creado por Lucas Sogaray        ║", "gris"))
    print(estilo("╚══════════════════════════════════════════════╝", "cian"))


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

    print("\n  " + estilo("0. Salir", "rojo"))
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
    input(estilo("Presiona Enter para volver al catálogo...", "amarillo"))


def main():
    while True:
        limpiar()
        categorias = mostrar_menu()
        opcion = input("\n" + estilo("Selecciona una categoría: ", "amarillo")).strip()

        if opcion == "0":
            print("\n" + estilo("¡Hasta luego!", "verde", "negrita"))
            break

        if not opcion.isdigit():
            input("\n" + estilo("Entrada no válida. Escribe un número. Presiona Enter...", "rojo"))
            continue

        numero = int(opcion)
        if 1 <= numero <= len(categorias):
            mostrar_categoria(categorias[numero - 1])
        else:
            input("\n" + estilo("Opción fuera del menú. Presiona Enter para continuar...", "rojo"))


if __name__ == "__main__":
    main()
