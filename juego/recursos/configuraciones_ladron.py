import pygame
from funciones import girar_imagen


ladron_camina_derecha = [
    pygame.transform.scale(pygame.image.load("juego/recursos\ladron/0.png"),(60,60)),
    pygame.transform.scale(pygame.image.load("juego/recursos\ladron/1.png"),(60,60)),
    pygame.transform.scale(pygame.image.load("juego/recursos\ladron/2.png"),(60,60)),
    pygame.transform.scale(pygame.image.load("juego/recursos\ladron/3.png"),(60,60)),
    pygame.transform.scale(pygame.image.load("juego/recursos\ladron/4.png"),(60,60)),
    pygame.transform.scale(pygame.image.load("juego/recursos\ladron/5.png"),(60,60))
]

ladron_camina_izquierda = girar_imagen(ladron_camina_derecha,True,False)
