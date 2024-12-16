import pygame
from pygame.locals import *
import piezas

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
COLOR_SELECCION = (255, 0, 0)

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
def poner_ficha(ventana, row, col , inicio_x, inicio_y, img):
    """
    Dibuja una ficha en la posición especificada.
    """
    x = inicio_x + col * CASILLA
    y = inicio_y + row * CASILLA
    ventana.blit(img, (x, y))
    

# Calcular posiciones iniciales para centrar los tableros horizontalmente
MARGEN_SUPERIOR = 50  # Distancia desde la parte superior de la ventana
ESPACIO_ENTRE_TABLEROS = 100  # Espacio horizontal entre los dos tableros

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
        
def mover_ficha(ficha, nueva_posicion):
    """
    Mueve una ficha a una nueva posición y actualiza la interfaz.
    """

    piezas.mover(ficha, nueva_posicion)
    
    
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

# Variables para mantener la selección actual y la ficha seleccionada
seleccion_izquierda = None
seleccion_derecha = None
ficha_seleccionada = None  # Nueva variable para rastrear la ficha seleccionada

# Bucle principal
ejecutando = True
pantalla_inicio = True
pantalla_completa = False

while not piezas.finalizar_juego() and ejecutando:
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
        # *Dibujar fichas en el tablero izquierdo
        for fichas in piezas.board.tablero:
            if fichas:
                for ficha in fichas:
                    if ficha:
                        poner_ficha(VENTANA, ficha.posicion[0], ficha.posicion[1], inicio_x_tablero_izquierdo, MARGEN_SUPERIOR, ficha.img)
            
        # *Dibujar fichas en el tablero derecho
        for fichas in piezas.board.tablero2:
            if fichas:
                for ficha in fichas:
                    if ficha:
                        poner_ficha(VENTANA, ficha.posicion[0], ficha.posicion[1], inicio_x_tablero_derecho, MARGEN_SUPERIOR, ficha.img)
                
        
        # *Detectar selección
        mouse_pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()
        keys = pygame.key.get_pressed()

        if mouse_click[0] or any(keys):  # Si se hace clic con el botón izquierdo o se presiona una tecla
            # Verificar selección en el tablero izquierdo
            seleccion = detectar_seleccion(mouse_pos, inicio_x_tablero_izquierdo, MARGEN_SUPERIOR)
            if seleccion:
                if ficha_seleccionada and ficha_seleccionada.dimension == 1:
                    mover_ficha(ficha_seleccionada, (seleccion[1], seleccion[0]))
                    ficha_seleccionada = None
                    seleccion_izquierda = None  # Restablecer selección izquierda
                else:
                    seleccion_izquierda = seleccion  # Guardar la selección
                    ficha_seleccionada = None  # Resetear ficha seleccionada
                    for fichas in piezas.board.tablero:
                        if fichas:
                            if fichas:
                                for ficha in fichas:
                                    if ficha:
                                        if ficha.dimension == 1 and ficha.posicion == (seleccion[1], seleccion[0]):
                                            ficha_seleccionada = ficha        

            # Verificar selección en el tablero derecho
            seleccion = detectar_seleccion(mouse_pos, inicio_x_tablero_derecho, MARGEN_SUPERIOR)
            if seleccion:
                if ficha_seleccionada and ficha_seleccionada.dimension == 2:
                    mover_ficha(ficha_seleccionada, (seleccion[1], seleccion[0]))
                    ficha_seleccionada = None
                    seleccion_derecha = None  # Restablecer selección derecha
                else:
                    seleccion_derecha = seleccion  # Guardar la selección
                    ficha_seleccionada = None  # Resetear ficha seleccionada
                    for fichas in piezas.board.tablero2:
                        if fichas:
                            for ficha in fichas:
                                if ficha:
                                    if ficha.dimension == 2 and ficha.posicion == (seleccion[1], seleccion[0]):
                                        ficha_seleccionada = ficha
                                        break   
                            

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

