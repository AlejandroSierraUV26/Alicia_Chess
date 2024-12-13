from src import tablero

class Pieza:
    def __init__(self, tipo, color, posicion, dimension):
        self.tipo = tipo  # Tipo de pieza: "Rey", "Reina", "Torre", etc.
        self.color = color  # Color: "Blanco" o "Negro"
        self.posicion = posicion  # Tupla (fila, columna)
        self.dimension = dimension # 1 izquierda 2 derecha
    
    def movimientos_legales(self, tablero_actual, tablero_opuesto):
        """
        Este método será implementado en las subclases.
        Define los movimientos válidos según el tipo de pieza.
        """
        raise NotImplementedError
class Peon(Pieza):
    def __init__(self, color, posicion, dimension):
        super().__init__("Peón", color, posicion, dimension)
    
    def movimientos_legales(self, tablero_actual, tablero_opuesto):
        movimientos = []
        fila, columna = self.posicion
        if self.color == "Blanco":
            if self.dimension == 1:    
                if fila + 1 < 8 and tablero_actual[fila + 1][columna] is None:
                    movimientos.append((fila + 1, columna))
                    if fila == 1 and tablero_actual[fila + 2][columna] is None:
                        movimientos.append((fila + 2, columna))
                if fila + 1 < 8 and columna + 1 < 8 and tablero_actual[fila + 1][columna + 1] is not None and tablero_actual[fila + 1][columna + 1].color != self.color:
                    movimientos.append((fila + 1, columna + 1))        
                if fila + 1 < 8 and columna - 1 >= 0 and tablero_actual[fila + 1][columna - 1] is not None and tablero_actual[fila + 1][columna - 1].color != self.color:
                    movimientos.append((fila + 1, columna - 1))    
            else:        
                if fila + 1 < 8 and tablero_opuesto[fila + 1][columna] is None:
                    movimientos.append((fila + 1, columna))
                    if fila == 1 and tablero_opuesto[fila + 2][columna] is None:
                        movimientos.append((fila + 2, columna))    
                if fila + 1 < 8 and columna + 1 < 8 and tablero_opuesto[fila + 1][columna + 1] is not None and tablero_opuesto[fila + 1][columna + 1].color != self.color:
                    movimientos.append((fila + 1, columna + 1))
        
                if fila + 1 < 8 and columna - 1 >= 0 and tablero_opuesto[fila + 1][columna - 1] is not None and tablero_opuesto[fila + 1][columna - 1].color != self.color:
                    movimientos.append((fila + 1, columna - 1))
        else:
            if self.dimension == 1:   
                if fila - 1 >= 0 and tablero_actual[fila - 1][columna] is None:
                    movimientos.append((fila - 1, columna))
                    if fila == 6 and tablero_actual[fila - 2][columna] is None:
                        movimientos.append((fila - 2, columna))
                if fila - 1 >= 0 and columna + 1 < 8 and tablero_actual[fila - 1][columna + 1] is not None and tablero_actual[fila - 1][columna + 1].color != self.color:
                    movimientos.append((fila - 1, columna + 1))
                if fila - 1 >= 0 and columna - 1 >= 0 and tablero_actual[fila - 1][columna - 1] is not None and tablero_actual[fila - 1][columna - 1].color != self.color:
                    movimientos.append((fila - 1, columna - 1))
            else:
                if fila - 1 >= 0 and tablero_opuesto[fila - 1][columna] is None:
                    movimientos.append((fila - 1, columna))
                    if fila == 6 and tablero_opuesto[fila - 2][columna] is None:
                        movimientos.append((fila - 2, columna))
                if fila - 1 >= 0 and columna + 1 < 8 and tablero_opuesto[fila - 1][columna + 1] is not None and tablero_opuesto[fila - 1][columna + 1].color != self.color:
                    movimientos.append((fila - 1, columna + 1))
                if fila - 1 >= 0 and columna - 1 >= 0 and tablero_opuesto[fila - 1][columna - 1] is not None and tablero_opuesto[fila - 1][columna - 1].color != self.color:
                    movimientos.append((fila - 1, columna - 1))
        return movimientos

class Torre(Pieza):
    def __init__(self, color, posicion, dimension):
        super().__init__("Torre", color, posicion, dimension)
    
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
                
                    
        else:
            for i in range(fila + 1, 8):
                if tablero_opuesto[i][columna] is None:
                    movimientos.append((i, columna))
                elif tablero_opuesto[i][columna].color != self.color:
                    movimientos.append((i, columna))
                    break
                else:
                    break

            for i in range(fila - 1, -1, -1):
                if tablero_opuesto[i][columna] is None:
                    movimientos.append((i, columna))
                elif tablero_opuesto[i][columna].color != self.color:
                    movimientos.append((i, columna))
                    break
                else:
                    break

            # Movimientos horizontales
            for i in range(columna + 1, 8):
                if tablero_opuesto[fila][i] is None:
                    movimientos.append((fila, i))
                elif tablero_opuesto[fila][i].color != self.color:
                    movimientos.append((fila, i))
                    break
                else:
                    break

            for i in range(columna - 1, -1, -1):
                if tablero_opuesto[fila][i] is None:
                    movimientos.append((fila, i))
                elif tablero_opuesto[fila][i].color != self.color:
                    movimientos.append((fila, i))
                    break
                else:
                    break
                
        return movimientos

class Caballo(Pieza):
    def __init__(self, color, posicion, dimension):
        super().__init__("Caballo", color, posicion, dimension)
    
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
    def __init__(self, color, posicion, dimension):
        super().__init__("Alfil", color, posicion, dimension)
    
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
    def __init__(self, color, posicion, dimension):
        super().__init__("Rey", color, posicion, dimension)
    
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
    def __init__(self, color, posicion, dimension):
        super().__init__("Dama", color, posicion, dimension)
    
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
    global board
    global fichas
    
    board = tablero.Tablero()
    
    fichas = []
    # Crear piezas blancas
    fichas.append(Torre("Blanco", (0, 0), 1))
    fichas.append(Caballo("Blanco", (0, 1), 1))
    fichas.append(Alfil("Blanco", (0, 2), 1))
    fichas.append(Reina("Blanco", (0, 3), 1))
    fichas.append(Rey("Blanco", (0, 4), 1))
    fichas.append(Alfil("Blanco", (0, 5), 1))
    fichas.append(Caballo("Blanco", (0, 6), 1))
    fichas.append(Torre("Blanco", (0, 7), 1))
    for _ in range(8):
        fichas.append(Peon("Blanco", (1, _), 1))
        
    # Crear piezas negras
    fichas.append(Torre("Negro", (7,0), 1))   
    fichas.append(Caballo("Negro", (7,1), 1))
    fichas.append(Alfil("Negro", (7,2), 1))
    fichas.append(Reina("Negro", (7,3), 1))
    fichas.append(Rey("Negro", (7,4), 1))
    fichas.append(Alfil("Negro", (7,5), 1))
    fichas.append(Caballo("Negro", (7,6), 1))
    fichas.append(Torre("Negro", (7,7), 1))
    for _ in range(8):
        fichas.append(Peon("Negro", (6, _), 1))

    inicializar_tablero(fichas)
    
    

def inicializar_tablero(piezas):
    for i in range(len(piezas)):
        board.agregar_ficha(piezas[i], piezas[i].posicion)
    

def mostrar_tablero():
    board.mostrar()
    
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

def mover(ficha, posicion):
    if posicion in ficha.movimientos_legales(board.tablero, board.tablero2):
        ficha_enemiga = buscar_ficha_general(posicion, board.fichas_oponentes(ficha.color,ficha.dimension))
        if ficha_enemiga:
            board.eliminar_ficha(ficha_enemiga, posicion)
            fichas.remove(ficha_enemiga)
            print("Eliminado")
        board.mover_ficha(ficha, posicion)
    else:
        print("Movimiento no válido para la ficha seleccionada.")
def movimientos_posibles(ficha):
    print(ficha.movimientos_legales(board.tablero, board.tablero2))