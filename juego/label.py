import pygame
from widgets import Widget
from constantes import *


class Label(Widget):
    def __init__(self, x, y, ancho, largo,texto, path_imagen):
        
        super().__init__(x, y, ancho, largo, path_imagen)
        
        
        self.fuente = pygame.font.SysFont("8bitoperator8",50)
        self.texto = texto
        
    
    @property
    def texto(self):
        return self.__texto

    @texto.setter
    def texto(self,texto):
        self.__texto = texto
        self.texto_renderizado = self.fuente.render(texto,True,COLOR_BLANCO)
        self.texto_rect = self.texto_renderizado.get_rect()
        self.texto_rect.center = self.rectangulo.center
    
    def update(self, pantalla, lista_eventos):
        super().update(pantalla, lista_eventos)
        pantalla.blit(self.texto_renderizado,self.texto_rect)
        