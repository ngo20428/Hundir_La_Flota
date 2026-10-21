# FUNCIONES

import random

from variables import *
from clases import *


def mostrar_tablero(tablero):
    print("  " + " ".join(f'{col:2}' for col in range(columnas)))
    for i, fila in enumerate(tablero):
        print(f'{i:2} ' + "  ".join(fila))


def coordenadas():

    while True:
        fila = input("Introduce la fila (0-9): ")
        columna = input("Introduce la columna (0-9): ")

        if fila.isdigit() and columna.isdigit():
            fila = int(fila)
            columna = int(columna)

            if (0 <= fila < filas and 0 <= columna < columnas):
                return fila, columna
                break
            else:
                print("Las coordenadas tienen que estar entre 0 y 9, que si no disparas fuera, capitán!")
                continue

        else:
            print("Mete solo números del 0 al 9, porfi :)")


def disparo_maquina():
    fila = random.randint(0, filas -1)
    columna = random.randint(0, columnas -1)
    return fila, columna

def menu():
    while True:
        print("----- MENU -----")
        print("1. Modo normal")
        print("2. Modo menos fácil: la máquina dispara dos veces en cada turno.")
        print("3. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            return 1
        elif opcion == "2":
            return 2
        elif opcion == "3":
            print("¡Hasta la próxima, capitán! :)")
            return 0
        else:
            print("Opción no válida. Prueba otra vez.")