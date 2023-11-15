import pygame
from menu import Menu
from widgets import Widget
from boton import Boton
from label import Label
from constantes import *
import json


class RankingPuntuaciones(Menu):
    def __init__(self, pantalla) -> None:
        ancho_boton = 180
        alto_boton = 100
        
        remarco = pygame.transform.scale(pygame.image.load("juego/recursos/botones/remarco_salir.png"),(ancho_boton + 60,alto_boton + 60))
        
        boton_3 = Boton(1150,650,ancho_boton,alto_boton,"juego/recursos/botones/boton_salir.png",self.set_dialogo,"volver",remarco)

        imagen_fondo = Widget(-15,0,ANCHO_VENTANA + 40,ALTO_VENTANA,"juego/recursos\decoracion/fondo_menu.png")

        
        lista_widgets = [imagen_fondo,boton_3]
        self.leer_progreso_partida()
        self.obtener_top(4)
        
        y = 100
        
        contador_top = 1
        for jugador in self.top_jugadores:
            puntaje_str = str(jugador["dinero"])
            nuevo_label_nombre = Label(100,y,700,70,jugador["nombre"],"juego/recursos/botones/Textbox.png")
            nuevo_label_puntaje = Label(850,y,300,70,puntaje_str,"juego/recursos/botones/Textbox.png")
            nuevo_label_numero_top = Label(20,y,50,70,str(contador_top),"juego/recursos/botones/Textbox.png")
            lista_widgets.append(nuevo_label_nombre)
            lista_widgets.append(nuevo_label_puntaje)
            lista_widgets.append(nuevo_label_numero_top)
            y += 140
            contador_top += 1

        super().__init__(lista_widgets, pantalla)
        
        
    def leer_progreso_partida(self):
        try:
            with open('data.json') as file:
                data = json.load(file)
       
        except:
            data = {}
            
        return data
    
    
    def obtener_top(self,cantidad):
        self.top_jugadores = []
        progreso = self.leer_progreso_partida()
        
        for i in range(cantidad):
            jugador_top = None
            
            for nombre_jugador in progreso:
                jugador = progreso[nombre_jugador]
                if jugador_top == None or jugador["dinero"] > jugador_top["dinero"] :
                    jugador_top = {"nombre" : nombre_jugador, "dinero" : jugador["dinero"]}
                    
                    
            if jugador_top != None:
                self.top_jugadores.append(jugador_top)
                progreso.pop(jugador_top["nombre"])
                