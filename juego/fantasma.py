import pygame
from recursos.configuraciones_fantasma import *
from recursos.configuraciones_mago import *
from funciones import obtener_rectangulos
from enemigo import Enemigo
from constantes import FPS


class Fantasma(Enemigo):
    def __init__(self,x,y) -> None:
        self.camina_derecha = lista_camina_derecha
        self.camina_izquierda = lista_camina_izquierda
        rectangulo_fantasma = pygame.transform.scale(self.camina_derecha[0],(60,60)).get_rect()
        rectangulo_fantasma.x = x
        rectangulo_fantasma.y = y
        lados_fantasma = obtener_rectangulos(rectangulo_fantasma)
        velocidad_movimiento = 10
        vidas = 3
        
        self.visibilidad = True
        
        poder = None
        distancia_poder = None
        velocidad_poder = None
        
        self.contador_general = 0
        self.cooldown_invisibilidad = 4
        self.contador_cooldown = 0
        

        super().__init__(x,y,velocidad_movimiento,rectangulo_fantasma,lados_fantasma,vidas,poder,distancia_poder,velocidad_poder,self.camina_derecha,self.camina_izquierda)
    


    def animar_imagen(self, lista_animaciones, pantalla, lados_enemigo):
            
        if self.visibilidad:
            self.velocidad_movimiento = 10
            if self.mira_derecha:
                self.img_derecha = self.camina_derecha
                
            else:
                self.img_izquierda = self.camina_izquierda 
                
                
            self.contador_general += 1
            if self.contador_general >= FPS * self.cooldown_invisibilidad:
                
                self.visibilidad = False
                self.contador_general = 0

       
        if not self.visibilidad:
            self.velocidad_movimiento = 13
            if self.mira_derecha:
                self.img_derecha = camina_derecha_invisible
                
            else:
                self.img_izquierda = camina_izquierda_invisible  
                
                
            self.contador_cooldown += 1
            

        if not self.visibilidad and (self.contador_cooldown >= self.cooldown_invisibilidad * FPS):
            
            self.visibilidad = True
            self.contador_cooldown = 0
            
        
         
        return super().animar_imagen(lista_animaciones, pantalla, lados_enemigo)
    
   