import tablero

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
    def mover_ficha(self):
        """
        Metodo para mover ficha, de un tablero a otro 
        """
        pass

class Peon(Pieza):
    def __init__(self, color, posicion):
        super().__init__("Peón", color, posicion)
    
    def movimientos_legales(self, tablero_actual, tablero_opuesto):
        # Implementar lógica de movimientos específicos para el peón
        movimientos = []
        # Ejemplo de lógica básica: avanzar un paso si la casilla está vacía
        # y manejar el cambio de tablero.
        return movimientos

class Torre(Pieza):
    def __init__(self, color, posicion):
        super().__init__("Torre", color, posicion)
    
    def movimientos_legales(self, tablero_actual, tablero_opuesto):
        # Lógica para movimientos horizontales y verticales
        movimientos = []
        return movimientos

class Caballo(Pieza):
    def __init__(self, color, posicion):
        super().__init__("Caballo", color, posicion)
    
    def movimientos_legales(self, tablero_actual, tablero_opuesto):
        # Lógica para movimientos en L
        movimientos = []
        return movimientos

class Alfil(Pieza):
    def __init__(self, color, posicion):
        super().__init__("Alfil", color, posicion)
    
    def movimientos_legales(self, tablero_actual, tablero_opuesto):
        # Lógica para movimientos diagonales
        movimientos = []
        return movimientos

class Rey(Pieza):
    def __init__(self, color, posicion):
        super().__init__("Rey", color, posicion)
    
    def movimientos_legales(self, tablero_actual, tablero_opuesto):
        # Lógica para movimientos en todas las direcciones
        movimientos = []
        return movimientos
    
class Reina(Pieza):
    def __init__(self, color, posicion):
        super().__init__("Reina", color, posicion)
    
    def movimientos_legales(self, tablero_actual, tablero_opuesto):
        # Lógica para movimientos en todas las direcciones
        movimientos = []
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
    board = tablero.Tablero()
    for i in range(len(piezas)):
        board.agregar_ficha(piezas[i], piezas[i].posicion)
    board.mostrar()
    

inicializar_piezas()
    



    