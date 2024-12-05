import time
import os
from src import piezas



fichas = piezas.inicializar_piezas()

peon4 = piezas.buscar_ficha((1,3),fichas)
peon5 = piezas.buscar_ficha((1,4),fichas)
peon1 = piezas.buscar_ficha((6,5),fichas)
peon6 = piezas.buscar_ficha((6,3),fichas)
peon7 = piezas.buscar_ficha((6,4),fichas)
alfil = piezas.buscar_ficha((0,2),fichas)




ficha = piezas.mover(peon4, (2,3))
if ficha:
    fichas.remove(ficha)
ficha = piezas.mover(peon5, (2,4))
ficha = piezas.mover(peon1, (5,5))
ficha = piezas.mover(peon6, (5,3))
ficha = piezas.mover(peon7, (5,4))
ficha = piezas.mover(peon4, (3,3))
ficha = piezas.mover(peon5, (3,4))
ficha = piezas.mover(peon1, (4,5))
ficha = piezas.mover(peon6, (4,3))
ficha = piezas.mover(peon7, (4,4))

piezas.movimientos_posibles(peon5)
ficha = piezas.mover(peon5, (4,5))
fichas.remove(ficha)
piezas.movimientos_posibles(peon7)




piezas.mostrar_tablero()

