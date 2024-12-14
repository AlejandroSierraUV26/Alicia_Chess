import time
import os
from src import piezas


piezas.inicializar_piezas()


# *PRUEBA DE MOVIMIENTO DE PEON (Funciona bien por ahora)
# peon1 = piezas.buscar_ficha((1,0))
# peon2 = piezas.buscar_ficha((6,1))  
# peon3 = piezas.buscar_ficha((1,1))
# peon4 = piezas.buscar_ficha((6,0))


# Prueba muerte por negro y blanco en el segundo mundo
# peon1 = piezas.buscar_ficha((3,2))
# peon2 = piezas.buscar_ficha((6,3))

# piezas.mover(peon1, (4,2))
# piezas.mover(peon2, (5,3))

# piezas.movimientos_posibles(peon1)

# piezas.mover(peon1, (5,3))

# piezas.mover(peon1, (3,0))
# piezas.mover(peon2, (4,1))
# piezas.mover(peon3, (3,1))
# piezas.mover(peon4, (4,0))

# piezas.movimientos_posibles(peon1)

# *PRUEBA DE MOVIMIENTO DE TORRE (Funciona bien por ahora)
# torre1 = piezas.buscar_ficha((4,0))
# torre2 = piezas.buscar_ficha((5,5))
# torre3 = piezas.buscar_ficha((0,7)) 
# torre4 = piezas.buscar_ficha((7,7))

# piezas.movimientos_posibles(torre1)
# piezas.mover(torre1, (3,0))


# piezas.mover(torre1, (4,0))
# piezas.mover(torre2, (7,5))
# piezas.mover(torre2, (7,0))
# piezas.mover(torre2, (5,0))
# piezas.mover(torre2, (4,0))
# piezas.mover(torre4, (4,7))
# piezas.mover(torre4, (1,7))
# piezas.mover(torre3, (1,7))
# for i in range(len(piezas.fichas)):
#     print(f"{piezas.fichas[i].posicion} : {piezas.fichas[i].dimension} : {piezas.fichas[i].color} : {piezas.fichas[i].tipo}")
    


# *PRUEBA DE MOVIMIENTO DE CABALLO (Funciona bien por ahora)

# caballo1 = piezas.buscar_ficha((0,1))
# caballo2 = piezas.buscar_ficha((7,1))
# caballo3 = piezas.buscar_ficha((0,6))
# caballo4 = piezas.buscar_ficha((7,6))

# piezas.movimientos_posibles(caballo1)
# piezas.mover(caballo1, (2,2))

# piezas.mover(caballo1, (2,0))
# piezas.mover(caballo2, (5,0))
# piezas.mover(caballo1, (4,1))
# piezas.mover(caballo2, (6,2))

# piezas.mover(caballo1, (6,2))

# for i in range(len(piezas.fichas)):
#     print(f"{piezas.fichas[i].posicion} : {piezas.fichas[i].dimension} : {piezas.fichas[i].color}")

piezas.mostrar_tablero()


