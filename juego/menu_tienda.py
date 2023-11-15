
from menu import Menu
from boton import Boton
from widgets import Widget
from pocion import Pocion
from botas import Botas

class MenuTienda(Menu):
    def __init__(self, pantalla,jugador) :
        
        self.jugador = jugador
        
        self.fondo = Widget(400,90,600,600,"juego/recursos/botones/remarco_menu_tienda.png")
        
        
        self.boton_pocion = Boton(560,250,100,100,"juego/recursos\iconos\marco_pocion.png",self.añadir_item,Pocion)
        
        self.boton_botas = Boton(730,250,100,100,"juego/recursos\iconos/marco_botas.png",self.añadir_item,Botas)
        
        self.boton_volver = Boton(650,560,100,50,"juego/recursos/botones/boton_salir_tienda.png",self.set_dialogo,"volver")
        
        lista_widgets = [self.fondo,self.boton_pocion,self.boton_botas,self.boton_volver]
        
        
        super().__init__(lista_widgets, pantalla)
    


    def añadir_item(self,item):
        item_añadir = item()        
        self.jugador.añadir_item(item_añadir)
        

        
    
    
    
        
    
    
    