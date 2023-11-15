import pygame 
from manejador_niveles import *
from constantes import *
from boton import Boton
from menu import Menu
from contenedor_niveles import ContenedorNiveles
from widgets import Widget
import json



class SelectorNiveles(Menu):
    def __init__(self,pantalla,nombre_jugador):
        ancho_boton = 180
        alto_boton = 100
        remarco = pygame.transform.scale(pygame.image.load("juego/recursos/botones/remarco_boton.png"),(ancho_boton + 60,alto_boton + 60))
        remarco_btn_salir = pygame.transform.scale(pygame.image.load("juego/recursos/botones/remarco_salir.png"),(ancho_boton + 60,alto_boton + 60))
        
        self.nombre_jugador = nombre_jugador
        boton_1 = Boton(250,350,ancho_boton,alto_boton,"juego/recursos/botones/boton_nivel_1.png",self.cambiar_nivel,1,remarco)
        boton_2 = Boton(600,350,ancho_boton,alto_boton,"juego/recursos/botones/boton_nivel_2.png",self.cambiar_nivel,2,remarco)
        boton_3 = Boton(950,350,ancho_boton,alto_boton,"juego/recursos/botones/boton_nivel_3.png",self.cambiar_nivel,3,remarco)
        boton_4 = Boton(1150,650,ancho_boton,alto_boton,"juego/recursos/botones/boton_salir.png",self.set_dialogo,"volver",remarco_btn_salir)
        
        imagen_fondo = Widget(-15,0,ANCHO_VENTANA + 40,ALTO_VENTANA,"juego/recursos\decoracion/fondo_menu.png")
        
        lista_widgets = [imagen_fondo,boton_1,boton_2,boton_3,boton_4]
        
        self.manejador_niveles = ManejadorNiveles(pantalla)
        
        self.nivel_actual = None
        self.ultimo_nivel_superado = 0
        
        self.leer_progreso()
        
        
        
        super().__init__(lista_widgets,pantalla)


    def leer_progreso(self):
        
        try:
            
            with open('data.json') as file:
                data = json.load(file)
            
            
        except:
            data = {}
        
            
        if self.nombre_jugador in data:    
            data_jugador = data[self.nombre_jugador]
        else:
            data_jugador = {
                "ultimo_nivel_ganado": 0,
                "dinero" : 0,
                "items": []
                }
            
        self.ultimo_nivel_ganado = data_jugador["ultimo_nivel_ganado"]
        self.progreso_general = data
        self.progreso_individual = data_jugador

    
    
    def guardar_nivel_superado(self):
        self.leer_progreso()
        
        self.progreso_individual["ultimo_nivel_ganado"] = self.nivel_actual
        
        self.progreso_general[self.nombre_jugador] = self.progreso_individual
        
        
        with open('data.json', 'w') as file:
            json.dump(self.progreso_general, file, indent=4, ensure_ascii=False )
            
            
            
    def leer_dialogo(self):
        
        dialogo = self.get_dialogo()
        if dialogo == "supero nivel":
            if self.progreso_individual["ultimo_nivel_ganado"] < self.nivel_actual:
                self.guardar_nivel_superado()
        
            self.set_hijo(None) 
        else:
            super().leer_dialogo()
        
    
    
    def cambiar_nivel(self,numero_nivel):
        
        self.leer_progreso()
        if self.ultimo_nivel_ganado + 1 >= numero_nivel:
            nivel = self.manejador_niveles.obtener_nivel(numero_nivel,self.nombre_jugador)
            self.nivel_actual = numero_nivel
            contenedor_nivel = ContenedorNiveles(self.pantalla,nivel)
            self.formulario_hijo = contenedor_nivel
        