import pygame
from llave import Llave


class LlaveRecolectable:
    def __init__(self,x,y) -> None:
        self.nombre = "llave"
        self.ancho_imagen = 25
        self.alto_imagen = 25
        self.imagen = pygame.transform.scale(pygame.image.load("juego/recursos\iconos\key.png"),(self.ancho_imagen,self.alto_imagen)) 
        
        self.rectangulo = self.imagen.get_rect()
        self.rectangulo.x = x
        self.rectangulo.y = y
        
        self.precio = 0
        
        self.mostrar = True
        
        
    def update(self,personaje,pantalla):
        if self.mostrar:
            pantalla.blit(self.imagen,self.rectangulo)
        
        if personaje.rectangulo_personaje.colliderect(self.rectangulo):
            self.mostrar = False
            personaje.lista_items.append(Llave())
            
        
        