import time
import os
from src import piezas



fichas = piezas.inicializar_piezas()
peon1 = piezas.buscar_ficha((1,0),fichas)
peon3 = piezas.buscar_ficha((6,0),fichas)
peon4 = piezas.buscar_ficha((6,1),fichas)
alfil1 = piezas.buscar_ficha((0,2),fichas)
torre1 = piezas.buscar_ficha((0,0),fichas)

piezas.mover(peon1, (3,0))
piezas.mover(peon3, (4,0))
piezas.movimientos_posibles(peon1)
piezas.movimientos_posibles(peon3)
print(peon1.color)
print(peon3.color)


piezas.mostrar_tablero()

