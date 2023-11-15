import pygame
from constantes import *
from recursos.configuraciones_personaje import *
from plataforma_1 import *
from fantasma import Fantasma
from pocion import Pocion
from botas import Botas


class Personaje:
    def __init__(self,x,y,velocidad_camina,salto):
        self.imagen = pygame.transform.scale(personaje_camina[0],(60,60))
        self.rectangulo_personaje = self.imagen.get_rect()
        self.rectangulo_personaje.x = x
        self.rectangulo_personaje.y = y   
        self.estado = "quieto"
        self.frame = 0
        self.debug = False
        self.checkpoint = (30,0)

        #dinero
        self.dinero = 0

        #vida y daño recibido
        self.vidas = 3
        self.colisiono_poder = False
        self.colisiono_enemigo = False
        self.imagen_corazon = pygame.transform.scale(pygame.image.load("juego/recursos\decoracion\corazon.png"),(40,40))
        
        #salto
        self.gravedad = 2.97
        self.salto = salto
        self.esta_saltando = False
        self.limite_velocidad_caida = salto * -1
        
        #movimiento
        self.mira_derecha = True
        self.velocidad_camina = velocidad_camina
        self.mover_x = 0
        self.mover_y = 0
        self.bandera_toco_derecha = False
        self.bandera_toco_izquierda = False
        self.toco_escalera = False
        
        #daño 
        self.daño = 10
        self.esta_golpeando = False
        
        #manejo de tiempos
        self.cooldown_inmunidad = 2
        self.contador_inmunidad = 0
        self.puede_perder_vida = True
        
        self.duracion_animacion = 0.5
        self.contador_animacion = 0
        
        self.cooldown_ataque = 0.5
        self.contador_cooldown = 0
        
        #items
        self.lista_items = []
        
        self.toco_puerta = False
        
    
    def añadir_item(self,item):
        if type(item) == Pocion and self.dinero >= 300:
            self.lista_items.append(item)
            self.dinero -= item.precio
            
        elif type(item) == Botas and self.dinero >=600:
            self.lista_items.append(item)
            self.dinero -= item.precio
            
        
    
    
    def aplicar_gravedad(self,lista_animaciones,pantalla,lista_plataformas,lados_personaje):
        
        
        if self.esta_saltando and not self.toco_escalera:
            self.animar_personaje(lista_animaciones,pantalla,lados_personaje)
            
            for lado in lados_personaje:
                lados_personaje[lado].y += self.mover_y
            
            
            if self.mover_y + self.gravedad < self.limite_velocidad_caida:
            
                self.mover_y += self.gravedad

                    
        for plataforma in lista_plataformas:
            
            if lados_personaje["abajo"].colliderect(plataforma.lados_plataforma["arriba"]):
                self.esta_saltando = False
                self.mover_y = 0
                lados_personaje["principal"].bottom = plataforma.lados_plataforma["principal"].top + 1
                self.corregir_desface_lados(lados_personaje)
                break
            
            else:
                self.esta_saltando = True
    
    
            if lados_personaje["arriba"].colliderect(plataforma.lados_plataforma["abajo"]) and not self.toco_escalera:
                self.mover_y = self.limite_velocidad_caida
                
                
    def corregir_desface_lados(self,lados_personaje):
        
        lados_personaje["arriba"].topleft = self.rectangulo_personaje.topleft 
        lados_personaje["izquierda"].bottomleft = self.rectangulo_personaje.bottomleft
        lados_personaje["derecha"].bottomright = self.rectangulo_personaje.bottomright
        lados_personaje["abajo"].bottomleft = self.rectangulo_personaje.bottomleft
    
    
    def verificar_caida_vacio(self,pantalla,lados_personaje):
        if self.rectangulo_personaje.y > pantalla.get_height():
            self.rectangulo_personaje.center = self.checkpoint
            self.corregir_desface_lados(lados_personaje)
            self.vidas -= 1
                   
    
    def verificar_colisiones(self,lista_poderes,lista_plataformas,lados_personaje,lista_enemigos,lista_monedas,lista_llaves,lista_escaleras,lista_puertas):
       
        self.bandera_toco_derecha = False
        self.bandera_toco_izquierda = False
       
        for plataforma in lista_plataformas:
            if lados_personaje["derecha"].colliderect(plataforma.lados_plataforma["izquierda"]) and not(lados_personaje["abajo"].colliderect(plataforma.lados_plataforma["arriba"])):
                self.bandera_toco_derecha = True
    
            if lados_personaje["izquierda"].colliderect(plataforma.lados_plataforma["derecha"]) and not(lados_personaje["abajo"].colliderect(plataforma.lados_plataforma["arriba"])):
                self.bandera_toco_izquierda = True
        
        
        self.colisiono_poder = False
        for poder in lista_poderes:
            if lados_personaje["principal"].colliderect(poder.rectangulo_poder):
                
                self.colisiono_poder = True
                poder.colisiono_personaje()
                
                
        self.colisiono_enemigo = False
        for enemigo in lista_enemigos:
            if type(enemigo) == Fantasma and not enemigo.visibilidad:
                if lados_personaje["principal"].colliderect(enemigo.rectangulo_enemigo):
                    self.colisiono_enemigo = True
                    
                    
        for moneda in lista_monedas:
            if lados_personaje["principal"].colliderect(moneda.rectangulo_imagen):
                moneda.mostrar = False
                self.dinero += 150
                print(self.dinero)
                break
        
        
        for llave in lista_llaves:
            if lados_personaje["principal"].colliderect(llave.rectangulo):
                llave.mostrar = False
                break
        
        
        for escalera in lista_escaleras:
            if lados_personaje["principal"].colliderect(escalera.rectangulo_imagen):
                self.toco_escalera = True
            else:
                self.toco_escalera = False
            
            
        for puerta in lista_puertas:
            if lados_personaje["principal"].colliderect(puerta.rectangulo_imagen):
                self.toco_puerta = True
            else:
                self.toco_puerta = False
            

    def atacar(self,lista_enemigos):
        if not self.esta_golpeando and self.contador_cooldown <= 0 and not self.esta_saltando:
            self.esta_golpeando = True
            self.estado = "quieto"
            for enemigo in lista_enemigos:
                if enemigo.visibilidad:
                    if self.rectangulo_personaje.colliderect(enemigo.rectangulo_enemigo):
                        enemigo.recibir_daño(self.daño)
           
            
    def control_vidas(self,pantalla):
        
        separador = 50
        
        self.contador_inmunidad += 1
        if self.contador_inmunidad >= FPS * self.cooldown_inmunidad:
            self.contador_inmunidad = 0
            self.puede_perder_vida = True
            
        if self.colisiono_enemigo and self.puede_perder_vida:
            self.puede_perder_vida = False
            self.vidas -= 1
            
        
        if self.colisiono_poder:    
            self.vidas -= 1
        
        for i in range(self.vidas):
            
            pantalla.blit(self.imagen_corazon,(1100 + separador *i,30))
        
        
            
    def control(self,velocidad_camina,lados_personaje):
        
        for lado in lados_personaje:
            
            if self.toco_escalera and self.estado == "sube escalera":
                lados_personaje[lado].y -= 5
                
            if (self.mira_derecha and not self.bandera_toco_derecha) or (not self.mira_derecha and not self.bandera_toco_izquierda):
                lados_personaje[lado].x += velocidad_camina
        

                
        
    
    def animar_personaje(self,lista_animaciones,pantalla,lados_personaje):
        largo = len(lista_animaciones)
        
        if self.frame >= largo:
            if lista_animaciones == personaje_salta_derecha or lista_animaciones == personaje_salta_izquierda:
                self.frame = self.frame -1
            else:
                self.frame = 0
                
        imagen = pygame.transform.scale(lista_animaciones[self.frame],(60,60))
        pantalla.blit(imagen,lados_personaje["principal"])
        self.frame += 1
        
        
        
    def update(self,pantalla,lados_personaje,lista_poderes,lista_plataformas,lista_enemigos,lista_monedas,lista_llaves,lista_escaleras,lista_puertas):

        
        if self.vidas > 0:
           
            self.verificar_colisiones(lista_poderes,lista_plataformas,lados_personaje,lista_enemigos,lista_monedas,lista_llaves,lista_escaleras,lista_puertas)
            
            self.control_vidas(pantalla)
            self.verificar_caida_vacio(pantalla,lados_personaje)
            
            self.contador_cooldown -= 1
            
            esta_trepando = (self.toco_escalera and self.esta_saltando) or self.estado == "sube escalera"
            
            if esta_trepando:
                self.animar_personaje(personaje_trepa,pantalla,lados_personaje)
                
                self.control(0,lados_personaje)    
            
            
            
            if self.esta_golpeando and self.contador_cooldown <= 0:
                
                if self.contador_animacion == FPS * self.duracion_animacion:
                
                    self.esta_golpeando = False
                    self.contador_animacion = 0
                    self.contador_cooldown = FPS * self.cooldown_ataque
                            
                if not self.esta_saltando:
                    self.animar_personaje(personaje_golpea_basico,pantalla,lados_personaje)

                self.contador_animacion += 1
            
                
                
            elif self.estado == "derecha":
                self.mira_derecha = True
                
                if not self.esta_saltando and not esta_trepando:
                    self.animar_personaje(personaje_camina,pantalla,lados_personaje)
                
                    
                self.control(self.velocidad_camina,lados_personaje)
                
                
            elif self.estado == "izquierda":
                self.mira_derecha = False
                
                if not self.esta_saltando and not esta_trepando:
                    self.animar_personaje(personaje_camina_izquierda, pantalla,lados_personaje)
                    
                self.control(self.velocidad_camina * -1,lados_personaje)
            
                
            
            elif self.estado == "salta" :
                
                if not self.esta_saltando and not esta_trepando :
                    self.esta_saltando = True
                    self.mover_y = self.salto

                
                
            elif self.estado == "quieto":
                
                if not self.esta_saltando and not esta_trepando:
                    
                    if self.mira_derecha:
                        self.animar_personaje(personaje_quieto_derecha,pantalla,lados_personaje)
                    else:
                        self.animar_personaje(personaje_quieto_izquierda,pantalla,lados_personaje)

            
            
            if self.mira_derecha:     
                self.aplicar_gravedad(personaje_salta_derecha,pantalla,lista_plataformas,lados_personaje)
                
            else:
                self.aplicar_gravedad(personaje_salta_izquierda,pantalla,lista_plataformas,lados_personaje)
                
                
        else:
            fuente = pygame.font.SysFont("Arial",50)
            fuente_1 = pygame.font.SysFont("Arial",52)
            texto_1 = fuente.render("GAME OVER",True,COLOR_BLANCO)
            texto_2 = fuente_1.render("GAME OVER",True,COLOR_NEGRO)
            
            rect_fuente = texto_1.get_rect()
            rect_fuente.center = (pantalla.get_width()/2,pantalla.get_height()/2)
            rect_fuente_2 = texto_2.get_rect()
            rect_fuente_2.center = (pantalla.get_width()/2,pantalla.get_height()/2)
            
            pantalla.blit(texto_2,rect_fuente_2)
            pantalla.blit(texto_1,rect_fuente)
            
            

    
            
            
    
        
    
    
    
 
        
  
    
            