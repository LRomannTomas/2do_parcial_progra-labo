import pygame 
from disparo import Disparo



class HechizoFuego(Disparo):
    def __init__(self,lista_plataformas,x,y,distancia,velocidad_disparo):
        
        lista_disparo_derecha = [
            pygame.transform.scale(pygame.image.load("juego/recursos/fuego/0.png"),(20,20)),
            pygame.transform.scale(pygame.image.load("juego/recursos/fuego/1.png"),(20,20)),
            pygame.transform.scale(pygame.image.load("juego/recursos/fuego/2.png"),(20,20)),
            pygame.transform.scale(pygame.image.load("juego/recursos/fuego/3.png"),(20,20))
        ]
        
        lista_disparo_izquierda = lista_disparo_derecha
        
        super().__init__(lista_plataformas,x,y,lista_disparo_derecha,lista_disparo_izquierda,velocidad_disparo,distancia) 