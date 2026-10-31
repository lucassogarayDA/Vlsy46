#!/data/data/com.termux/files/usr/bin/env python3

import os

from catalogo import paquetes


def limpiar():
    os.system("clear")


def main():
    print("—————————————————————Vlsy46———————————————————————")
    print("version: 1.0.2")
    print("Creado por Lucas Sogaray")

    while True:
        print("\nCategorías disponibles:\n")
        categorias = list(paquetes.keys())
        for i, categoria in enumerate(categorias, start=1):
            print(f"{i}. {categoria}")
        print("0. Salir")

        opcion = input("\nElige una categoría: ")

        if opcion == "0":
            print("¡Hasta luego!")
            break

        try:
            opcion = int(opcion)
        except ValueError:
            print("Escribe un número, por favor.")
            continue

        if 1 <= opcion <= len(categorias):
            categoria_elegida = categorias[opcion - 1]
            print(f"\n=== {categoria_elegida.upper()} ===\n")
            for nombre, comando in paquetes[categoria_elegida].items():
                print(f"- {nombre}: {comando}")
            input("\nPresiona Enter para volver al menú...")
        else:
            print("Opción no válida.")
        limpiar()


if __name__ == "__main__":
    main()
