#!/data/data/com.termux/files/usr/bin/env python3

import os

from catalogo import paquetes


def limpiar():
    os.system("clear")


def mostrar_encabezado():
    print("╔══════════════════════════════════════════════╗")
    print("║                    Vlsy46                    ║")
    print("║                   versión 1.0.2              ║")
    print("║              Creado por Lucas Sogaray        ║")
    print("╚══════════════════════════════════════════════╝")


def mostrar_menu():
    categorias = list(paquetes.keys())
    total_paquetes = sum(len(lista) for lista in paquetes.values())

    mostrar_encabezado()
    print("\nCATÁLOGO DE PAQUETES")
    print("────────────────────────────────────────────────")
    print(f"Categorías: {len(categorias)}  |  Paquetes: {total_paquetes}\n")

    for numero, categoria in enumerate(categorias, start=1):
        cantidad = len(paquetes[categoria])
        print(f"  {numero:>2}. {categoria:<22} [{cantidad} paquetes]")

    print("\n   0. Salir")
    print("────────────────────────────────────────────────")
    return categorias


def mostrar_categoria(categoria):
    lista_paquetes = paquetes[categoria]

    limpiar()
    mostrar_encabezado()
    print(f"\n{categoria.upper()}")
    print("────────────────────────────────────────────────")
    print(f"Paquetes disponibles: {len(lista_paquetes)}\n")

    for nombre, comando in lista_paquetes.items():
        print(f"  • {nombre}")
        print(f"    {comando}")

    print("\n────────────────────────────────────────────────")
    input("Presiona Enter para volver al catálogo...")


def main():
    while True:
        limpiar()
        categorias = mostrar_menu()
        opcion = input("\nSelecciona una categoría: ").strip()

        if opcion == "0":
            print("\n¡Hasta luego!")
            break

        if not opcion.isdigit():
            input("\nEntrada no válida. Escribe un número. Presiona Enter...")
            continue

        numero = int(opcion)
        if 1 <= numero <= len(categorias):
            mostrar_categoria(categorias[numero - 1])
        else:
            input("\nOpción fuera del menú. Presiona Enter para continuar...")


if __name__ == "__main__":
    main()
