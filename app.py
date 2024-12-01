import numpy as np
import os

os.system('cls')
tablero = np.array([['T', 'C', 'A', 'D', 'R',   'A', 'C', 'T'],
                        ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
                        ['-', '-', '-', '-', '-', '-', '-', '-'],
                        ['-', '-', '-', '-', '-', '-', '-', '-'],
                        ['-', '-', '-', '-', '-', '-', '-', '-'],
                        ['-', '-', '-', '-', '-', '-', '-', '-'],
                        ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
                        ['T', 'C', 'A', 'R', 'D', 'A', 'C', 'T']])
tablero_vacio = np.array([['-', '-', '-', '-', '-', '-', '-', '-'],
                            ['-', '-', '-', '-', '-', '-', '-', '-'],
                            ['-', '-', '-', '-', '-', '-', '-', '-'],
                            ['-', '-', '-', '-', '-', '-', '-', '-'],
                            ['-', '-', '-', '-', '-', '-', '-', '-'],
                            ['-', '-', '-', '-', '-', '-', '-', '-'],
                            ['-', '-', '-', '-', '-', '-', '-', '-'],
                            ['-', '-', '-', '-', '-', '-', '-', '-']])

def encontrar_ficha(ficha, i, j):
    if tablero[i, j] == ficha:
        return 'tablero', (i, j)
    if tablero_vacio[i, j] == ficha:
        return 'tablero_vacio', (i, j)
    return None, None

def mover_ficha(ficha, pos_inicial, pos_final, dimension):
    if dimension == "tablero_vacio":
        tablero_vacio[pos_inicial] = '-'
        tablero[pos_final] = ficha    
    else:
        tablero[pos_inicial] = '-'
        tablero_vacio[pos_final] = ficha

def imprimir_tableros(tablero, tablero_vacio):
    indices = '  ' + ' '.join(map(str, range(8)))
    print(indices + '    ' + indices)
    for i, (fila1, fila2) in enumerate(zip(tablero, tablero_vacio)):
        print(str(i) + ' ' + ' '.join(fila1) + '    ' + str(i) + ' ' + ' '.join(fila2))

imprimir_tableros(tablero, tablero_vacio)
dim = encontrar_ficha('P', 1, 0)[0]
mover_ficha('P', (1, 0), (3, 0), dim)
print()
imprimir_tableros(tablero, tablero_vacio)
dim = encontrar_ficha('P', 3, 0)[0]
mover_ficha('P', (3, 0), (4, 0), dim)
print()
imprimir_tableros(tablero, tablero_vacio)



