import pygame
from pygame.locals import *
import piezas
import random
from concurrent.futures import ThreadPoolExecutor

# Inicializar Pygame
pygame.init()

# Icono de la ventana
icono = pygame.image.load(fr"src\img\cuadro\icon.png")

# Establecer el diseño del borde de la ventana

pygame.display.set_icon(icono)


piezas.inicializar_piezas()

# Configuración de la ventana
ANCHO = 1600
ALTO = 800


# Colores y posiciones
CLOSE_BUTTON_COLOR = (200, 0, 0) 
CLOSE_BUTTON_HOVER = (255, 0, 0)
CLOSE_BUTTON_POS = (750, 10, 40, 40)  # x, y, ancho, alto
FULLSCREEN_BUTTON_COLOR = (0, 200, 0)
FULLSCREEN_BUTTON_HOVER = (0, 255, 0)
BUTTON_WIDTH = 100
BUTTON_HEIGHT = 40

CLOSE_BUTTON_POS = (ANCHO - BUTTON_WIDTH - 10, 10, BUTTON_WIDTH, BUTTON_HEIGHT)
FULLSCREEN_BUTTON_POS = (ANCHO - BUTTON_WIDTH - 10, 60, BUTTON_WIDTH, BUTTON_HEIGHT)


VENTANA = pygame.display.set_mode((ANCHO, ALTO), pygame.NOFRAME)
pygame.display.set_caption("Ajedrez")

# Tamaño de las casillas
CASILLA = 50

# Colores para resaltar selección
COLOR_SELECCION = (255, 0, 0) # Rojo

# Cargar imágenes y escalarlas al tamaño de las casillas
img_blanca = pygame.image.load(fr"src\img\cuadro\blanco.png")
img_negra = pygame.image.load(fr"src\img\cuadro\negro.png")
img_blanca = pygame.transform.scale(img_blanca, (CASILLA, CASILLA))
img_negra = pygame.transform.scale(img_negra, (CASILLA, CASILLA))


# Cargar imágenes de las fichas y escalarlas al tamaño de las casillas

imgs = []
img_peon_negro = pygame.image.load(fr"src\img\negros\peon.png")
img_torre_negro = pygame.image.load(fr"src\img\negros\torre.png")
img_caballo_negro = pygame.image.load(fr"src\img\negros\caballo.png")
img_alfil_negro = pygame.image.load(fr"src\img\negros\alfil.png")
img_reina_negro = pygame.image.load(fr"src\img\negros\reina.png")
img_rey_negro = pygame.image.load(fr"src\img\negros\rey.png")

img_torre_negro = pygame.transform.scale(img_torre_negro, (CASILLA, CASILLA))
img_caballo_negro = pygame.transform.scale(img_caballo_negro, (CASILLA, CASILLA))
img_alfil_negro = pygame.transform.scale(img_alfil_negro, (CASILLA, CASILLA))
img_reina_negro = pygame.transform.scale(img_reina_negro, (CASILLA, CASILLA))
img_rey_negro = pygame.transform.scale(img_rey_negro, (CASILLA, CASILLA))
img_peon_negro = pygame.transform.scale(img_peon_negro, (CASILLA, CASILLA))

img_peon_blanco = pygame.image.load(fr"src\img\blancos\peon.png")
img_torre_blanco = pygame.image.load(fr"src\img\blancos\torre.png")
img_caballo_blanco = pygame.image.load(fr"src\img\blancos\caballo.png")
img_alfil_blanco = pygame.image.load(fr"src\img\blancos\alfil.png")
img_reina_blanco = pygame.image.load(fr"src\img\blancos\reina.png")
img_rey_blanco = pygame.image.load(fr"src\img\blancos\rey.png")
# Cargar imagen de inicio
imagen_inicio = pygame.image.load(fr'src\img\cuadro\inicio.png')
imagen_inicio = pygame.transform.scale(imagen_inicio, (ANCHO, ALTO))

img_torre_blanco = pygame.transform.scale(img_torre_blanco, (CASILLA, CASILLA))
img_caballo_blanco = pygame.transform.scale(img_caballo_blanco, (CASILLA, CASILLA))
img_alfil_blanco = pygame.transform.scale(img_alfil_blanco, (CASILLA, CASILLA))
img_reina_blanco = pygame.transform.scale(img_reina_blanco, (CASILLA, CASILLA))
img_rey_blanco = pygame.transform.scale(img_rey_blanco, (CASILLA, CASILLA))
img_peon_blanco = pygame.transform.scale(img_peon_blanco, (CASILLA, CASILLA))

# Cargar imagen de fondo y ajustarla al tamaño de la ventana
fondo = pygame.image.load(fr"src\img\cuadro\fondo.jpg")
fondo = pygame.transform.scale(fondo, (ANCHO, ALTO))


# Función para dibujar botones
def dibujar_boton(ventana, color, pos, texto):
    pygame.draw.rect(ventana, color, pos)
    fuente = pygame.font.Font(None, 36)
    texto_render = fuente.render(texto, True, (255, 255, 255))
    ventana.blit(texto_render, (pos[0] + 10, pos[1] + 5))

# Función para verificar si un botón ha sido clicado
def boton_clicado(pos, boton_pos):
    x, y, ancho, alto = boton_pos
    if x <= pos[0] <= x + ancho and y <= pos[1] <= y + alto:
        return True
    return False


# Animación de fin de juego
def animacion_fin_juego(ventana, img, duracion=3000):
    """
    Muestra una animación de fin de juego con la imagen proporcionada.
    """
    alpha = 0
    clock = pygame.time.Clock()
    start_time = pygame.time.get_ticks()
    
    while pygame.time.get_ticks() - start_time < duracion:
        ventana.fill((0, 0, 0))  # Limpiar la ventana
        img.set_alpha(alpha)
        ventana.blit(img, (0, 0))
        pygame.display.flip()
        
        alpha += 5  # Incrementar transparencia
        if alpha > 255:
            alpha = 255
        
        clock.tick(30)  # Controlar la velocidad de la animación

def dibujar_tablero(ventana, inicio_x, inicio_y):
    """
    Dibuja un tablero de ajedrez 8x8 en la posición especificada.
    """
    for fila in range(8):
        for columna in range(8):
            x = inicio_x + columna * CASILLA
            y = inicio_y + fila * CASILLA
            # Alternar entre casillas blancas y negras
            if (fila + columna) % 2 == 0:
                ventana.blit(img_blanca, (x, y))
            else:
                ventana.blit(img_negra, (x, y))



def detectar_seleccion(mouse_pos, inicio_x, inicio_y):
    """
    Detecta si el mouse está sobre una casilla del tablero y devuelve su posición.
    """
    col = (mouse_pos[0] - inicio_x) // CASILLA
    row = (mouse_pos[1] - inicio_y) // CASILLA
    if 0 <= col < 8 and 0 <= row < 8:
        return col, row
    return None

def detectar_seleccion_teclado(seleccion_actual, keys):
    """
    Detecta el movimiento de la selección actual usando las teclas de flecha.
    """
    if seleccion_actual:
        col, row = seleccion_actual
        if keys[pygame.K_LEFT]:
            col = max(0, col - 1)
        if keys[pygame.K_RIGHT]:
            col = min(7, col + 1)
            pygame.time.wait(100)  # Añadir un pequeño retraso
        if keys[pygame.K_UP]:
            row = max(0, row - 1)
            pygame.time.wait(100)  # Añadir un pequeño retraso
        if keys[pygame.K_DOWN]:
            row = min(7, row + 1)
            pygame.time.wait(100)  # Añadir un pequeño retraso
        if keys[pygame.K_RETURN]:
            return "selected"
        return col, row
    return None
def poner_ficha(ventana, row, col , inicio_x, inicio_y, img):
    """
    Dibuja una ficha en la posición especificada.
    """
    x = inicio_x + col * CASILLA
    y = inicio_y + row * CASILLA
    ventana.blit(img, (x, y))
    

# Calcular posiciones iniciales para centrar los tableros horizontalmente
MARGEN_SUPERIOR = 50  # Distancia desde la parte superior de la ventana
ESPACIO_ENTRE_TABLEROS = 140  # Espacio horizontal entre los dos tableros

# Cálculo dinámico de las posiciones
total_ancho_tableros = 2 * (8 * CASILLA) + ESPACIO_ENTRE_TABLEROS
inicio_x_tablero_izquierdo = (ANCHO - total_ancho_tableros) // 2
inicio_x_tablero_derecho = inicio_x_tablero_izquierdo + 8 * CASILLA + ESPACIO_ENTRE_TABLEROS

for ficha in piezas.fichas:
    if ficha.color == "Blanco":
        if ficha.tipo == "Peon":
            ficha.img = img_peon_blanco
        elif ficha.tipo == "Torre":
            ficha.img = img_torre_blanco
        elif ficha.tipo == "Caballo":
            ficha.img = img_caballo_blanco
        elif ficha.tipo == "Alfil":
            ficha.img = img_alfil_blanco
        elif ficha.tipo == "Dama":
            ficha.img = img_reina_blanco
        elif ficha.tipo == "Rey":
            ficha.img = img_rey_blanco
    elif ficha.color == "Negro":
        if ficha.tipo == "Peon":
            ficha.img = img_peon_negro
        elif ficha.tipo == "Torre":
            ficha.img = img_torre_negro
        elif ficha.tipo == "Caballo":
            ficha.img = img_caballo_negro
        elif ficha.tipo == "Alfil":
            ficha.img = img_alfil_negro
        elif ficha.tipo == "Dama":
            ficha.img = img_reina_negro
        elif ficha.tipo == "Rey":
            ficha.img = img_rey_negro
    else:
        ficha.img = None
def mostrar_casillas_disponibles(ficha):
    movimientos = ficha.movimientos_legales(piezas.board.tablero, piezas.board.tablero2)
    
    for movimiento in movimientos:
        if ficha.dimension == 1:
            x = inicio_x_tablero_izquierdo + movimiento[1] * CASILLA
            y = MARGEN_SUPERIOR + movimiento[0] * CASILLA
        else:
            x = inicio_x_tablero_derecho + movimiento[1] * CASILLA
            y = MARGEN_SUPERIOR + movimiento[0] * CASILLA
        pygame.draw.rect(VENTANA, (0, 255, 0), (x, y, CASILLA, CASILLA), 3)
        
    
    
def mostrar_cuadro_informacion(ventana):
    """
    Dibuja un cuadro en blanco fijo debajo de los tableros
    donde se mostrará información.
    """
    # Dimensiones y posición del cuadro
    ancho_cuadro = ANCHO - 40  # Margen de 20 píxeles a cada lado
    alto_cuadro = 200  # Altura fija para el cuadro
    posicion_x = 20  # Margen izquierdo
    posicion_y = MARGEN_SUPERIOR + 8 * CASILLA + 20  # Justo debajo de los tableros

    # Dibujar el cuadro en blanco
    pygame.draw.rect(ventana, (255, 255, 255), (posicion_x, posicion_y, ancho_cuadro, alto_cuadro))

    # Dibujar borde negro alrededor del cuadro
    pygame.draw.rect(ventana, (0, 0, 0), (posicion_x, posicion_y, ancho_cuadro, alto_cuadro), 2)

def mostrar_info_ficha(ventana, ficha):
    """
    Muestra la información de la ficha en el cuadro debajo de los tableros.
    """
    fuente = pygame.font.Font(None, 36)  # Fuente para el texto
    texto = f"Tipo: {ficha.tipo}, Color: {ficha.color}, Posición: {ficha.posicion}, Dimension: {ficha.dimension}"  # Texto a mostrar
    cuadro_texto = fuente.render(texto, True, (0, 0, 0))  # Texto negro
    ancho_texto = cuadro_texto.get_width()
    mostrar_casillas_disponibles(ficha)
    
    # Calcular posición centrada dentro del cuadro
    posicion_x = (ANCHO - ancho_texto) // 2
    posicion_y = MARGEN_SUPERIOR + 8 * CASILLA + 40  # Posición dentro del cuadro

    ventana.blit(cuadro_texto, (posicion_x, posicion_y))  # Dibujar texto en la ventana
def animacion_aparicion(ventana, duracion=5000):
        """
        Muestra una animación de aparición de la pantalla de inicio.
        """
        alpha = 0
        clock = pygame.time.Clock()
        start_time = pygame.time.get_ticks()
        
        while pygame.time.get_ticks() - start_time < duracion:
            ventana.fill((0, 0, 0))  # Limpiar la ventana
            imagen_inicio.set_alpha(alpha)
            ventana.blit(imagen_inicio, (0, 0))
            pygame.display.flip()
            
            alpha += 5  # Incrementar transparencia
            if alpha > 255:
                alpha = 255
            
            clock.tick(30)  # Controlar la velocidad de la animación

    # Mostrar animación de aparición al inicio del juego
# Función para mostrar la pantalla de inicio
def mostrar_pantalla_inicio(ventana):
    ventana.blit(imagen_inicio, (0, 0))
    pygame.display.update()
    # Función para mostrar una animación de aparición
    animacion_aparicion(ventana)
    
# Función para verificar si el botón invisible ha sido clicado
def boton_invisible_clicado(pos):
    boton_x = ANCHO // 2 - 200
    boton_y = ALTO // 2 - 100
    boton_ancho = 400
    boton_alto = 200
    if boton_x <= pos[0] <= boton_x + boton_ancho and boton_y <= pos[1] <= boton_y + boton_alto:
        return True
    return False

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
    [0.3, -0.4, -0.4, -0.5, -0.5, -0.4, -0.4, -0.3],
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
    # Reproducir sonido de movimiento
    resultado = piezas.mover(ficha, nueva_posicion)
    if isinstance(resultado, tuple):
        mov, mensaje = resultado
    else:
        mov = resultado
        mensaje = ""
    if mov:
        if ficha.tipo == "Caballo":
            sonido_movimiento = pygame.mixer.Sound(fr"src\audio\caballo.mp3")
        else:
            sonido_movimiento = pygame.mixer.Sound(fr"src\audio\movimiento.mp3")
            
                
        sonido_movimiento.play()
        # Mostrar mensaje de movimiento
        fuente = pygame.font.Font(None, 72)
        texto_movimiento = fuente.render(f"Moviendo {ficha.tipo} a {nueva_posicion}", True, (255, 255, 255))
        ventana_movimiento = pygame.Surface((texto_movimiento.get_width() + 20, texto_movimiento.get_height() + 20))
        ventana_movimiento.fill((0, 0, 0))
        ventana_movimiento.blit(texto_movimiento, (10, 10))
        VENTANA.blit(ventana_movimiento, ((ANCHO - ventana_movimiento.get_width()) // 2, (ALTO - ventana_movimiento.get_height()) // 2))
        pygame.display.flip()
        pygame.time.wait(2000)  # Esperar 2 segundos
    
    return mov
def determinar_profundidad():
    total_fichas = len(fichas_blancas) + len(fichas_negras)
    if total_fichas > 20:
        return 2  # Menor profundidad para posiciones complejas
    elif total_fichas > 10:
        return 3
    else:
        return 4  # Mayor profundidad para el final del juego
def evaluar_movimiento(tablero, ficha, mov, profundidad, alfa, beta, maximizando):
    """
    Función auxiliar para evaluar un movimiento individual de forma paralela.
    """
    tablero_copia = tablero.copia_tablero()
    pieza_enemigo = tablero.tablero[mov[0]][mov[1]] if ficha.dimension == 1 else tablero.tablero2[mov[0]][mov[1]]

    piezas.mover(ficha, mov, simular=True)
    eval = minimax(tablero_copia, profundidad - 1, alfa, beta, not maximizando)

    if pieza_enemigo:  # Si hay una pieza enemiga en la posición de destino
        eval += pieza_enemigo.valor

    return eval
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

                # Calcular movilidad
                movilidad = len(pieza.movimientos_legales(piezas.board.tablero, piezas.board.tablero2))

                # Valorar capturas (priorizar capturar piezas enemigas)
                capturas = sum(
                    enemigo.valor for mov in pieza.movimientos_legales(piezas.board.tablero, piezas.board.tablero2)
                    if (enemigo := piezas.board.obtener_pieza_en(mov)) and enemigo.color != pieza.color
                )

                # Ajustar el valor dependiendo del color
                if pieza.color == "Blanco":
                    valor -= base_valor + control_centro + movilidad + capturas
                else:
                    valor += base_valor + control_centro + movilidad + capturas

    return valor

def minimax(tablero, profundidad, alfa, beta, maximizando):
    if profundidad == 0:
        return evaluar_tablero() + random.uniform(-0.5, 0.5)

    if maximizando:
        max_eval = -float('inf')
        with ThreadPoolExecutor() as executor:
            futures = []
            for ficha in fichas_blancas:
                movimientos = ficha.movimientos_legales(tablero.tablero, tablero.tablero2)
                movimientos = filtrar_movimientos_prometedores(ficha, movimientos)
                for mov in movimientos:
                    futures.append(executor.submit(evaluar_movimiento, tablero, ficha, mov, profundidad, alfa, beta, maximizando))

            for future in futures:
                eval = future.result()
                max_eval = max(max_eval, eval)
                alfa = max(alfa, eval)
                if beta <= alfa:
                    break
        return max_eval
    else:
        min_eval = float('inf')
        with ThreadPoolExecutor() as executor:
            futures = []
            for ficha in fichas_negras:
                movimientos = ficha.movimientos_legales(tablero.tablero, tablero.tablero2)
                movimientos = filtrar_movimientos_prometedores(ficha, movimientos)
                for mov in movimientos:
                    futures.append(executor.submit(evaluar_movimiento, tablero, ficha, mov, profundidad, alfa, beta, maximizando))

            for future in futures:
                eval = future.result()
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
            pieza_enemiga = piezas.board.tablero[mov[0]][mov[1]] if ficha.dimension == 1 else piezas.board.tablero2[mov[0]][mov[1]]
            piezas.mover(ficha, mov, simular=True)
            profundidad = determinar_profundidad()
            valor = minimax(tablero_copia, profundidad, -float('inf'), float('inf'), True)
            if pieza_enemiga:  # Si hay una pieza enemiga en la posición de destino
                valor -= pieza_enemiga.valor 
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





# Variables para mantener la selección actual y la ficha seleccionada
seleccion_izquierda = None
seleccion_derecha = None
ficha_seleccionada = None  # Nueva variable para rastrear la ficha seleccionada

sonido_jaque = pygame.mixer.Sound(fr"src\audio\jaque.mp3")
# Bucle principal
ejecutando = True
pantalla_inicio = True
pantalla_completa = False
turno_blanco = True
turno_actual = 0
while not piezas.finalizar_juego() and ejecutando:
    # Si el rey esta en jaque, reproducir sonido
    if piezas.rey_en_jaque("Blanco") and turno_blanco:
        sonido_jaque.play()
    elif piezas.rey_en_jaque("Negro") and not turno_blanco:
        sonido_jaque.play()
    
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if pantalla_inicio:
                if boton_invisible_clicado(evento.pos):
                    pantalla_inicio = False  # Iniciar el juego
            else:
                if boton_clicado(evento.pos, CLOSE_BUTTON_POS):
                    ejecutando = False
                elif boton_clicado(evento.pos, FULLSCREEN_BUTTON_POS):
                    pantalla_completa = not pantalla_completa
                    if pantalla_completa:
                        VENTANA = pygame.display.set_mode((ANCHO, ALTO), pygame.FULLSCREEN)
                    else:
                        VENTANA = pygame.display.set_mode((ANCHO, ALTO))
    if pantalla_inicio:
        mostrar_pantalla_inicio(VENTANA)
    else:
        # Dibujar fondo
        VENTANA.blit(fondo, (0, 0))  # Dibuja la imagen de fondo

        # Dibujar los dos tableros
        dibujar_tablero(VENTANA, inicio_x_tablero_izquierdo, MARGEN_SUPERIOR)  # Tablero izquierdo
        dibujar_tablero(VENTANA, inicio_x_tablero_derecho, MARGEN_SUPERIOR)  # Tablero derecho

        # Dibujar fichas en el tablero izquierdo
        for fichas in piezas.board.tablero:
            if fichas:
                for ficha in fichas:
                    if ficha:
                        poner_ficha(VENTANA, ficha.posicion[0], ficha.posicion[1], inicio_x_tablero_izquierdo, MARGEN_SUPERIOR, ficha.img)

        # Dibujar fichas en el tablero derecho
        for fichas in piezas.board.tablero2:
            if fichas:
                for ficha in fichas:
                    if ficha:
                        poner_ficha(VENTANA, ficha.posicion[0], ficha.posicion[1], inicio_x_tablero_derecho, MARGEN_SUPERIOR, ficha.img)

        if turno_blanco:
            # Detectar selección
            mouse_pos = pygame.mouse.get_pos()
            mouse_click = pygame.mouse.get_pressed()
            keys = pygame.key.get_pressed()
            if mouse_click[0] or any(keys):  # Si se hace clic con el botón izquierdo o se presiona una tecla
                # Que tenga un delay para que no se mueva tan rápido
                pygame.time.wait(100)

            if mouse_click[0] or any(keys):  # Si se hace clic con el botón izquierdo o se presiona una tecla
                # Verificar selección en el tablero izquierdo
                seleccion = detectar_seleccion(mouse_pos, inicio_x_tablero_izquierdo, MARGEN_SUPERIOR)
                if seleccion:
                    if ficha_seleccionada and ficha_seleccionada.dimension == 1:
                        try:
                            mover_ficha(ficha_seleccionada, (seleccion[1], seleccion[0]))
                        except TypeError:
                            pass
                        ficha_seleccionada = None
                        seleccion_izquierda = None  # Restablecer selección izquierda
                        turno_blanco = False  # Cambiar turno a negro
                    else:
                        seleccion_izquierda = seleccion  # Guardar la selección
                        ficha_seleccionada = None  # Resetear ficha seleccionada
                        for fichas in piezas.board.tablero:
                            if fichas:
                                if fichas:
                                    for ficha in fichas:
                                        if ficha:
                                            if ficha.dimension == 1 and ficha.posicion == (seleccion[1], seleccion[0]) and ficha.color == "Blanco":
                                                ficha_seleccionada = ficha

                # Verificar selección en el tablero derecho
                seleccion = detectar_seleccion(mouse_pos, inicio_x_tablero_derecho, MARGEN_SUPERIOR)
                if seleccion:
                    if ficha_seleccionada and ficha_seleccionada.dimension == 2:
                        try:
                            mover_ficha(ficha_seleccionada, (seleccion[1], seleccion[0]))
                        except TypeError:
                            pass
                        ficha_seleccionada = None
                        seleccion_derecha = None  # Restablecer selección derecha
                        turno_blanco = False  # Cambiar turno a negro
                    else:
                        seleccion_derecha = seleccion  # Guardar la selección
                        ficha_seleccionada = None  # Resetear ficha seleccionada
                        for fichas in piezas.board.tablero2:
                            if fichas:
                                for ficha in fichas:
                                    if ficha:
                                        if ficha.dimension == 2 and ficha.posicion == (seleccion[1], seleccion[0]) and ficha.color == "Blanco":
                                            ficha_seleccionada = ficha
                                            break
            # Detectar movimiento de selección con teclado
            seleccion_izquierda = detectar_seleccion_teclado(seleccion_izquierda, keys)
            seleccion_derecha = detectar_seleccion_teclado(seleccion_derecha, keys)
            # Dibujar siempre las selecciones actuales si existen
            if seleccion_izquierda:
                col, row = seleccion_izquierda
                pygame.draw.rect(
                    VENTANA, COLOR_SELECCION,
                    (inicio_x_tablero_izquierdo + col * CASILLA, MARGEN_SUPERIOR + row * CASILLA, CASILLA, CASILLA),
                    3
                )

            if seleccion_derecha:
                col, row = seleccion_derecha
                pygame.draw.rect(
                    VENTANA, COLOR_SELECCION,
                    (inicio_x_tablero_derecho + col * CASILLA, MARGEN_SUPERIOR + row * CASILLA, CASILLA, CASILLA),
                    3
                )

            # Mostrar cuadro fijo para la información
            mostrar_cuadro_informacion(VENTANA)

            # Mostrar información de la ficha seleccionada (si existe)
            if ficha_seleccionada:
                mostrar_info_ficha(VENTANA, ficha_seleccionada)

        else:
            if not turno_blanco and turno_actual >= TURNOS_SEMIALEATORIOS:
                # Mostrar mensaje de "Minimax pensando"
                fuente = pygame.font.Font(None, 36)
                texto_pensando = fuente.render("Minimax pensando...", True, (255, 255, 255))
                ventana_pensando = pygame.Surface((texto_pensando.get_width() + 20, texto_pensando.get_height() + 20))
                ventana_pensando.fill((0, 0, 0))
                ventana_pensando.blit(texto_pensando, (10, 10))
                VENTANA.blit(ventana_pensando, ((ANCHO - ventana_pensando.get_width()) // 2, (ALTO - ventana_pensando.get_height()) // 2))
                pygame.display.flip()

            # Movimiento de las piezas negras por la IA
            while True:
                if turno_actual < TURNOS_SEMIALEATORIOS:
                    movimiento = movimiento_semi_aleatorio()
                else:
                    movimiento = mejor_movimiento()
                if movimiento:
                    ficha, nueva_posicion = movimiento
                    if mover_ficha(ficha, nueva_posicion):
                        turno_blanco = True  # Cambiar turno a blanco
                        turno_actual += 1
                        break
                    

                

        # Dibujar botones
        dibujar_boton(VENTANA, CLOSE_BUTTON_COLOR, CLOSE_BUTTON_POS, "Salir")
        dibujar_boton(VENTANA, FULLSCREEN_BUTTON_COLOR, FULLSCREEN_BUTTON_POS, "Pantalla Completa")

        # Actualizar la pantalla
        pygame.display.flip()

else:
    pygame.mixer.music.load(fr"src\audio\background_music.mp3")
    pygame.mixer.music.play(-1)  # Reproducir en bucle

    # Mostrar animación de fin de juego
    img_fin_juego = pygame.image.load(fr"src\img\cuadro\fin_juego.png")
    img_fin_juego = pygame.transform.scale(img_fin_juego, (ANCHO, ALTO))
    animacion_fin_juego(VENTANA, img_fin_juego, duracion=5000)


pygame.quit()

