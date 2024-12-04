from src import tablero

class Pieza:
    def __init__(self, tipo, color, posicion):
        self.tipo = tipo  # Tipo de pieza: "Rey", "Reina", "Torre", etc.
        self.color = color  # Color: "Blanco" o "Negro"
        self.posicion = posicion  # Tupla (fila, columna)
    
    def movimientos_legales(self, tablero_actual, tablero_opuesto):
        """
        Este método será implementado en las subclases.
        Define los movimientos válidos según el tipo de pieza.
        """
        raise NotImplementedError

class Peon(Pieza):
    def __init__(self, color, posicion):
        super().__init__("Peón", color, posicion)
    
    def movimientos_legales(self, tablero_actual, tablero_opuesto):
        movimientos = []
        fila, columna = self.posicion
        if self.color == "Blanco":
            if fila + 1 < 8 and tablero_actual[fila + 1][columna] is None and tablero_opuesto[fila + 1][columna] is None:
                movimientos.append((fila + 1, columna))
                if fila == 1 and tablero_actual[fila + 2][columna] is None and tablero_opuesto[fila + 2][columna] is None and tablero_actual[fila + 1][columna] is None and tablero_opuesto[fila + 1][columna] is None:
                    movimientos.append((fila + 2, columna))
            if fila + 1 < 8 and columna + 1 < 8 and tablero_actual[fila + 1][columna + 1] is not None and tablero_actual[fila + 1][columna + 1].color != self.color:
                movimientos.append((fila + 1, columna + 1))
            if fila + 1 < 8 and columna - 1 >= 0 and tablero_actual[fila + 1][columna - 1] is not None and tablero_actual[fila + 1][columna - 1].color != self.color:
                movimientos.append((fila + 1, columna - 1))
        else:
            if fila - 1 >= 0 and tablero_actual[fila - 1][columna] is None and tablero_opuesto[fila - 1][columna] is None:
                movimientos.append((fila - 1, columna))
                if fila == 6 and tablero_actual[fila - 2][columna] is None and tablero_opuesto[fila - 2][columna] is None and tablero_actual[fila - 1][columna] is None and tablero_opuesto[fila - 1][columna] is None:
                    movimientos.append((fila - 2, columna))
            if fila - 1 >= 0 and columna + 1 < 8 and tablero_actual[fila - 1][columna + 1] is not None and tablero_actual[fila - 1][columna + 1].color != self.color:
                movimientos.append((fila - 1, columna + 1))
            if fila - 1 >= 0 and columna - 1 >= 0 and tablero_actual[fila - 1][columna - 1] is not None and tablero_actual[fila - 1][columna - 1].color != self.color:
                movimientos.append((fila - 1, columna - 1))
        return movimientos

class Torre(Pieza):
    def __init__(self, color, posicion):
        super().__init__("Torre", color, posicion)
    
    def movimientos_legales(self, tablero_actual, tablero_opuesto):
        movimientos = []
        fila, columna = self.posicion

        # Movimientos verticales
        for i in range(fila + 1, 8):
            if tablero_actual[i][columna] is None:
                movimientos.append((i, columna))
            elif tablero_actual[i][columna].color != self.color:
                movimientos.append((i, columna))
                break
            else:
                break

        for i in range(fila - 1, -1, -1):
            if tablero_actual[i][columna] is None:
                movimientos.append((i, columna))
            elif tablero_actual[i][columna].color != self.color:
                movimientos.append((i, columna))
                break
            else:
                break

        # Movimientos horizontales
        for i in range(columna + 1, 8):
            if tablero_actual[fila][i] is None:
                movimientos.append((fila, i))
            elif tablero_actual[fila][i].color != self.color:
                movimientos.append((fila, i))
                break
            else:
                break

        for i in range(columna - 1, -1, -1):
            if tablero_actual[fila][i] is None:
                movimientos.append((fila, i))
            elif tablero_actual[fila][i].color != self.color:
                movimientos.append((fila, i))
                break
            else:
                break
            
                
        print(len(movimientos))
        return movimientos

class Caballo(Pieza):
    def __init__(self, color, posicion):
        super().__init__("Caballo", color, posicion)
    
    def movimientos_legales(self, tablero_actual, tablero_opuesto):
        movimientos = []
        fila, columna = self.posicion
        posibles_movimientos = [
            (fila + 2, columna + 1), (fila + 2, columna - 1),
            (fila - 2, columna + 1), (fila - 2, columna - 1),
            (fila + 1, columna + 2), (fila + 1, columna - 2),
            (fila - 1, columna + 2), (fila - 1, columna - 2)
        ]
        for mov in posibles_movimientos:
            if 0 <= mov[0] < 8 and 0 <= mov[1] < 8:
                pieza = tablero_actual[mov[0]][mov[1]]
                if pieza is None or pieza.color != self.color:
                    movimientos.append(mov)
        return movimientos

class Alfil(Pieza):
    def __init__(self, color, posicion):
        super().__init__("Alfil", color, posicion)
    
    def movimientos_legales(self, tablero_actual, tablero_opuesto):
        movimientos = []
        fila, columna = self.posicion
        for i in range(1, 8):
            if fila + i < 8 and columna + i < 8:
                if tablero_actual[fila + i][columna + i] is None:
                    movimientos.append((fila + i, columna + i))
                elif tablero_actual[fila + i][columna + i].color != self.color:
                    movimientos.append((fila + i, columna + i))
                    break
                else:
                    break
            else:
                break

        for i in range(1, 8):
            if fila + i < 8 and columna - i >= 0:
                if tablero_actual[fila + i][columna - i] is None:
                    movimientos.append((fila + i, columna - i))
                elif tablero_actual[fila + i][columna - i].color != self.color:
                    movimientos.append((fila + i, columna - i))
                    break
                else:
                    break
            else:
                break

        for i in range(1, 8):
            if fila - i >= 0 and columna + i < 8:
                if tablero_actual[fila - i][columna + i] is None:
                    movimientos.append((fila - i, columna + i))
                elif tablero_actual[fila - i][columna + i].color != self.color:
                    movimientos.append((fila - i, columna + i))
                    break
                else:
                    break
            else:
                break

        for i in range(1, 8):
            if fila - i >= 0 and columna - i >= 0:
                if tablero_actual[fila - i][columna - i] is None:
                    movimientos.append((fila - i, columna - i))
                elif tablero_actual[fila - i][columna - i].color != self.color:
                    movimientos.append((fila - i, columna - i))
                    break
                else:
                    break
            else:
                break

        return movimientos

class Rey(Pieza):
    def __init__(self, color, posicion):
        super().__init__("Rey", color, posicion)
    
    def movimientos_legales(self, tablero_actual, tablero_opuesto):
        movimientos = []
        fila, columna = self.posicion
        posibles_movimientos = [
            (fila + 1, columna), (fila - 1, columna),
            (fila, columna + 1), (fila, columna - 1),
            (fila + 1, columna + 1), (fila + 1, columna - 1),
            (fila - 1, columna + 1), (fila - 1, columna - 1)
        ]
        for mov in posibles_movimientos:
            if 0 <= mov[0] < 8 and 0 <= mov[1] < 8:
                pieza = tablero_actual[mov[0]][mov[1]]
                if pieza is None or pieza.color != self.color:
                    movimientos.append(mov)
        return movimientos
class Reina(Pieza):
    def __init__(self, color, posicion):
        super().__init__("Dama", color, posicion)
    
    def movimientos_legales(self, tablero_actual, tablero_opuesto):
        movimientos = []
        fila, columna = self.posicion

        # Movimientos como Torre
        for i in range(fila + 1, 8):
            if tablero_actual[i][columna] is None:
                movimientos.append((i, columna))
            elif tablero_actual[i][columna].color != self.color:
                movimientos.append((i, columna))
                break
            else:
                break

        for i in range(fila - 1, -1, -1):
            if tablero_actual[i][columna] is None:
                movimientos.append((i, columna))
            elif tablero_actual[i][columna].color != self.color:
                movimientos.append((i, columna))
                break
            else:
                break

        for i in range(columna + 1, 8):
            if tablero_actual[fila][i] is None:
                movimientos.append((fila, i))
            elif tablero_actual[fila][i].color != self.color:
                movimientos.append((fila, i))
                break
            else:
                break

        for i in range(columna - 1, -1, -1):
            if tablero_actual[fila][i] is None:
                movimientos.append((fila, i))
            elif tablero_actual[fila][i].color != self.color:
                movimientos.append((fila, i))
                break
            else:
                break

        # Movimientos como Alfil
        for i in range(1, 8):
            if fila + i < 8 and columna + i < 8:
                if tablero_actual[fila + i][columna + i] is None:
                    movimientos.append((fila + i, columna + i))
                elif tablero_actual[fila + i][columna + i].color != self.color:
                    movimientos.append((fila + i, columna + i))
                    break
                else:
                    break
            else:
                break

        for i in range(1, 8):
            if fila + i < 8 and columna - i >= 0:
                if tablero_actual[fila + i][columna - i] is None:
                    movimientos.append((fila + i, columna - i))
                elif tablero_actual[fila + i][columna - i].color != self.color:
                    movimientos.append((fila + i, columna - i))
                    break
                else:
                    break
            else:
                break

        for i in range(1, 8):
            if fila - i >= 0 and columna + i < 8:
                if tablero_actual[fila - i][columna + i] is None:
                    movimientos.append((fila - i, columna + i))
                elif tablero_actual[fila - i][columna + i].color != self.color:
                    movimientos.append((fila - i, columna + i))
                    break
                else:
                    break
            else:
                break

        for i in range(1, 8):
            if fila - i >= 0 and columna - i >= 0:
                if tablero_actual[fila - i][columna - i] is None:
                    movimientos.append((fila - i, columna - i))
                elif tablero_actual[fila - i][columna - i].color != self.color:
                    movimientos.append((fila - i, columna - i))
                    break
                else:
                    break
            else:
                break

        return movimientos

def inicializar_piezas():
    piezas = []
    # Crear piezas blancas
    piezas.append(Torre("Blanco", (0, 0)))
    piezas.append(Caballo("Blanco", (0, 1)))
    piezas.append(Alfil("Blanco", (0, 2)))
    piezas.append(Reina("Blanco", (0, 3)))
    piezas.append(Rey("Blanco", (0, 4)))
    piezas.append(Alfil("Blanco", (0, 5)))
    piezas.append(Caballo("Blanco", (0, 6)))
    piezas.append(Torre("Blanco", (0, 7)))
    for _ in range(8):
        piezas.append(Peon("Blanco", (1, _)))
        
    # Crear piezas negras
    piezas.append(Torre("Negro", (7,0)))   
    piezas.append(Caballo("Negro", (7,1)))
    piezas.append(Alfil("Negro", (7,2)))
    piezas.append(Reina("Negro", (7,3)))
    piezas.append(Rey("Negro", (7,4)))
    piezas.append(Alfil("Negro", (7,5)))
    piezas.append(Caballo("Negro", (7,6)))
    piezas.append(Torre("Negro", (7,7)))
    for _ in range(8):
        piezas.append(Peon("Negro", (6, _)))
    # for i in range(len(piezas)):
    #     print(f"{piezas[i].tipo} : {piezas[i].color}")
    inicializar_tablero(piezas)
    return piezas

def inicializar_tablero(piezas):
    global board
    board = tablero.Tablero()
    for i in range(len(piezas)):
        board.agregar_ficha(piezas[i], piezas[i].posicion)
    

def mostrar_tablero():
    board.mostrar()
    
def buscar_ficha(posicion, fichas):
    for pieza in fichas:
        if pieza.posicion == posicion:
            return pieza
    return None


def mover(ficha, posicion):
    if posicion in ficha.movimientos_legales(board.tablero, board.tablero2):
        board.mover_ficha(ficha, posicion)
    else:
        print("Movimiento no válido para la ficha seleccionada.")
def movimientos_posibles(ficha):
    print(ficha.movimientos_legales(board.tablero, board.tablero2))