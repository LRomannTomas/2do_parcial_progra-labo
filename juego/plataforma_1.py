import pygame
from constantes import *
from funciones import *


class Plataforma:
    def __init__(self,path,eje_x,eje_y,ancho,largo) -> None:
        
        self.imagen = pygame.image.load(path)
        self.imagen = pygame.transform.scale(self.imagen,(ancho,largo))
        self.rectangulo_imagen = self.imagen.get_rect()
        self.rectangulo_imagen.x = eje_x
        self.rectangulo_imagen.y = eje_y
        self.lados_plataforma = obtener_rectangulos(self.rectangulo_imagen)
        
    