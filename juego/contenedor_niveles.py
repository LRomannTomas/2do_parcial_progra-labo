import pygame
from menu import Menu
from constantes import *
from menu_tienda import *


class ContenedorNiveles(Menu):
    def __init__(self,pantalla,nivel):
        self.ancho_boton = 100
        self.alto_boton = 60
        self.remarco = pygame.transform.scale(pygame.image.load("juego/recursos/botones/remarco_boton.png"),(self.ancho_boton + 60,self.alto_boton + 60))
        
        lista_widgets = []
        self.nivel = nivel
        
        super().__init__(lista_widgets,pantalla)
        
   
        
    def update(self,lista_eventos):
        
        #recibe la flag y le comunica al selector de niveles
        self.nivel.update(lista_eventos)
        if self.nivel.supero_nivel:
            self.set_dialogo("supero nivel")
            
        
        
        if self.nivel.abrir_tienda == True:
            self.nivel.abrir_tienda = False
            menu_tienda = MenuTienda(self.pantalla,self.nivel.jugador)
            self.set_hijo(menu_tienda)
        
        if self.nivel.abrir_menu:
            dialogo = "volver"
            self.set_dialogo(dialogo)
            
    
            
        super().update(lista_eventos)
        