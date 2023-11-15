import pygame
from enemigo import Enemigo
from recursos.configuraciones_ladron import *
from funciones import obtener_rectangulos
from trampa import Trampa

      
        
class Ladron(Enemigo):
    def __init__(self, x, y):
        camina_derecha = ladron_camina_derecha
        camina_izquierda = ladron_camina_izquierda
        rectangulo_ladron = pygame.transform.scale(camina_derecha[0],(60,60)).get_rect() 
        rectangulo_ladron.x = x
        rectangulo_ladron.y = y
        lados_ladron = obtener_rectangulos(rectangulo_ladron)
        velocidad_movimiento = 10
        poder = Trampa
        distancia_poder = None
        velocidad_poder = None
        vidas = 3
         
        super().__init__(x, y,velocidad_movimiento, rectangulo_ladron,lados_ladron,vidas,poder,distancia_poder,velocidad_poder, camina_derecha, camina_izquierda)
        
                