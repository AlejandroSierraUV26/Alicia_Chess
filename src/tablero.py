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
        
                
