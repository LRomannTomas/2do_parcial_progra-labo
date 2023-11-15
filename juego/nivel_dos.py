from nivel import Nivel
import pygame
from constantes import *
from personaje import *
from decoraciones import *
from mago import Mago
from ladron import Ladron
from fantasma import Fantasma
from llave_recolectable import LlaveRecolectable


class NivelDos(Nivel):
    def __init__(self, pantalla: pygame.Surface,nombre_jugador):
        
        #---------------------------------------------------------------ATRIBUTOS PERSONAJE--------------------------------------------------------------------------------
        limite_enemigo_1 = Plataforma("juego/recursos\plataformas/0_v2.png",1390,520,10,60)
        limite_enemigo_2 = Plataforma("juego/recursos\plataformas/0_v2.png",40,650,10,60)
        
        
        plataforma_1 = Plataforma("juego/recursos\plataformas/0_v2.png",0,710,530,100) 
        plataforma_2 = Plataforma("juego/recursos\plataformas/0_v2.png",500,710,530,115)
        plataforma_3 = Plataforma("juego/recursos\plataformas/tierra.png",1200,610,200,200)
        plataforma_4 = Plataforma("juego/recursos\plataformas/0_v2.png",1200,580,300,100)
        plataforma_5 = Plataforma("juego/recursos\plataformas/0_v2.png",1060,650,300,100)
        plataforma_6 = Plataforma("juego/recursos\plataformas/0_v2.png",670,710,530,100)
        
        
        plataforma_7 = Plataforma("juego/recursos\plataformas/plataforma_madera_llana.png",740,510,140,40)
        plataforma_8 = Plataforma("juego/recursos\plataformas\plataforma_madera_llana.png",540,480,100,40)
        plataforma_9 = Plataforma("juego/recursos\plataformas/plataforma_madera_llana.png",330,460,100,40)
        plataforma_10 = Plataforma("juego/recursos\plataformas\plataforma_madera_izquierda.png",0,490,250,80)
        
        
        fondo_1 = Decoraciones("imagenes/fondo_lvl_2/fondo_2.png",0,0,ANCHO_VENTANA,ALTO_VENTANA)
        puerta_cerrada = Decoraciones("juego/recursos\decoracion\puerta_cerrada.png",50,375,85,120)
        puerta_abierta = Decoraciones("juego/recursos\decoracion\puerta_abierta.png",50,370,85,120)
        
        lista_puertas =  [puerta_cerrada,puerta_abierta]
        
        
        llave = LlaveRecolectable(1250,545) 
        
        escalera_1 = Plataforma("juego/recursos/decoracion/escalera_larga.png",180,510,40,200)
        
        
        #estas 2 las separo porque una se anima y la otra no (reveer)
        
        lista_monedas = []
        lista_llaves = [llave]  
        
        
        
        #objetos plataforma
        lista_plataformas = [plataforma_1,plataforma_2,plataforma_3,plataforma_4,plataforma_5,plataforma_6,plataforma_7,plataforma_8,plataforma_9,plataforma_10]
        
        lista_limites = [limite_enemigo_1,limite_enemigo_2]
        
        #imagenes a mostrar
        lista_img_decorativas = [
            fondo_1,  
            plataforma_1,plataforma_2,plataforma_3,plataforma_4,plataforma_5,plataforma_6,plataforma_7,plataforma_8,plataforma_9,plataforma_10,
            
            ]
        
        lista_escaleras = [escalera_1]
        
        #player
        jugador_1 = Personaje(200,430,10,-20)
        lados_personaje = obtener_rectangulos(jugador_1.rectangulo_personaje)
        
        
        lista_img_animadas = []
        
        #enemigos--------------------------------------------------------
        
        #mago
        mago_enemigo = Mago(1340,520,0)
        mago_enemigo.poder
        
        #ladron
        ladron_enemigo = Ladron(450,650)

        #fantasma 
        fantasma_enemigo = Fantasma(500,650)
        
        lista_enemigos = [mago_enemigo,ladron_enemigo,fantasma_enemigo]
        
        lista_disparos = []  

        
     
        #-----------------------------------------------------------------------------------------------------------------------------------------------------------------
        

        #titulo
        pygame.display.set_caption("NIVEL 2")
        
    

        super().__init__(pantalla, jugador_1,lados_personaje, lista_enemigos,lista_plataformas, lista_img_decorativas,lista_img_animadas,lista_limites,lista_disparos,
                         lista_monedas,lista_llaves,lista_escaleras,lista_puertas,nombre_jugador)
        
    def update(self, lista_eventos):
        if self.abrir_puerta:
            self.guardar_progreso_partida()
            self.supero_nivel = True
            
        return super().update(lista_eventos)

        