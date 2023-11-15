import pygame
from constantes import *
from widgets import Widget

class Boton(Widget):
    def __init__(self,x,y,ancho,alto,path_imagen,on_click,parametro_1=None,remarco=None):
        
        super().__init__(x,y,ancho,alto,path_imagen)
       
        self.remarco = remarco
        self.on_click = on_click
        self.parametro_1 = parametro_1

        
    def update(self,pantalla,lista_eventos):
        
        if self.remarco != None:
            pantalla.blit(self.remarco,(self.rectangulo.x - 30 ,self.rectangulo.y - 30))
            
        pantalla.blit(self.imagen,(self.rectangulo.x,self.rectangulo.y))
        

        for evento in lista_eventos:
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if self.rectangulo.collidepoint(evento.pos):
                    if self.parametro_1 != None:
                        self.on_click(self.parametro_1)
                    else:
                        self.on_click()