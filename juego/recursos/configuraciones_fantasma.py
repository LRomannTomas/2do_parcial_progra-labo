import pygame
from funciones import girar_imagen

lista_camina_derecha = [
    pygame.transform.scale(pygame.image.load("juego/recursos/fantasma\camina_1.png"),(60,60)),    
    pygame.transform.scale(pygame.image.load("juego/recursos/fantasma\camina_2.png"),(60,60)),    
    pygame.transform.scale(pygame.image.load("juego/recursos/fantasma\camina_3.png"),(60,60)),    
    pygame.transform.scale(pygame.image.load("juego/recursos/fantasma\camina_4.png"),(60,60)),    
    pygame.transform.scale(pygame.image.load("juego/recursos/fantasma\camina_5.png"),(60,60)),    
    pygame.transform.scale(pygame.image.load("juego/recursos/fantasma\camina_6.png"),(60,60)),    
    pygame.transform.scale(pygame.image.load("juego/recursos/fantasma\camina_7.png"),(60,60)),    
    pygame.transform.scale(pygame.image.load("juego/recursos/fantasma\camina_8.png"),(60,60))    
]

camina_derecha_invisible = [
    pygame.transform.scale(pygame.image.load("juego/recursos/fantasma\invisible_1.png"),(60,60)),    
    pygame.transform.scale(pygame.image.load("juego/recursos/fantasma\invisible_2.png"),(60,60)),    
    pygame.transform.scale(pygame.image.load("juego/recursos/fantasma\invisible_3.png"),(60,60)),    
    pygame.transform.scale(pygame.image.load("juego/recursos/fantasma\invisible_4.png"),(60,60)),    
    pygame.transform.scale(pygame.image.load("juego/recursos/fantasma\invisible_5.png"),(60,60)),    
    pygame.transform.scale(pygame.image.load("juego/recursos/fantasma\invisible_6.png"),(60,60)),    
    pygame.transform.scale(pygame.image.load("juego/recursos/fantasma\invisible_7.png"),(60,60)),    
    pygame.transform.scale(pygame.image.load("juego/recursos/fantasma\invisible_8.png"),(60,60))    
]


lista_camina_izquierda = girar_imagen(lista_camina_derecha,True,False)


camina_izquierda_invisible = girar_imagen(camina_derecha_invisible,True,False)