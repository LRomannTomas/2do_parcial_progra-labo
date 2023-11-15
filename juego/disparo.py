import pygame
from plataforma_1 import *
from funciones import *


class Disparo:
    def __init__(self,x,y,direccion,lista_img_derecha,lista_img_izquierda,velocidad_disparo,distancia) -> None:
        
        self.img_derecha = lista_img_derecha
        self.img_izquierda = lista_img_izquierda
        self.rectangulo_poder = self.img_derecha[0].get_rect()
        self.rectangulo_poder.centerx = x
        self.rectangulo_poder.top = y
        self.mostrar_disparo = False
        self.frame = 0
        self.velocidad_disparo = velocidad_disparo
        self.mover_x = 0
        self.recorrido_disparo = 0
        self.distancia_maxima_disparo = distancia
        self.colisiono = False
        self.kill = False
        self.direccion = direccion
        
    def verificar_colisiones(self,lista_plataformas):
        for plataforma in lista_plataformas:
            if self.rectangulo_poder.colliderect(plataforma.lados_plataforma["principal"]):
                self.kill = True
                
        
    def colisiono_personaje(self):
        self.kill = True
         
    
    def movimiento(self,lista_plataformas):
        self.verificar_colisiones(lista_plataformas)
        if self.recorrido_disparo < self.distancia_maxima_disparo and not self.kill: 
            
            self.mostrar_disparo = True
            if self.direccion == "izquierda":
                self.mover_x = 0
                self.mover_x += self.velocidad_disparo * -1
                
                self.recorrido_disparo += self.mover_x * -1
            
            elif self.direccion == "derecha":
                self.mover_x = 0
                self.mover_x += self.velocidad_disparo 
                
                self.recorrido_disparo += self.mover_x
                
            
            self.rectangulo_poder.x += self.mover_x
        else:
            self.kill = True 
        
            
        
    def dibujar_disparo(self,pantalla):
        
        if not self.kill:
            if self.direccion == "izquierda":
                lista_imagenes = self.img_izquierda
            elif self.direccion == "derecha":
                lista_imagenes = self.img_derecha
                
                
            largo = len(lista_imagenes)
            
            if self.frame >= largo:    
                self.frame = 0
                    
            imagen = lista_imagenes[self.frame]
            pantalla.blit(imagen,self.rectangulo_poder)
            self.frame += 1
        
        
    def update(self,pantalla,lista_plataformas):
        self.dibujar_disparo(pantalla)
        self.movimiento(lista_plataformas)
        
        
        

        
        
            
        