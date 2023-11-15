import pygame
from constantes import *
from poder_mago import HechizoFuego
from hechizo_multiple import HechizoMultiple
from trampa import Trampa

class Enemigo:
    def __init__(self,x,y,velocidad_movimiento,rectangulo_enemigo,lados_enemigo,vidas,poder,distancia_poder,velocidad_poder,lista_imgs_derecha,lista_imgs_izquierda) :
        
        #rectangulo
        self.rectangulo_enemigo = rectangulo_enemigo
        self.lados_enemigo = lados_enemigo
        self.img_derecha = lista_imgs_derecha
        self.img_izquierda = lista_imgs_izquierda
        
        #movimiento
        self.velocidad_movimiento = velocidad_movimiento
        
        self.rectangulo_enemigo.x = x
        self.rectangulo_enemigo.y = y
        self.frame = 0 
        self.mira_derecha = True
        self.gravedad = 2.97
        
        self.salta = False
        self.esta_disparando = False
        self.animacion_disparo = False
        
        #interaccion con plataformas
        
        self.colisiono_plataforma = False
        self.bandera_toco_derecha = False
        self.bandera_toco_izquierda = False
        
        self.vidas = vidas
        self.kill = False
        self.visibilidad = True
        
        #poderes
        
        self.poder = poder
        self.contador = 0
        self.distancia_poder = distancia_poder
        self.velocidad_poder = velocidad_poder
    
    
        self.invocacion = None
        self.eliminar_enemigos = False

    def disparo(self,direccion,lista_disparos):
        if self.poder == HechizoFuego:
            nuevo_poder = self.poder(self.rectangulo_enemigo.x,self.rectangulo_enemigo.y,direccion,self.distancia_poder,self.velocidad_poder)
        elif self.poder == Trampa:
            nuevo_poder = self.poder(self.rectangulo_enemigo.x,self.rectangulo_enemigo.bottom - 23)
        else:
            nuevo_poder = None
        
        if nuevo_poder != None:
            lista_disparos.append(nuevo_poder)
        
    
        
    def animar_imagen(self,lista_animaciones,pantalla,lados_enemigo):
         
        
        largo_lista = len(lista_animaciones)
        if self.frame >= largo_lista:
            self.frame = 0
        
        imagen = lista_animaciones[self.frame]
            
        pantalla.blit(imagen,lados_enemigo["principal"])
        self.frame += 1    

        
    
    def verificar_colisiones(self,limites_enemigo,lados_enemigo,lista_plataformas,rect_jugador):
        
        
        for plataforma in lista_plataformas:
            
            if lados_enemigo["izquierda"].colliderect(plataforma.lados_plataforma["derecha"]) and not (lados_enemigo["abajo"].colliderect(plataforma.lados_plataforma["arriba"])):
                
                self.bandera_toco_derecha = False
                self.mira_derecha = True
                
            if lados_enemigo["derecha"].colliderect(plataforma.lados_plataforma["izquierda"]) and not (lados_enemigo["abajo"].colliderect(plataforma.lados_plataforma["arriba"])):
                self.bandera_toco_derecha = True
                self.mira_derecha = False
                        
                        
        for limite in limites_enemigo:
            if lados_enemigo["izquierda"].colliderect(limite.lados_plataforma["derecha"]):
                
                self.bandera_toco_derecha = False
                self.mira_derecha = True
                
            if lados_enemigo["derecha"].colliderect(limite.lados_plataforma["izquierda"]):
                self.bandera_toco_derecha = True
                
                self.mira_derecha = False
        
        
                
    def movimiento(self,lados_enemigo): 
        
        for lado in lados_enemigo:
            if self.mira_derecha and not self.bandera_toco_derecha and not self.esta_disparando:
                
                lados_enemigo[lado].x += self.velocidad_movimiento
           
            if not self.mira_derecha and self.bandera_toco_derecha and not self.esta_disparando:
                
                lados_enemigo[lado].x -= self.velocidad_movimiento
    
    
    
    def recibir_daño(self,daño):
        self.vidas -= daño
        
        
    def update(self,pantalla,limites_enemigo,lados_enemigo,lista_disparos,lista_plataformas,rect_jugador):
        
        
        if self.vidas > 0:

            self.verificar_colisiones(limites_enemigo,lados_enemigo,lista_plataformas,rect_jugador)
            if not self.animacion_disparo:
            
                if self.mira_derecha:
                    direccion = "derecha"
                    if not self.salta:
                        self.animar_imagen(self.img_derecha,pantalla,lados_enemigo)
                        
                    self.movimiento(lados_enemigo)
                    
                elif not self.mira_derecha:
                    direccion = "izquierda"
                    if not self.salta:
                        self.animar_imagen(self.img_izquierda,pantalla,lados_enemigo)
                        
                    self.movimiento(lados_enemigo)
            
            
            self.contador += 1
            if self.contador == FPS * 2:
                self.esta_disparando = True
                if not self.salta:
                    self.disparo(direccion,lista_disparos)
                self.contador = 0
            else:
                self.esta_disparando = False
                
        else:
            self.kill = True
            
            
        
        
       






