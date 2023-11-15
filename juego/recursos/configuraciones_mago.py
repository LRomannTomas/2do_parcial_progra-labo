import pygame
from funciones import girar_imagen


mago_quieto_derecha = [
    pygame.transform.scale(pygame.image.load("juego/recursos\mago\quieto/0.png"),(60,60)),
    pygame.transform.scale(pygame.image.load("juego/recursos\mago\quieto/1.png"),(60,60)),
    pygame.transform.scale(pygame.image.load("juego/recursos\mago\quieto/2.png"),(60,60)),
    pygame.transform.scale(pygame.image.load("juego/recursos\mago\quieto/3.png"),(60,60)),

]

mago_camina = [
    pygame.transform.scale(pygame.image.load("juego/recursos\mago\camina/0.png"),(60,60)),
    pygame.transform.scale(pygame.image.load("juego/recursos\mago\camina/1.png"),(60,60)),
    pygame.transform.scale(pygame.image.load("juego/recursos\mago\camina/2.png"),(60,60)),
    pygame.transform.scale(pygame.image.load("juego/recursos\mago\camina/3.png"),(60,60)),
    pygame.transform.scale(pygame.image.load("juego/recursos\mago\camina/4.png"),(60,60)),
    pygame.transform.scale(pygame.image.load("juego/recursos\mago\camina/5.png"),(60,60)),
    
]

camina_izquierda = girar_imagen(mago_camina,True,False)
quieto_izquierda = girar_imagen(mago_quieto_derecha,True,False)



