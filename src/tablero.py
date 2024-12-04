class Tablero:
    def __init__(self):
        # Matriz 8x8 que representa el tablero
        self.tablero = [[None for _ in range(8)] for _ in range(8)]
        self.tablero2 = [[None for _ in range(8)] for _ in range(8)]
    def mostrar(self):
        for i in range(8):
            fila1 = ' '.join(['.' if x is None else str(x.tipo[0]) for x in self.tablero[i]])
            fila2 = ' '.join(['.' if x is None else str(x.tipo[0]) for x in self.tablero2[i]])
            print(fila1 + '    ' + fila2)
    def agregar_ficha(self, ficha, posicion):
        fila, columna = posicion
        self.tablero[fila][columna] = ficha
        
    def mover_ficha(self, ficha, posicion):
        fila, columna = posicion
        if ficha in [item for sublist in self.tablero for item in sublist]:
            if self.tablero2[fila][columna] is None or self.tablero2[fila][columna].color != ficha.color:
                self.tablero[ficha.posicion[0]][ficha.posicion[1]] = None
                self.tablero2[fila][columna] = ficha
            else:
                print("Movimiento inválido: posición ocupada por un aliado")
        else:
            if self.tablero[fila][columna] is None or self.tablero[fila][columna].color != ficha.color:
                self.tablero2[ficha.posicion[0]][ficha.posicion[1]] = None
                self.tablero[fila][columna] = ficha
            else:
                print("Movimiento inválido: posición ocupada por un aliado")
        ficha.posicion = posicion
        print("Movimiento")
    
    
                
