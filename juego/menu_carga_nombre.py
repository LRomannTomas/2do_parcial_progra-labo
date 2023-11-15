from menu import Menu
from text_box import TextBox
from widgets import Widget
from boton import Boton
from constantes import *
from selector_niveles import SelectorNiveles
import pygame



class MenuCargarNombre(Menu):
    def __init__(self, pantalla) -> None:
        
        ancho_boton = 180
        alto_boton = 100
        
        self.text_box = TextBox(150,200,1100,250,"8bitoperator8","juego/recursos/botones/remarco_boton.png","juego/recursos/botones/remarco_salir.png")
        self.text_box.place_holder_text = "nombre de usuario"
        
        remarco = pygame.transform.scale(pygame.image.load("juego/recursos/botones/remarco_boton.png"),(ancho_boton + 60,alto_boton + 60))
        remarco_btn_salir = pygame.transform.scale(pygame.image.load("juego/recursos/botones/remarco_salir.png"),(ancho_boton + 60,alto_boton + 60))
        
        boton_cargar = Boton(785,550,ancho_boton,alto_boton,"juego/recursos/botones/boton_cargar.png",self.abrir_selector_niveles,None,remarco)
        boton_salir = Boton(415,550,ancho_boton,alto_boton,"juego/recursos/botones/boton_salir.png",self.set_dialogo,"volver",remarco_btn_salir)
        fondo = Widget(-15,0,ANCHO_VENTANA + 40,ALTO_VENTANA,"juego/recursos\decoracion/fondo_menu.png")

        lista_widgets = [fondo,boton_cargar,boton_salir,self.text_box]
        
        super().__init__(lista_widgets, pantalla)
        
        
        
    def abrir_selector_niveles(self):
        nombre_sin_espacios = self.text_box.texto.strip()
        if nombre_sin_espacios != "":
            menu_selector_niveles = SelectorNiveles(self.pantalla,nombre_sin_espacios)
            self.set_hijo(menu_selector_niveles)