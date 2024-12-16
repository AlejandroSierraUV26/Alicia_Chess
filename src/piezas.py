from src import tablero

class Pieza:
    def __init__(self, tipo, color, posicion, dimension, valor):
        self.tipo = tipo  # Tipo de pieza: "Rey", "Reina", "Torre", etc.
        self.color = color  # Color: "Blanco" o "Negro"
        self.posicion = posicion  # Tupla (fila, columna)
        self.dimension = dimension # 1 izquierda 2 derecha
        self.valor = valor
        self.img = None
    
    def movimientos_legales(self, tablero_actual, tablero_opuesto):
        """
        Este método será implementado en las subclases.
        Define los movimientos válidos según el tipo de pieza.
        """
        raise NotImplementedError
class Peon(Pieza):
    def __init__(self, color, posicion, dimension, valor):
        super().__init__("Peon", color, posicion, dimension, valor)
    
    def movimientos_legales(self, tablero_actual, tablero_opuesto):
        movimientos = []
        fila, columna = self.posicion
        if self.color == "Blanco":
            if self.dimension == 1:
                if fila + 1 < 8 and tablero_actual[fila + 1][columna] is None and tablero_opuesto[fila + 1][columna] is None:
                    movimientos.append((fila + 1, columna))
                if fila == 1 and tablero_actual[fila + 2][columna] is None and tablero_opuesto[fila + 2][columna] is None:
                    movimientos.append((fila + 2, columna))
                if fila + 1 < 8 and columna + 1 < 8 and tablero_actual[fila + 1][columna + 1] is not None and tablero_actual[fila + 1][columna + 1].color != self.color:
                    movimientos.append((fila + 1, columna + 1))
                if fila + 1 < 8 and columna - 1 >= 0 and tablero_actual[fila + 1][columna - 1] is not None and tablero_actual[fila + 1][columna - 1].color != self.color:
                    movimientos.append((fila + 1, columna - 1))
            else:
                if fila + 1 < 8 and tablero_opuesto[fila + 1][columna] is None and tablero_actual[fila + 1][columna] is None:
                    movimientos.append((fila + 1, columna))
                if fila == 1 and tablero_opuesto[fila + 2][columna] is None and tablero_actual[fila + 2][columna] is None:
                    movimientos.append((fila + 2, columna))
                if fila + 1 < 8 and columna + 1 < 8 and tablero_opuesto[fila + 1][columna + 1] is not None and tablero_opuesto[fila + 1][columna + 1].color != self.color:
                    movimientos.append((fila + 1, columna + 1))
                if fila + 1 < 8 and columna - 1 >= 0 and tablero_opuesto[fila + 1][columna - 1] is not None and tablero_opuesto[fila + 1][columna - 1].color != self.color:
                    movimientos.append((fila + 1, columna - 1))
        else:
            if self.dimension == 1:
                if fila - 1 >= 0 and tablero_actual[fila - 1][columna] is None and tablero_opuesto[fila - 1][columna] is None:
                    movimientos.append((fila - 1, columna))
                if fila == 6 and tablero_actual[fila - 2][columna] is None and tablero_opuesto[fila - 2][columna] is None:
                    movimientos.append((fila - 2, columna))
                if fila - 1 >= 0 and columna + 1 < 8 and tablero_actual[fila - 1][columna + 1] is not None and tablero_actual[fila - 1][columna + 1].color != self.color:
                    movimientos.append((fila - 1, columna + 1))
                if fila - 1 >= 0 and columna - 1 >= 0 and tablero_actual[fila - 1][columna - 1] is not None and tablero_actual[fila - 1][columna - 1].color != self.color:
                    movimientos.append((fila - 1, columna - 1))
            else:
                if fila - 1 >= 0 and tablero_opuesto[fila - 1][columna] is None and tablero_actual[fila - 1][columna] is None:
                    movimientos.append((fila - 1, columna))
                if fila == 6 and tablero_opuesto[fila - 2][columna] is None and tablero_actual[fila - 2][columna] is None:
                    movimientos.append((fila - 2, columna))
                if fila - 1 >= 0 and columna + 1 < 8 and tablero_opuesto[fila - 1][columna + 1] is not None and tablero_opuesto[fila - 1][columna + 1].color != self.color:
                    movimientos.append((fila - 1, columna + 1))
                if fila - 1 >= 0 and columna - 1 >= 0 and tablero_opuesto[fila - 1][columna - 1] is not None and tablero_opuesto[fila - 1][columna - 1].color != self.color:
                    movimientos.append((fila - 1, columna - 1))
        return movimientos
    def coronar(self):
        # Verificar si el peón se encuentra en la fila 0 o 7
        pass
    def en_passant(self):
        # Verificar si el peón puede realizar el movimiento en passant
        pass    
class Torre(Pieza):
    def __init__(self, color, posicion, dimension, valor):
        super().__init__("Torre", color, posicion, dimension, valor)
    
    def movimientos_legales(self, tablero_actual, tablero_opuesto):
        movimientos = []
        fila, columna = self.posicion
        # Movimientos verticales
        if self.dimension == 1:
            for i in range(fila + 1, 8):
                if tablero_actual[i][columna] is None:
                    movimientos.append((i, columna))
                elif tablero_actual[i][columna].color != self.color:
                    movimientos.append((i, columna))
                    # if tablero_actual[i][columna].tipo == "Rey":
                    #     continue
                    break
                else:
                    break

            for i in range(fila - 1, -1, -1):
                if tablero_actual[i][columna] is None:
                    movimientos.append((i, columna))
                elif tablero_actual[i][columna].color != self.color:
                    movimientos.append((i, columna))
                    # if tablero_actual[i][columna].tipo == "Rey":
                    #     continue
                    break
                else:
                    break

            # Movimientos horizontales
            for i in range(columna + 1, 8):
                if tablero_actual[fila][i] is None:
                    movimientos.append((fila, i))
                elif tablero_actual[fila][i].color != self.color:
                    movimientos.append((fila, i))
                    # if tablero_actual[fila][i].tipo == "Rey":
                    #     continue
                    
                    break
                else:
                    break

            for i in range(columna - 1, -1, -1):
                if tablero_actual[fila][i] is None:
                    movimientos.append((fila, i))
                elif tablero_actual[fila][i].color != self.color:
                    movimientos.append((fila, i))
                    # if tablero_actual[fila][i].tipo == "Rey":
                    #     continue
                    
                    break
                else:
                    break
                
                    
        else:
            for i in range(fila + 1, 8):
                if tablero_opuesto[i][columna] is None:
                    movimientos.append((i, columna))
                elif tablero_opuesto[i][columna].color != self.color:
                    movimientos.append((i, columna))
                    # if tablero_opuesto[i][columna].tipo == "Rey":
                    #     continue
                    break
                else:
                    break

            for i in range(fila - 1, -1, -1):
                if tablero_opuesto[i][columna] is None:
                    movimientos.append((i, columna))
                elif tablero_opuesto[i][columna].color != self.color:
                    movimientos.append((i, columna))
                    # if tablero_opuesto[i][columna].tipo == "Rey":
                    #     continue
                    break
                else:
                    break

            # Movimientos horizontales
            for i in range(columna + 1, 8):
                if tablero_opuesto[fila][i] is None:
                    movimientos.append((fila, i))
                elif tablero_opuesto[fila][i].color != self.color:
                    movimientos.append((fila, i))
                    # if tablero_opuesto[fila][i].tipo == "Rey":
                    #     continue
                    break
                else:
                    break

            for i in range(columna - 1, -1, -1):
                if tablero_opuesto[fila][i] is None:
                    movimientos.append((fila, i))
                elif tablero_opuesto[fila][i].color != self.color:
                    movimientos.append((fila, i))
                    # if tablero_opuesto[fila][i].tipo == "Rey":
                    #     continue
                    break
                else:
                    break
                
        return movimientos
class Caballo(Pieza):
    def __init__(self, color, posicion, dimension, valor):
        super().__init__("Caballo", color, posicion, dimension, valor)
    
    def movimientos_legales(self, tablero_actual, tablero_opuesto):
        movimientos = []
        fila, columna = self.posicion
        posibles_movimientos = [
                (fila + 2, columna + 1), (fila + 2, columna - 1),
                (fila - 2, columna + 1), (fila - 2, columna - 1),
                (fila + 1, columna + 2), (fila + 1, columna - 2),
                (fila - 1, columna + 2), (fila - 1, columna - 2)
            ]
        if self.dimension == 1:    
            for mov in posibles_movimientos:
                if 0 <= mov[0] < 8 and 0 <= mov[1] < 8:
                    pieza = tablero_actual[mov[0]][mov[1]]
                    if pieza is None or pieza.color != self.color:
                        movimientos.append(mov) 
        else:
            for mov in posibles_movimientos:
                if 0 <= mov[0] < 8 and 0 <= mov[1] < 8:
                    pieza = tablero_opuesto[mov[0]][mov[1]]
                    if pieza is None or pieza.color != self.color:
                        movimientos.append(mov)
        return movimientos
class Alfil(Pieza):
    def __init__(self, color, posicion, dimension, valor):
        super().__init__("Alfil", color, posicion, dimension, valor)
    
    def movimientos_legales(self, tablero_actual, tablero_opuesto):
        movimientos = []
        fila, columna = self.posicion
        if self.dimension == 1:
            tablero = tablero_actual
        else:
            tablero = tablero_opuesto
        # Dirección de movimiento del alfil: [arriba-derecha, arriba-izquierda, abajo-derecha, abajo-izquierda]
        direcciones = [(1, 1), (1, -1), (-1, 1), (-1, -1)]

        for dx, dy in direcciones:
            for i in range(1, 8):  # Máximo 7 pasos en el tablero
                nueva_fila = fila + i * dx
                nueva_columna = columna + i * dy
                if 0 <= nueva_fila < 8 and 0 <= nueva_columna < 8:  # Dentro de los límites del tablero
                    pieza = tablero[nueva_fila][nueva_columna]
                    if pieza is None:  # Celda vacía, movimiento válido
                        movimientos.append((nueva_fila, nueva_columna))
                    elif pieza.color != self.color:  # Celda ocupada por una pieza enemiga
                        movimientos.append((nueva_fila, nueva_columna))
                        # if pieza.tipo == "Rey":
                        #     continue
                        break  # El alfil no puede continuar después de capturar
                    else:  # Celda ocupada por una pieza aliada
                        break  # No puede continuar por piezas aliadas
                else:
                    break  # Fuera de los límites del tablero

        return movimientos
class Rey(Pieza):
    def __init__(self, color, posicion, dimension, valor):
        super().__init__("Rey", color, posicion, dimension, valor)
    
    def movimientos_legales(self, tablero_actual, tablero_opuesto):
        movimientos = []
        fila, columna = self.posicion
        if self.dimension == 1:
            tablero = tablero_actual
        else:
            tablero = tablero_opuesto
            
        posibles_movimientos = [
                (fila + 1, columna), (fila - 1, columna),
                (fila, columna + 1), (fila, columna - 1),
                (fila + 1, columna + 1), (fila + 1, columna - 1),
                (fila - 1, columna + 1), (fila - 1, columna - 1)
            ]
        for mov in posibles_movimientos:
            if 0 <= mov[0] < 8 and 0 <= mov[1] < 8:
                pieza = tablero[mov[0]][mov[1]]
                if pieza is None or pieza.color != self.color:
                    movimientos.append(mov)
        return movimientos
    def enroque(self, tablero_actual, tablero_opuesto):
        # Determinar si el rey ha movido
        # Determinar si la torre ha movido
        # Determinar si hay piezas entre el rey y la torre
        
        movimientos = []
        fila, columna = self.posicion

        if self.color == "Blanco":
            if self.dimension == 1:
                if self.posicion == (0, 4):
                    # Enroque corto
                    if isinstance(tablero_actual[0][7], Torre) and tablero_actual[0][7].dimension == 1:
                        if tablero_actual[0][5] is None and tablero_actual[0][6] is None:
                            movimientos.append((0, 6))
                    # Enroque largo
                    if isinstance(tablero_actual[0][0], Torre) and tablero_actual[0][0].dimension == 1:
                        if tablero_actual[0][1] is None and tablero_actual[0][2] is None and tablero_actual[0][3] is None:
                            movimientos.append((0, 2))
                else:
                    if self.posicion == (0, 4):
                        # Enroque corto
                        if isinstance(tablero_opuesto[0][7], Torre) and tablero_opuesto[0][7].dimension == 2:
                            if tablero_opuesto[0][5] is None and tablero_opuesto[0][6] is None:
                                movimientos.append((0, 6))
                    # Enroque largo
                    if isinstance(tablero_opuesto[0][0], Torre) and tablero_opuesto[0][0].dimension == 2:
                        if tablero_opuesto[0][1] is None and tablero_opuesto[0][2] is None and tablero_opuesto[0][3] is None:
                            movimientos.append((0, 2))
        else:
            if self.dimension == 1:
                if self.posicion == (7, 4):
                    # Enroque corto
                    if isinstance(tablero_actual[7][7], Torre) and tablero_actual[7][7].dimension == 1:
                        if tablero_actual[7][5] is None and tablero_actual[7][6] is None:
                            movimientos.append((7, 6))
                    # Enroque largo
                    if isinstance(tablero_actual[7][0], Torre) and tablero_actual[7][0].dimension == 1:
                        if tablero_actual[7][1] is None and tablero_actual[7][2] is None and tablero_actual[7][3] is None:
                            movimientos.append((7, 2))
                else:
                    if self.posicion == (7, 4):
                    # Enroque corto
                        if isinstance(tablero_opuesto[7][7], Torre) and tablero_opuesto[7][7].dimension == 2:
                            if tablero_opuesto[7][5] is None and tablero_opuesto[7][6] is None:
                                movimientos.append((7, 6))
                        # Enroque largo
                        if isinstance(tablero_opuesto[7][0], Torre) and tablero_opuesto[7][0].dimension == 2:
                            if tablero_opuesto[7][1] is None and tablero_opuesto[7][2] is None and tablero_opuesto[7][3] is None:
                                movimientos.append((7, 2))
        return movimientos
    
    def jaque(self, tablero_actual, tablero_opuesto):
        # Sacar todas las casillas que ocupan los enemigos
        for pieza in fichas:
            if pieza.color != self.color:
                movimientos_enemigos = pieza.movimientos_legales(tablero_actual, tablero_opuesto)
                if self.posicion in movimientos_enemigos:
                    return True
    def jaque_mate(self, tablero_actual, tablero_opuesto):
        return True
    
    def ahogado(self):
        # Verificar si el rey está ahogado
        pass  
class Reina(Pieza):
    def __init__(self, color, posicion, dimension, valor):
        super().__init__("Dama", color, posicion, dimension, valor)
    
    def movimientos_legales(self, tablero_actual, tablero_opuesto):
        movimientos = []
        fila, columna = self.posicion
        
        if self.dimension == 1:
            tablero = tablero_actual
        else:
            tablero = tablero_opuesto
            

        # Movimientos como Torre
        for i in range(fila + 1, 8):
            if tablero[i][columna] is None:
                movimientos.append((i, columna))
            elif tablero[i][columna].color != self.color:
                movimientos.append((i, columna))
                # if tablero[i][columna].tipo == "Rey":
                #     continue
                break
            else:
                break

        for i in range(fila - 1, -1, -1):
            if tablero[i][columna] is None:
                movimientos.append((i, columna))
            elif tablero[i][columna].color != self.color:
                movimientos.append((i, columna))
                # if tablero[i][columna].tipo == "Rey":
                #     continue
                break
            else:
                break

        for i in range(columna + 1, 8):
            if tablero[fila][i] is None:
                movimientos.append((fila, i))
            elif tablero[fila][i].color != self.color:
                movimientos.append((fila, i))
                # if tablero[fila][i].tipo == "Rey":
                #     continue
                break
            else:
                break

        for i in range(columna - 1, -1, -1):
            if tablero[fila][i] is None:
                movimientos.append((fila, i))
            elif tablero[fila][i].color != self.color:
                movimientos.append((fila, i))
                # if tablero[fila][i].tipo == "Rey":
                #     continue
                break
            else:
                break

        # Movimientos como Alfil
        for i in range(1, 8):
            if fila + i < 8 and columna + i < 8:
                if tablero[fila + i][columna + i] is None:
                    movimientos.append((fila + i, columna + i))
                elif tablero[fila + i][columna + i].color != self.color:
                    movimientos.append((fila + i, columna + i))
                    # if tablero[fila + i][columna + i].tipo == "Rey":
                    #     continue
                    break
                else:
                    break
            else:
                break

        for i in range(1, 8):
            if fila + i < 8 and columna - i >= 0:
                if tablero[fila + i][columna - i] is None:
                    movimientos.append((fila + i, columna - i))
                elif tablero[fila + i][columna - i].color != self.color:
                    movimientos.append((fila + i, columna - i))
                    # if tablero[fila + i][columna - i].tipo == "Rey":
                    #     continue
                    break
                else:
                    break
            else:
                break

        for i in range(1, 8):
            if fila - i >= 0 and columna + i < 8:
                if tablero[fila - i][columna + i] is None:
                    movimientos.append((fila - i, columna + i))
                elif tablero[fila - i][columna + i].color != self.color:
                    movimientos.append((fila - i, columna + i))
                    # if tablero[fila - i][columna + i].tipo == "Rey":
                    #     continue
                    break
                else:
                    break
            else:
                break

        for i in range(1, 8):
            if fila - i >= 0 and columna - i >= 0:
                if tablero[fila - i][columna - i] is None:
                    movimientos.append((fila - i, columna - i))
                elif tablero[fila - i][columna - i].color != self.color:
                    movimientos.append((fila - i, columna - i))
                    # if tablero[fila - i][columna - i].tipo == "Rey":
                    #     continue
                    break
                else:
                    break
            else:
                break

        return movimientos

def inicializar_piezas():
    global board
    global fichas
    
    board = tablero.Tablero()
    
    fichas = []
    # Crear piezas blancas
    fichas.append(Torre("Blanco", (0, 0), 1, 5))
    fichas.append(Caballo("Blanco", (0, 1), 1, 3))
    fichas.append(Alfil("Blanco", (0, 2), 1, 3))
    fichas.append(Reina("Blanco", (0, 3), 1, 9))
    fichas.append(Rey("Blanco", (0, 4), 1, 100))
    fichas.append(Alfil("Blanco", (0, 5), 1, 3))
    fichas.append(Caballo("Blanco", (0, 6), 1, 3))
    fichas.append(Torre("Blanco", (0, 7), 1, 5))
    for _ in range(8):
        fichas.append(Peon("Blanco", (1, _), 1, 1))
    
        
    # Crear piezas negras
    fichas.append(Torre("Negro", (7,0), 1, 5))   
    fichas.append(Caballo("Negro", (7,1), 1, 3))
    fichas.append(Alfil("Negro", (7,2), 1, 3))
    fichas.append(Reina("Negro", (7,3), 1, 9))
    fichas.append(Rey("Negro", (7,4), 1, 100))
    fichas.append(Alfil("Negro", (7,5), 1, 3))
    fichas.append(Caballo("Negro", (7,6), 1, 3))
    fichas.append(Torre("Negro", (7,7), 1, 5))
    for _ in range(8):
        fichas.append(Peon("Negro", (6, _), 1, 1))

    inicializar_tablero(fichas)
    
    

def inicializar_tablero(piezas):
    for i in range(len(piezas)):
        board.agregar_ficha(piezas[i], piezas[i].posicion)
    

def mostrar_tablero():
    board.mostrar()
def obtener_tableros():
    return board.tablero, board.tablero2
def buscar_ficha(posicion):
    for pieza in fichas:
        if pieza.posicion == posicion:
            return pieza
    return None

def buscar_ficha_general(posicion, piezas):
    for pieza in piezas:
        if pieza.posicion == posicion:
            return pieza
    return None

def mover(ficha, posicion, simular=False):
    if board.tablero[posicion[0]][posicion[1]] is not None and board.tablero2[posicion[0]][posicion[1]] is not None:
        return False
    rey = next((pieza for pieza in fichas if isinstance(pieza, Rey) and pieza.color == ficha.color), None)

    if ficha.color != rey.color:
        if posicion in ficha.movimientos_legales(board.tablero, board.tablero2):
            if simular:
                return True
            ficha_enemiga = buscar_ficha_general(posicion, board.fichas_oponentes(ficha.color, ficha.dimension))
            if ficha_enemiga:
                board.eliminar_ficha(ficha_enemiga, posicion)
                print("Eliminado : {}".format(ficha_enemiga.tipo, ficha_enemiga.posicion, ficha_enemiga.color))
                if ficha_enemiga in fichas:
                    fichas.remove(ficha_enemiga)
            board.mover_ficha(ficha, posicion)
            return True
        else:
            return False

    if rey and rey.jaque(board.tablero, board.tablero2):
        movimientos_defensivos = []
        fichas_defensivas = []

        if rey.dimension == 1:
            tablero = board.tablero
        else:
            tablero = board.tablero2

        movimientos_para_defender = []
        fichas_defensivas = []

        for pieza in fichas:
            if pieza.color != rey.color:
                movimientos_para_defender.extend(pieza.movimientos_legales(tablero, board.tablero2))
            else:
                fichas_defensivas.extend(pieza.movimientos_legales(tablero, board.tablero2))

        diferencia_simetrica = set(fichas_defensivas).difference(movimientos_para_defender).intersection(rey.movimientos_legales(tablero, board.tablero2))
        print(diferencia_simetrica)
        if movimientos_para_defender == fichas_defensivas:
            print("No se puede defender")
            return False
        if ficha.color == rey.color:
            if ficha.tipo == "Rey":
                if posicion in diferencia_simetrica:
                    if simular:
                        return True
                    board.mover_ficha(ficha, posicion)
                    return True
                else:
                    return False
            else:
                if posicion in diferencia_simetrica:
                    if simular:
                        return True
                    board.mover_ficha(ficha, posicion)
                    return True
                else:
                    return False

    if not rey.jaque(board.tablero, board.tablero2):
        if isinstance(ficha, Rey):
            enroque_movimientos = ficha.enroque(board.tablero, board.tablero2)
            if posicion in enroque_movimientos:
                if simular:
                    return True
                if posicion[1] == 6:
                    torre = buscar_ficha((posicion[0], 7))
                    board.mover_ficha(torre, (posicion[0], 5))
                elif posicion[1] == 2:
                    torre = buscar_ficha((posicion[0], 0))
                    board.mover_ficha(torre, (posicion[0], 3))
                board.mover_ficha(ficha, posicion)
                return True
        if posicion in ficha.movimientos_legales(board.tablero, board.tablero2):
            if simular:
                return True
            ficha_enemiga = buscar_ficha_general(posicion, board.fichas_oponentes(ficha.color, ficha.dimension))
            if ficha_enemiga:
                board.eliminar_ficha(ficha_enemiga, posicion)
                print(f"Eliminado : {ficha_enemiga.tipo} {ficha_enemiga.posicion} {ficha_enemiga.color}")
                if ficha_enemiga in fichas:
                    fichas.remove(ficha_enemiga)
            board.mover_ficha(ficha, posicion)
            return True
        else:
            return False
    else:
        return False
def movimientos_posibles(ficha):
    print(ficha.movimientos_legales(board.tablero, board.tablero2))
    
def indicar_jaque():    
    for pieza in fichas:
        if isinstance(pieza, Rey):
            if pieza.jaque(board.tablero, board.tablero2):
                print(f"El rey {pieza.color} está en jaque.")
                return True
    return False

def indicar_jaque_mate():
    for pieza in fichas:
        if isinstance(pieza, Rey):
            if pieza.jaque_mate(board.tablero, board.tablero2):
                # print(f"El rey {pieza.color} está en jaque mate y ha perdido.")
                return True
    return False

def finalizar_juego():
    # Si uno de los reyes es eliminado indicar que el juego ha terminado
    reyes = [pieza for pieza in fichas if isinstance(pieza, Rey)]
    if len(reyes) < 2:
        return True
    return False


def obtener_ficha_jaque():
    rey = next((pieza for pieza in fichas if isinstance(pieza, Rey)), None)
    fichas_jaque = []
    for pieza in fichas:
        if pieza.color != rey.color:
            movimientos_enemigos = pieza.movimientos_legales(board.tablero, board.tablero2)
            if rey.posicion in movimientos_enemigos:
                fichas_jaque.append(pieza)
    return fichas_jaque