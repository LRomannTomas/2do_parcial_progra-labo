import pygame
from enemigo import Enemigo 
from recursos.configuraciones_mago import *
from funciones import obtener_rectangulos
from poder_mago import HechizoFuego
      
        
class Mago(Enemigo):
    def __init__(self, x, y,velocidad_mov):
        
        velocidad_movimiento = velocidad_mov
        if velocidad_movimiento != 0:
            mago_derecha = mago_camina
            mago_izquierda = camina_izquierda
        else:
            mago_derecha = mago_quieto_derecha
            mago_izquierda = quieto_izquierda
            
        rectangulo_mago = pygame.transform.scale(mago_derecha[0],(60,60)).get_rect()
        rectangulo_mago.x = x
        rectangulo_mago.y = y
        lados_mago = obtener_rectangulos(rectangulo_mago)
        vidas = 3
        
        poder = HechizoFuego
        distancia_poder = 140
        velocidad_poder = 15
        super().__init__(x,y,velocidad_movimiento,rectangulo_mago,lados_mago,vidas,poder,distancia_poder,velocidad_poder,mago_derecha,mago_izquierda)
    
    
        
    