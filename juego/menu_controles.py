import pygame
from menu import Menu
from widgets import Widget
from boton import Boton
from constantes import *


class MenuControles(Menu):
    def __init__(self, pantalla) -> None:
        ancho_boton = 180
        alto_boton = 100
        
        remarco = pygame.transform.scale(pygame.image.load("juego/recursos/botones/remarco_salir.png"),(ancho_boton + 60,alto_boton + 60))
        
        flecha_arriba = Widget(300,200,100,100,"juego/recursos\iconos/flecha_arriba.png")
        flecha_abajo = Widget(300,300,100,100,"juego/recursos\iconos/flecha_abajo.png")
        flecha_derecha = Widget(300,400,100,100,"juego/recursos\iconos/flecha_derecha.png")
        flecha_izquierda = Widget(300,500,100,100,"juego/recursos\iconos/flecha_izquierda.png")
        
        
        boton_3 = Boton(1150,650,ancho_boton,alto_boton,"juego/recursos/botones/boton_salir.png",self.set_dialogo,"volver",remarco)

        imagen_fondo = Widget(-15,0,ANCHO_VENTANA + 40,ALTO_VENTANA,"juego/recursos\decoracion/fondo_menu.png")

        lista_widgets = [imagen_fondo,boton_3,flecha_arriba,flecha_derecha,flecha_izquierda,flecha_abajo]
        
        
        super().__init__(lista_widgets, pantalla)
        
   