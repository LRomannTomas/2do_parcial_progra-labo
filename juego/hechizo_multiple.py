import pygame
from disparo import Disparo
from funciones import girar_imagen


class HechizoMultiple(Disparo):
    def __init__(self, lista_plataformas, x, y,distancia,velocidad_disparo):
        
        lista_disparo_derecha = [
            
            pygame.transform.scale(pygame.image.load("juego/recursos\primer_boss\poder_hechizo\pulse1.png"),(70,50)),
            pygame.transform.scale(pygame.image.load("juego/recursos\primer_boss\poder_hechizo\pulse2.png"),(70,50)),
            pygame.transform.scale(pygame.image.load("juego/recursos\primer_boss\poder_hechizo\pulse3.png"),(70,50)),
            pygame.transform.scale(pygame.image.load("juego/recursos\primer_boss\poder_hechizo\pulse4.png"),(70,50)),
            
        ]
        lista_disparo_izquierda = girar_imagen(lista_disparo_derecha,True,False)
      
        
        super().__init__(lista_plataformas, x, y,lista_disparo_derecha,lista_disparo_izquierda,velocidad_disparo,distancia)