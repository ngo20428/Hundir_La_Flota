# CLASES

import random

from variables import *

class Tablero:

    def __init__(self, jugador):
        
        self.jugador = jugador
        
        # Tablero propio: en el que tenemos nuestros barcos + los disparos recibidos
        self.tablero_propio = [[agua for i in range(columnas)] for j in range(filas)]

        # Tablero "rival": en el que vamos registrando los disparos que vamos haciendo
        self.tablero_disparos = [[agua for i in range(columnas)] for j in range(filas)]

        # Llevamos registro de los barcos que siguen a flote
        self.barcos_restantes = sum(eslora * num 
                                    for eslora, num in barcos_dict.items())
        
        
    def colocar_barcos(self):
        """Coloca todos los barcos aleatoriamente y aislados."""
        self.itsasontzis = []

        for eslora, cantidad in barcos_dict.items(): # Cada tipo de barco
            for _ in range(cantidad): # Repetimos el num de veces que está ese barco
                # Repetimos hasta encontrar una posición válida
                posicion_valida = False
                while not posicion_valida:
                    fila = random.randint(0, filas - 1)
                    col = random.randint(0, columnas - 1)
                    orientacion = random.choice(["H", "V"])

                    celdas_barco = []
                    for x in range(eslora):
                        if orientacion == "H":
                            celdas_barco.append((fila, col + x))
                            
                        else:
                            celdas_barco.append((fila + x, col))

                    # Comprobamos que el barco cabe en el tablero
                    if any(not (0 <= f < filas and 0 <= c < columnas) for f, c in celdas_barco):

                        continue # Si no cabe, vuelve a pedir coordenadas nuevas (aquí sí funciona porque está al inicio)

                    # Obtenemos las celdas que rodean al barco
                    celdas_adyacentes = set()
                    for f, c in celdas_barco: # Para cada casilla del barco
                        for i in [-1, 0, 1]: # Fila de arriba, misma y la de abajo
                            for j in [-1, 0, 1]:
                                nf = f + i # Nuevas coordenadas
                                nc = c + j
                                if 0 <= nf < filas and 0 <= nc < columnas:
                                    celdas_adyacentes.add((nf, nc))

                    # Comprobamos que no haya barcos alrededor
                    if any(self.tablero_propio[f][c] != agua for f, c in celdas_adyacentes):
                        # Si toca a otro barco, NO hacemos continue. 
                        # Dejamos que el bucle vuelva a empezar y genere un nuevo random
                        pass 
                    else:
                        # Si no hay barcos alrededor, colocamos el barco y salimos del bucle while
                        barco_actual = []
                        for f, c in celdas_barco:
                            self.tablero_propio[f][c] = barco
                            barco_actual.append((f, c))
                        
                        self.itsasontzis.append(barco_actual) # Añadimos la posición del barco a la lista de barcos
                        posicion_valida = True

                

    def recibir_disparo(self, fila, columna):
        
        # Si había barco:
        if self.tablero_propio[fila][columna] == barco:
            self.tablero_propio[fila][columna] = impacto # cambiamos el ikurra por el de impacto
            self.barcos_restantes -=1

            # Ahora comprobamos si el barco ha sido hundido o solo tocado
            for barco_tocado in self.itsasontzis:
                if (fila, columna) in barco_tocado:
                    barco_tocado.remove((fila, columna)) # Quitamos la posición disparada

                    # El barco está hundido cuando ya no le quedan posiciones:
                    hundido = len(barco_tocado) == 0

                    return "impacto", hundido
                    # "impacto", True --> el barco está hundido
                    # "impacto", False --> el barco solo ha sido tocado
        
        else: # Si no había barco --> había agua
            self.tablero_propio[fila][columna] = fallo
            return "fallo", False # Ni tocado ni hundido --> agua


    def registrar_disparo(self, fila, columna, resultado):
        if resultado == "impacto":
            self.tablero_disparos[fila][columna] = impacto
        
        elif resultado == "fallo":
            self.tablero_disparos[fila][columna] = fallo

    def disparo_repe(self, fila, columna):
        return self.tablero_disparos[fila][columna] != agua