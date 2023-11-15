from nivel import Nivel
import pygame
from constantes import *
from personaje import *
from decoraciones import *
from mago_boss import MagoBoss



class NivelTres(Nivel):
    def __init__(self, pantalla: pygame.Surface,nombre_jugador):
        
        #---------------------------------------------------------------ATRIBUTOS PERSONAJE--------------------------------------------------------------------------------
        
        
        #piso
        plataforma_1 = Plataforma("juego/recursos\plataformas/0_v2.png",0,710,467,100) 
        plataforma_2 = Plataforma("juego/recursos\plataformas/0_v2.png",467,710,467,100)
        plataforma_3 = Plataforma("juego/recursos\plataformas/0_v2.png",934,710,467,100)
        
     
        
        
        fondo_1 = Decoraciones("imagenes/fondo_lvl_3/fondo_1.png",0,0,ANCHO_VENTANA,ALTO_VENTANA)
        fondo_2 = Decoraciones("imagenes/fondo_lvl_3/fondo_2.png",0,0,ANCHO_VENTANA,ALTO_VENTANA)
        fondo_3 = Decoraciones("imagenes/fondo_lvl_3/fondo_3.png",0,0,ANCHO_VENTANA,ALTO_VENTANA)
        fondo_4 = Decoraciones("imagenes/fondo_lvl_3/fondo_4.png",0,0,ANCHO_VENTANA,ALTO_VENTANA)
        
        
        
        lista_puertas =  []
        
        
        #estas 2 las separo porque una se anima y la otra no (reveer)
        
        lista_monedas = []
        lista_llaves = []  
        
        
        
        #objetos plataforma
        
        limite_1 = Plataforma("juego/recursos\plataformas/1_v2.png",0,400,15,300)
        limite_2 = Plataforma("juego/recursos\plataformas/1_v2.png",1390,400,15,300)
        
        lista_plataformas = [plataforma_1,plataforma_2,plataforma_3]
        lista_limites_enemigos = [limite_1,limite_2]
        
        #imagenes a mostrar
        lista_img_decorativas = [
            fondo_1,fondo_2,fondo_3,fondo_4,  
            plataforma_1,plataforma_2,plataforma_3
            ]
        
        
        lista_escaleras = []
        
        #player
        jugador_1 = Personaje(200,430,10,-20)
        lados_personaje = obtener_rectangulos(jugador_1.rectangulo_personaje)
        
        lista_img_animadas = []
        
        #enemigos--------------------------------------------------------
        
        
        #mago boss
        self.mago_boss = MagoBoss(600,510)
        lista_enemigos = [self.mago_boss]
        
        
            
        
        lista_disparos = []  

        
        
        #-----------------------------------------------------------------------------------------------------------------------------------------------------------------
        
            
        #titulo
        pygame.display.set_caption("NIVEL 3")
        
    

        super().__init__(pantalla, jugador_1,lados_personaje, lista_enemigos,lista_plataformas, lista_img_decorativas,lista_img_animadas,lista_limites_enemigos,
                        lista_disparos,lista_monedas,lista_llaves,lista_escaleras,lista_puertas,nombre_jugador)
    
    
    def update(self, lista_eventos):
        if self.mago_boss.kill:
            self.guardar_progreso_partida()
            self.supero_nivel = True
        return super().update(lista_eventos)
        