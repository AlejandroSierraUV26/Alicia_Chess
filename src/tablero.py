import colorama
class Tablero:
    def __init__(self):
        # Matriz 8x8 que representa el tablero
        self.tablero = [[None for _ in range(8)] for _ in range(8)]
        self.tablero2 = [[None for _ in range(8)] for _ in range(8)]
    def mostrar(self):
        """
        Muestra los tableros con bordes decorativos y etiquetas de filas y columnas.
        """
        letras = "01234567"  # Etiquetas de columnas
        
        # Borde superior para ambos tableros
        borde = "  +" + "-" * 17 + "+"  # Cada tablero mide 8 columnas (7 espacios + 8 caracteres)
        print("    " + " ".join(letras) + "          " + " ".join(letras))
        print(borde + "    " + borde)

        for i in range(8):  # Recorrer filas
            # Crear las filas de ambos tableros
            fila1 = ' '.join([
                self._colorear_pieza(x) if x else '.'
                for x in self.tablero[i]
            ])
            fila2 = ' '.join([
                self._colorear_pieza(x) if x else '.'
                for x in self.tablero2[i]
            ])
            # Mostrar las filas con etiquetas de filas
            print(f"{i} | {fila1} |    {i} | {fila2} |")

        # Borde inferior para ambos tableros
        print(borde + "    " + borde)

    @staticmethod
    def _colorear_pieza(pieza):
        """
        Devuelve el símbolo de la pieza coloreado según su color.
        """
        # Códigos de color ANSI
        if pieza.color == "Blanco":
            return f"\033[97m{pieza.tipo[0]}\033[0m"  # Blanco
        elif pieza.color == "Negro":
            return f"\033[91m{pieza.tipo[0]}\033[0m"  # Gris oscuro
        else:
            return pieza.tipo[0]  # Sin color si no coincide
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
    def eliminar_ficha(self, ficha, posicion):
        fila, columna = posicion
        if ficha in [item for sublist in self.tablero for item in sublist]:
            self.tablero[fila][columna] = None
        else:
            self.tablero2[fila][columna] = None
    def fichas_oponentes(self, color):
        return [item for sublist in self.tablero for item in sublist if item and item.color != color]
                
