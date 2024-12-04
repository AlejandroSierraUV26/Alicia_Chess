import time
import os
from src import piezas



fichas = piezas.inicializar_piezas()
peon1 = piezas.buscar_ficha((1,2),fichas)
peon2 = piezas.buscar_ficha((1,3),fichas)
peon3 = piezas.buscar_ficha((1,4),fichas)

piezas.mover(peon1, (2,2))
piezas.mover(peon2, (2,3))
piezas.mover(peon3, (2,4))

piezas.mostrar_tablero()

reina = piezas.buscar_ficha((0,3), fichas)

piezas.movimientos_posibles(reina)

piezas.mover(reina, (4,7))

piezas.mostrar_tablero()