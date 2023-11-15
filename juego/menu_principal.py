import pygame
from menu import Menu
from widgets import Widget
from boton import Boton
from constantes import *
from menu_carga_nombre import MenuCargarNombre
from menu_controles import MenuControles
from ranking_puntajes import RankingPuntuaciones



class MenuPrincipal(Menu):
    def __init__(self, pantalla):
        
        ancho_boton = 180
        alto_boton = 100
        
        remarco = pygame.transform.scale(pygame.image.load("juego/recursos/botones/remarco_boton.png"),(ancho_boton + 60,alto_boton + 60))
        
        remarco_btn_salir = pygame.transform.scale(pygame.image.load("juego/recursos/botones/remarco_salir.png"),(ancho_boton + 60,alto_boton + 60))
        
        boton_jugar = Boton(250,350,ancho_boton,alto_boton,"juego/recursos/botones/boton_jugar.png",self.abrir_cargar_nombre,None,remarco)
        
         
        boton_controles = Boton(600,350,ancho_boton,alto_boton,"juego/recursos/botones/boton_controles.png",self.abrir_controles,None,remarco)
        

        boton_ranking = Boton(950,350,ancho_boton,alto_boton,"juego/recursos/botones/boton_puntaje.png",self.abrir_ranking,None,remarco)
        
        
        boton_salir = Boton(600,600,ancho_boton,alto_boton,"juego/recursos/botones/boton_salir.png",self.set_dialogo,"volver",remarco_btn_salir)  #implementar cerrar el juego con este btn
        
        
        imagen_fondo = Widget(-15,0,ANCHO_VENTANA + 40,ALTO_VENTANA,"juego/recursos\decoracion/fondo_menu.png")
        

        lista_widgets = [imagen_fondo,boton_jugar,boton_controles,boton_ranking,boton_salir]
        
        
        super().__init__(lista_widgets, pantalla)
    
    
    def abrir_cargar_nombre(self):
        menu_cargar_nombre = MenuCargarNombre(self.pantalla)
        self.set_hijo(menu_cargar_nombre)
    
    
    def abrir_controles(self):
        menu_controles = MenuControles(self.pantalla)
        self.set_hijo(menu_controles)
        
    def abrir_ranking(self):
        ranking_puntuaciones = RankingPuntuaciones(self.pantalla)
        self.set_hijo(ranking_puntuaciones)
    