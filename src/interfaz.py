import pygame
from pygame.locals import *
import piezas

# Inicializar Pygame
pygame.init()
piezas.inicializar_piezas()

# Configuración de la ventana
ANCHO = 1600
ALTO = 800
VENTANA = pygame.display.set_mode((ANCHO, ALTO))
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

img_torre_blanco = pygame.transform.scale(img_torre_blanco, (CASILLA, CASILLA))
img_caballo_blanco = pygame.transform.scale(img_caballo_blanco, (CASILLA, CASILLA))
img_alfil_blanco = pygame.transform.scale(img_alfil_blanco, (CASILLA, CASILLA))
img_reina_blanco = pygame.transform.scale(img_reina_blanco, (CASILLA, CASILLA))
img_rey_blanco = pygame.transform.scale(img_rey_blanco, (CASILLA, CASILLA))
img_peon_blanco = pygame.transform.scale(img_peon_blanco, (CASILLA, CASILLA))

# Cargar imagen de fondo y ajustarla al tamaño de la ventana
fondo = pygame.image.load(fr"src\img\cuadro\fondo.jpg")
fondo = pygame.transform.scale(fondo, (ANCHO, ALTO))


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
    texto = f"Tipo: {ficha.tipo}, Color: {ficha.color}, Posición: {ficha.posicion}"  # Texto a mostrar
    cuadro_texto = fuente.render(texto, True, (0, 0, 0))  # Texto negro
    ancho_texto = cuadro_texto.get_width()
    
    # Calcular posición centrada dentro del cuadro
    posicion_x = (ANCHO - ancho_texto) // 2
    posicion_y = MARGEN_SUPERIOR + 8 * CASILLA + 40  # Posición dentro del cuadro

    ventana.blit(cuadro_texto, (posicion_x, posicion_y))  # Dibujar texto en la ventana


# Variables para mantener la selección actual y la ficha seleccionada
seleccion_izquierda = None
seleccion_derecha = None
ficha_seleccionada = None  # Nueva variable para rastrear la ficha seleccionada

# Bucle principal del juego
corriendo = True
while corriendo:
    for evento in pygame.event.get():
        if evento.type == QUIT:
            corriendo = False

    # Dibujar fondo
    VENTANA.blit(fondo, (0, 0))  # Dibuja la imagen de fondo

    # Dibujar los dos tableros
    dibujar_tablero(VENTANA, inicio_x_tablero_izquierdo, MARGEN_SUPERIOR)  # Tablero izquierdo
    dibujar_tablero(VENTANA, inicio_x_tablero_derecho, MARGEN_SUPERIOR)  # Tablero derecho

    # Detectar selección
    mouse_pos = pygame.mouse.get_pos()
    mouse_click = pygame.mouse.get_pressed()
    keys = pygame.key.get_pressed()

    if mouse_click[0] or any(keys):  # Si se hace clic con el botón izquierdo o se presiona una tecla
        # Verificar selección en el tablero izquierdo
        seleccion = detectar_seleccion(mouse_pos, inicio_x_tablero_izquierdo, MARGEN_SUPERIOR)
        if seleccion:
            seleccion_izquierda = seleccion  # Guardar la selección
            ficha_seleccionada = None  # Resetear ficha seleccionada
            for ficha in piezas.fichas:
                if ficha.dimension == 1 and ficha.posicion == (seleccion[1], seleccion[0]):
                    ficha_seleccionada = ficha  # Guardar la ficha seleccionada

        # Verificar selección en el tablero derecho
        seleccion = detectar_seleccion(mouse_pos, inicio_x_tablero_derecho, MARGEN_SUPERIOR)
        if seleccion:
            seleccion_derecha = seleccion  # Guardar la selección
            ficha_seleccionada = None  # Resetear ficha seleccionada
            for ficha in piezas.fichas:
                if ficha.dimension == 2 and ficha.posicion == (seleccion[1], seleccion[0]):
                    ficha_seleccionada = ficha  # Guardar la ficha seleccionada

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

    # Dibujar fichas en el tablero izquierdo
    for ficha in piezas.fichas:
        if ficha.dimension == 1:
            poner_ficha(VENTANA, ficha.posicion[0], ficha.posicion[1], inicio_x_tablero_izquierdo, MARGEN_SUPERIOR, ficha.img)

    # Dibujar fichas en el tablero derecho
    for ficha in piezas.fichas:
        if ficha.dimension == 2:
            poner_ficha(VENTANA, ficha.posicion[0], ficha.posicion[1], inicio_x_tablero_derecho, MARGEN_SUPERIOR, ficha.img)

    # Mostrar cuadro fijo para la información
    mostrar_cuadro_informacion(VENTANA)

    # Mostrar información de la ficha seleccionada (si existe)
    if ficha_seleccionada:
        mostrar_info_ficha(VENTANA, ficha_seleccionada)

    # Actualizar la pantalla
    pygame.display.flip()

pygame.quit()
