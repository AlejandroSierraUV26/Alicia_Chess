import time
import os
from src import piezas
import random
import time
import pygame


piezas.inicializar_piezas()
# Realizar un ciclo infinito
fichas_blancas = [ item for sublist in piezas.board.tablero for item in sublist if item and item.color == "Blanco"]
fichas_blancas.extend(item for sublist in piezas.board.tablero2 for item in sublist if item and item.color == "Blanco")
fichas_negras = [ item for sublist in piezas.board.tablero2 for item in sublist if item and item.color  == "Negro"]
fichas_negras.extend(item for sublist in piezas.board.tablero for item in sublist if item and item.color == "Negro")
tabla_costo_peon = [
    [1, 1, 1, 1, 1, 1, 1, 1],
    [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5],
    [0.3, 0.3, 0.35, 0.45, 0.45, 0.35, 0.3, 0.3],
    [ 0.5, 0.5, 1, 2.5, 2.5, 1, 0.5, 0.5],
    [0.15, 0.15, 0.15, 0.27, 0.27, 0.15, 0.15, 0.15],
    [ 0.5, -0.5, -1, 0, 0, -1, -0.5, 0.5],
    [0.05, 0.1, 0.1, -0.25, -0.25, 0.1, 0.1, 0.05],
    [ 0, 0, 0, 0, 0, 0, 0, 0]
]
tabla_costo_caballo = [
    [-0.5, -0.4, -0.3, -0.3, -0.3, -0.3, -0.4, -0.5],
    [-0.4, -0.2,  0,    0,    0,    0,  -0.2, -0.4],
    [-0.3,  0,    0.1,  0.15, 0.15, 0.1,  0,  -0.3],
    [-0.3,  0.05, 0.15, 0.2,  0.2,  0.15, 0.05, -0.3],
    [-0.3,  0,    0.15, 0.2,  0.2,  0.15, 0,  -0.3],
    [-0.3,  0.05, 0.1,  0.15, 0.15, 0.1,  0.05, -0.3],
    [-0.4, -0.2,  0,    0.05, 0.05, 0,   -0.2, -0.4],
    [-0.5, -0.4, -0.2, -0.3, -0.3, -0.2, -0.4, -0.5]
]
tabla_costo_alfil = [
    [-0.4, -0.2, -0.2, -0.2, -0.2, -0.2, -0.2, -0.4],
    [-0.2,  0.1,  0.1,  0.1,  0.1,  0.1,  0.1, -0.2],
    [-0.2,  0.1,  0.2,  0.3,  0.3,  0.2,  0.1, -0.2],
    [-0.2,  0.2,  0.2,  0.3,  0.3,  0.2,  0.2, -0.2],
    [-0.2,  0.1,  0.3,  0.3,  0.3,  0.3,  0.1, -0.2],
    [-0.2,  0.3,  0.3,  0.3,  0.3,  0.3,  0.3, -0.2],
    [-0.2,  0.2,  0.1,  0.1,  0.1,  0.1,  0.2, -0.2],
    [-0.4, -0.2, -0.6, -0.2, -0.2, -0.6, -0.2, -0.4]
]

tabla_costo_torre = [
    [-0.5, -0.4, -0.3, -0.2, -0.2, -0.3, -0.4, -0.5],
    [-0.4, -0.4, -0.25, 0, 0, -0.25, -0.4, -0.4],
    [-0.3, -0.25, 0, 0.25, 0.25, 0, -0.25, -0.3],
    [-0.2, 0, 0.25, 0.5, 0.5, 0.25, 0, -0.2],
    [-0.2, 0, 0.25, 0.5, 0.5, 0.25, 0, -0.2],
    [-0.3, -0.25, 0, 0.25, 0.25, 0, -0.25, -0.3],
    [-0.4, -0.4, -0.25, 0, 0, -0.25, -0.4, -0.4],
    [-0.5, -0.4, -0.3, 0, 0, -0.3, -0.4, -0.5]
]

tabla_costo_reina = [
    [-0.8, -0.5, -0.5, -0.25, -0.25, -0.5, -0.5, -0.8],
    [-0.5,  0,    0,    0,     0,     0,    0,   -0.5],
    [-0.5,  0,    0.25, 0.5,   0.5,   0.25, 0,   -0.5],
    [-0.25, 0,    0.25, 0.5,   0.5,   0.25, 0,   -0.25],
    [ 0,    0,    0.25, 0.5,   0.5,   0.25, 0,   -0.25],
    [-0.5,  0.25, 0.25, 0.5,   0.5,   0.25, 0,   -0.5],
    [-0.5,  0,    0.25, 0,     0,     0,    0,   -0.5],
    [-0.8, -0.5, -0.5, -0.25, -0.25, -0.5, -0.5, -0.8]
]

tabla_costo_rey = [
    [-0.3, -0.4, -0.4, -0.5, -0.5, -0.4, -0.4, -0.3],
    [-0.3, -0.4, -0.4, -0.5, -0.5, -0.4, -0.4, -0.3],
    [-0.3, -0.4, -0.4, -0.5, -0.5, -0.4, -0.4, -0.3],
    [-0.3, -0.4, -0.4, -0.5, -0.5, -0.4, -0.4, -0.3],
    [-0.2, -0.3, -0.3, -0.4, -0.4, -0.3, -0.3, -0.2],
    [-0.1, -0.2, -0.2, -0.2, -0.2, -0.2, -0.2, -0.1],
    [ 0.2,  0.2,  0,    0,    0,    0,    0.2,  0.2],
    [ 0.2,  0.3,  0.1,  0,    0,    0.1,  0.3,  0.2]
]
tabla_costos = [
    tabla_costo_peon,
    tabla_costo_caballo,
    tabla_costo_alfil,
    tabla_costo_torre,
    tabla_costo_reina,
    tabla_costo_rey
]
def lista_movimientos_posibles(ficha):
    movimientos = ficha.movimientos_legales(piezas.board.tablero,piezas.board.tablero2)
    elems = []
    if movimientos:
        for mov in movimientos:
            elems.append([ficha.tipo, ficha.posicion, ficha.color, mov, ficha.dimension])
            
    return elems
def seleccionar_ficha(posicion, fichas):
    # Convertir la posición a fila y columna
    fila, columna = int(posicion[0]), int(posicion[1])
    
    for ficha in fichas:
        if ficha.posicion == (fila, columna):
            return ficha
    return None

def mover_ficha(ficha, nueva_posicion):
    return piezas.mover(ficha, nueva_posicion)
def evaluar_tablero():
    valor = 0
    for fila in piezas.board.tablero:
        for pieza in fila:
            if pieza:
                base_valor = pieza.valor
                if pieza.tipo == "Peon":
                    control_centro = tabla_costo_peon[pieza.posicion[0]][pieza.posicion[1]]
                elif pieza.tipo == "Caballo":
                    control_centro = tabla_costo_caballo[pieza.posicion[0]][pieza.posicion[1]]
                elif pieza.tipo == "Alfil":
                    control_centro = tabla_costo_alfil[pieza.posicion[0]][pieza.posicion[1]]
                elif pieza.tipo == "Torre":
                    control_centro = tabla_costo_torre[pieza.posicion[0]][pieza.posicion[1]]
                elif pieza.tipo == "Reina":
                    control_centro = tabla_costo_reina[pieza.posicion[0]][pieza.posicion[1]]
                elif pieza.tipo == "Rey":
                    control_centro = tabla_costo_rey[pieza.posicion[0]][pieza.posicion[1]]
                else:
                    control_centro = 0
                movilidad = len(pieza.movimientos_legales(piezas.board.tablero, piezas.board.tablero2))
                if pieza.color == "Blanco":
                    valor -= base_valor + control_centro + movilidad
                else:
                    valor += base_valor + control_centro + movilidad

    return valor
def minimax(tablero, profundidad, alfa, beta, maximizando):
    if profundidad == 0:
        return evaluar_tablero() + random.uniform(-0.5, 0.5)

    if maximizando:
        max_eval = -float('inf')
        for ficha in fichas_blancas:
            movimientos = ficha.movimientos_legales(tablero.tablero, tablero.tablero2)
            movimientos = filtrar_movimientos_prometedores(ficha, movimientos)
            for mov in movimientos:
                tablero_copia = tablero.copia_tablero()
                piezas.mover(ficha, mov, simular=True)
                eval = minimax(tablero_copia, profundidad - 1, alfa, beta, False)
                max_eval = max(max_eval, eval)
                alfa = max(alfa, eval)
                if beta <= alfa:
                    break
        return max_eval
    else:
        min_eval = float('inf')
        for ficha in fichas_negras:
            movimientos = ficha.movimientos_legales(tablero.tablero, tablero.tablero2)
            movimientos = filtrar_movimientos_prometedores(ficha, movimientos)
            for mov in movimientos:
                tablero_copia = tablero.copia_tablero()
                piezas.mover(ficha, mov, simular=True)
                eval = minimax(tablero_copia, profundidad - 1, alfa, beta, True)
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alfa:
                    break
        return min_eval
def mejor_movimiento():
    mejor_movimientos = []
    mejor_valor = float('inf')
    for ficha in fichas_negras:
        movimientos = ficha.movimientos_legales(piezas.board.tablero, piezas.board.tablero2)
        movimientos = filtrar_movimientos_prometedores(ficha, movimientos)
        for mov in movimientos:
            tablero_copia = piezas.board.copia_tablero()
            piezas.mover(ficha, mov, simular=True)
            valor = minimax(tablero_copia, 3, -float('inf'), float('inf'), True)
            if valor < mejor_valor:
                mejor_valor = valor
                mejor_movimientos = [(ficha, mov)]
            elif valor == mejor_valor:
                mejor_movimientos.append((ficha, mov))
    # Elegir aleatoriamente entre los mejores movimientos
    return random.choice(mejor_movimientos) if mejor_movimientos else None

TURNOS_SEMIALEATORIOS = 5
turno_actual = 0
def filtrar_movimientos_prometedores(ficha, movimientos, maximo=5):
    """
    Ordena los movimientos por prioridad y selecciona los más prometedores.
    Por ejemplo, prioriza capturas o movimientos hacia el centro.
    """
    if ficha.tipo == "Peon":
        tabla_costo = tabla_costo_peon
    elif ficha.tipo == "Caballo":
        tabla_costo = tabla_costo_caballo
    elif ficha.tipo == "Alfil":
        tabla_costo = tabla_costo_alfil
    elif ficha.tipo == "Torre":
        tabla_costo = tabla_costo_torre
    elif ficha.tipo == "Reina":
        tabla_costo = tabla_costo_reina
    elif ficha.tipo == "Rey":
        tabla_costo = tabla_costo_rey
    else:
        tabla_costo = [[0]*8 for _ in range(8)]  # Default to a neutral table if type is unknown

    movimientos_ordenados = sorted(
        movimientos, 
        key=lambda mov: tabla_costo[mov[0]][mov[1]], 
        reverse=True
    )
    return movimientos_ordenados[:maximo]  # Considera solo los 5 mejores movimientos

def movimiento_semi_aleatorio():
    """
    Selecciona un movimiento aleatorio de las piezas negras basado en sus movimientos legales.
    """
    movimientos_posibles = []
    for ficha in fichas_negras:
        movimientos = ficha.movimientos_legales(piezas.board.tablero, piezas.board.tablero2)
        for mov in movimientos:
            movimientos_posibles.append((ficha, mov))
    
    # Si hay movimientos posibles, elegir uno aleatoriamente
    if movimientos_posibles:
        return random.choice(movimientos_posibles)
    return None

#!# Bucle principal del juego
turno_blanco = True
while not piezas.finalizar_juego():
    os.system("cls")
    piezas.mostrar_tablero()
    if turno_blanco:
        # Turno del jugador blanco (movimiento aleatorio)
        movimientos_posibles = []
        for ficha in fichas_blancas:
            movimientos = ficha.movimientos_legales(piezas.board.tablero, piezas.board.tablero2)
            for mov in movimientos:
                movimientos_posibles.append((ficha, mov))
        
        if movimientos_posibles:
            while True:
                ficha, mov = random.choice(movimientos_posibles)
                if mover_ficha(ficha, mov):
                    print(f"Jugador blanco movió {ficha.tipo} a {mov}")
                    break
                
        # while True:
        #     if piezas.indicar_jaque():
        #         time.sleep(1)
        #     try:
        #         posicion = input("Introduce la posición de la ficha que quieres mover (ej. '12'): ")
        #         fila, columna = int(posicion[0]), int(posicion[1])
        #     except Exception as e:
        #         print("Error: Introduce una posición válida.")
        #         continue
        #     posicion = (fila, columna)
        #     ficha = seleccionar_ficha(posicion, fichas_blancas)
        #     if ficha:
        #         movimientos = lista_movimientos_posibles(ficha)
        #         if movimientos:
        #             print("Movimientos posibles: ", [mov[3] for mov in movimientos])
        #             try:
        #                 nueva_posicion = input("Introduce la nueva posición (ej. '12'): ")
        #                 fila, columna = int(nueva_posicion[0]), int(nueva_posicion[1])
        #             except Exception as e:
        #                 print("Error: Introduce una posición válida.")
        #                 continue
        #             nueva_posicion = (fila, columna)
        #             if mover_ficha(ficha, nueva_posicion):
        #                 print(f"Ficha movida a {nueva_posicion}")
        #                 break
        #             else:
        #                 print("Movimiento no válido.")
        #         else:
        #             print("No hay movimientos posibles para esta ficha.")
        #     else:
        #         print("Ficha no encontrada.")
    else:
        # Turno de la máquina
        if turno_actual < TURNOS_SEMIALEATORIOS:
            # Fase semialeatoria
            print("Turno semialeatorio de la máquina.")
            mejor_mov = movimiento_semi_aleatorio()
        else:
            # Fase de Minimax
            print("Turno estratégico de la máquina (Minimax).")
            mejor_mov = mejor_movimiento()
        
        if mejor_mov:
            ficha, mov = mejor_mov
            if mover_ficha(ficha, mov):
                print(f"Máquina movió {ficha.tipo} a {mov}")
    
    turno_actual += 1
    turno_blanco = not turno_blanco
print("Juego terminado.")
# Inicializar pygame mixer
pygame.mixer.init()

# Verificar si la inicialización fue exitosa
if not pygame.mixer.get_init():
    print("Error al inicializar el mixer de Pygame")
else:
    # Cargar el archivo mp3
    try:
        pygame.mixer.music.load(fr"src\audio\sonido.mp3")
    except pygame.error as e:
        print(f"Error al cargar el archivo de sonido: {e}")
    else:
        # Establecer el volumen (opcional)
        pygame.mixer.music.set_volume(1.0)  # Volumen máximo

        # Reproducir el archivo mp3
        pygame.mixer.music.play()

        # Mantener el programa en ejecución para escuchar el sonido
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)


print(f"Fichas restantes: ")

a = 0
for elem in piezas.board.tablero:
    for item in elem:
        if item:
            a += 1
print(f"Tablero 1: {a} fichas")
a = 0
for elem in piezas.board.tablero2:
    for item in elem:
        if item:
            a += 1
print(f"Tablero 2: {a} fichas")