import pygame
from constantes import *
from modo import *

from menu_principal import MenuPrincipal



pygame.init()
#ocultar_mouse = pygame.mouse.set_visible(False)   --> OCULTAR EL CURSOR
pantalla = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
reloj = pygame.time.Clock()

menu_principal = MenuPrincipal(pantalla)


flag_correr = True


while flag_correr:
    
    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            flag_correr = False
        
        
    menu_principal.update(lista_eventos)


    reloj.tick(FPS)
    
    pygame.display.flip()

    
pygame.quit()   