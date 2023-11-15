from nivel import Nivel
import pygame
from constantes import *
from personaje import *
from decoraciones import *
from mago import Mago

class NivelUno(Nivel):
    def __init__(self, pantalla: pygame.Surface,nombre_jugador):
        
        #---PLATAFORMAS----------------------------------------------------------------------------------------------------------------------------------------------------
        limite_enemigo_1 = Plataforma("juego/recursos\plataformas/1_v2.png",650,650,10,60)
        plataforma_1 = Plataforma("juego/recursos\plataformas/0.png",880,720,520,120)
        plataforma_2 = Plataforma("juego/recursos\plataformas/2.png",-30,610,400,400)
        plataforma_3 = Plataforma("juego/recursos\plataformas/5.png",210,690,450,455)
        
        plataforma_4 = Plataforma("juego/recursos\plataformas\plat.png",80,200,200,40)
        plataforma_5 = Plataforma("juego/recursos\plataformas\plat.png",410,300,80,20)
        plataforma_6 = Plataforma("juego/recursos\plataformas\plat.png",590,200,80,20)
        plataforma_7 = Plataforma("juego/recursos\plataformas\plat.png",460,140,60,20)
        plataforma_8 = Plataforma("juego/recursos\plataformas\plat.png",800,130,80,20)
        
        lista_plataformas = [plataforma_1,plataforma_2,plataforma_3,plataforma_4,plataforma_5,plataforma_6,plataforma_7,plataforma_8]
        
        
        #---JUGADOR--------------------------------------------------------------------------------------------------------------------------------------------------------
        jugador_1 = Personaje(30,430,10,-20)
        lados_personaje = obtener_rectangulos(jugador_1.rectangulo_personaje)
        limites_enemigo = [limite_enemigo_1] 
        
        #---Enemigos-------------------------------------------------------------------------------------------------------------------------------------------------------
        
        #Mago 
        mago_enemigo = Mago(550,630,6)
        
        lista_enemigos = [mago_enemigo]
        #---IMAGENES ESTATICAS--------------------------------------------------------------------------------------------------------------------------------------------
        
        #FONDO
        fondo_1 = Decoraciones("imagenes/assets_1/background/background_layer_1.png",0,0,ANCHO_VENTANA,ALTO_VENTANA)
        fondo_2 = Decoraciones("imagenes/assets_1/background/background_layer_2.png",0,0,ANCHO_VENTANA,ALTO_VENTANA)
        fondo_3 = Decoraciones("imagenes/assets_1/background/background_layer_3.png",0,0,ANCHO_VENTANA,ALTO_VENTANA)
        
        #FAROL
        farol = Decoraciones("juego/recursos\decoracion/0.png",900,620,35,100)
        
        #PIEDRAS
        piedra_1 = Decoraciones("juego/recursos\decoracion\piedra_1.png",330,590,30,20)
        piedra_2 = Decoraciones("juego/recursos\decoracion\piedra_2.png",600,660,50,30)
        piedra_3 = Decoraciones("juego/recursos\decoracion\piedra_3.png",100,570,100,40)
        
        
        
        lista_img_estaticas = [fondo_1,fondo_2,fondo_3,farol,piedra_1,piedra_2,piedra_3,plataforma_1,plataforma_2,plataforma_3,plataforma_4,plataforma_5,plataforma_6,plataforma_7,plataforma_8]
        
    
        #---IMAGENES ANIMADAS--------------------------------------------------------------------------------------------------------------------------------------------
        
        #TIENDA
        tienda = DecoracionesAnimadas(pantalla,tienda_animada,1020,450,270,270)
        
        #PASTO
        pasto = DecoracionesAnimadas(pantalla,pasto_animado,550,670,30,20)
        pasto_2 = DecoracionesAnimadas(pantalla,pasto_animado_invertido,290,595,30,20)
        pasto_3 = DecoracionesAnimadas(pantalla,pasto_animado,185,600,30,10)
        pasto_4 = DecoracionesAnimadas(pantalla,pasto_animado,15,595,40,20)
        pasto_5 = DecoracionesAnimadas(pantalla,pasto_animado,380,670,40,20)
        
        moneda_1 = DecoracionesAnimadas(pantalla,moneda_animada,477,117,20,20)
        moneda_2 = DecoracionesAnimadas(pantalla,moneda_animada,828,107,20,20)
        
        lista_llaves = []
        lista_monedas = [moneda_1,moneda_2]
        
        lista_img_animadas = [tienda,pasto,pasto_2,pasto_3,pasto_4,pasto_5]

        lista_disparos = []
        
        lista_escaleras = []
        
        lista_puertas = []
        
   
                
        #---TITULO--------------------------------------------------------------------------------------------------------------------------------------------------------
        pygame.display.set_caption("NIVEL 1")
        

        super().__init__(pantalla, jugador_1,lados_personaje, lista_enemigos,lista_plataformas,lista_img_estaticas,lista_img_animadas,limites_enemigo,lista_disparos,
        lista_monedas,lista_llaves,lista_escaleras,lista_puertas,nombre_jugador)
        
        self.tienda = tienda
         
    def update(self, lista_eventos):
        if self.jugador.rectangulo_personaje.x >= 1300:
            self.guardar_progreso_partida()
            self.supero_nivel = True
            
        return super().update(lista_eventos)