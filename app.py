import time
import os
from src import piezas
import random
import time


piezas.inicializar_piezas()
# Realizar un ciclo infinito
fichas_blancas = [ item for sublist in piezas.board.tablero for item in sublist if item and item.color == "Blanco"]
fichas_blancas.extend(item for sublist in piezas.board.tablero2 for item in sublist if item and item.color == "Blanco")
fichas_negras = [ item for sublist in piezas.board.tablero2 for item in sublist if item and item.color  == "Negro"]
fichas_negras.extend(item for sublist in piezas.board.tablero for item in sublist if item and item.color == "Negro")


def lista_movimientos_posibles(ficha):
    movimientos = ficha.movimientos_legales(piezas.board.tablero,piezas.board.tablero2)
    elems = []
    if movimientos:
        for mov in movimientos:
            elems.append([ficha.tipo, ficha.posicion, ficha.color, mov, ficha.dimension])
            
    return elems
def seleccionar_ficha(posicion, fichas):
    for ficha in fichas:
        if ficha.posicion == posicion:
            return ficha
    return None

def mover_ficha(ficha, nueva_posicion):
    piezas.mover(ficha, nueva_posicion)


# Hacer el juego por turnos
turno_blanco = True

while not piezas.finalizar_juego():
    piezas.mostrar_tablero()
    
    fichas_turno = fichas_blancas if turno_blanco else fichas_negras
    
    # Verificar si el jugador está en jaque
    rey = next((pieza for pieza in fichas_turno if isinstance(pieza, piezas.Rey)), None)
    if rey and rey.jaque(piezas.board.tablero, piezas.board.tablero2):
        print(f"El rey {rey.color} está en jaque.")
        movimientos_defensivos = []
        for ficha in fichas_turno:
            movimientos = lista_movimientos_posibles(ficha)
            for movimiento in movimientos:
                if piezas.mover(ficha, movimiento[3], simular=True):
                    movimientos_defensivos.append((ficha, movimiento[3]))
        
        if not movimientos_defensivos:
            print(f"El rey {rey.color} está en jaque mate. Fin del juego.")
            break
        else:
            ficha_seleccionada, nueva_posicion = random.choice(movimientos_defensivos)
            piezas.mover(ficha_seleccionada, nueva_posicion)
    else:
        ficha_seleccionada = random.choice(fichas_turno)
        movimientos = lista_movimientos_posibles(ficha_seleccionada)
        if movimientos:
            movimiento = random.choice(movimientos)
            piezas.mover(ficha_seleccionada, movimiento[3])
        else:
            print("No hay movimientos posibles para la ficha seleccionada.")
    for elem in piezas.board.tablero2:
        for item in elem:
            if item:
                if item.tipo == "Rey":
                    print(item.color, item.posicion)
    for elem in piezas.board.tablero:
        for item in elem:
            if item:
                if item.tipo == "Rey":
                    print(item.color, item.posicion)
    turno_blanco = not turno_blanco 

print(f"Fichas restantes: ")

a = 0
for elem in piezas.board.tablero:
    for item in elem:
        if item:
            if item.tipo == "Rey":
                print(item.color, item.posicion)
print(f"Tablero 1: {a} fichas")
a = 0
for elem in piezas.board.tablero2:
    for item in elem:
        if item:
            if item.tipo == "Rey":
                print(item.color, item.posicion)
print(f"Tablero 2: {a} fichas")