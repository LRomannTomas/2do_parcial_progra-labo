import pygame 
from enemigo import Enemigo
from recursos.configuraciones_mago_boss import *
from funciones import obtener_rectangulos
from hechizo_multiple import HechizoMultiple
from constantes import *
from fantasma import Fantasma


class MagoBoss(Enemigo):
    def __init__(self, x, y):
        quieto_derecha = boss_quieto_derecha
        quieto_izquierda = boss_quieto_izquierda
        camina_derecha = boss_camina_derecha
        camina_izquierda = boss_camina_izquierda
        rectangulo = quieto_derecha[0].get_rect() 
        rectangulo.x = x
        rectangulo.y = y
        lados = obtener_rectangulos(rectangulo)
        velocidad_movimiento = 8
        vidas = 40
        
        #poder
        poder = HechizoMultiple
        self.distancia_poder = 1200
        self.velocidad_poder = 15
        self.cantidad_disparos = 2
        self.separador_disparos = 120
        
        self.salta = False
        self.salto = -30
        self.limite_velocidad_caida = self.salto * -1
        self.mover_y = 0
        
        self.contador_animacion_disparo = 0
        
        self.contador_salto = 0
        self.cooldown_salto = 3
        
        self.contador_invocacion = 0
        self.cooldown_invocacion = 5
        
        self.invocacion = None
        
        
        super().__init__(x, y, velocidad_movimiento, rectangulo, lados,vidas, poder,self.distancia_poder,self.velocidad_poder, camina_derecha, camina_izquierda)
    
    def invocar_fantasmas(self):
        if not self.salta:
            self.contador_invocacion += 1
            if self.contador_invocacion == FPS * self.cooldown_invocacion:
                self.invocacion = Fantasma(self.rectangulo_enemigo.x,self.rectangulo_enemigo.y + 140)
                self.contador_invocacion = 0
            
    
    def disparo(self, direccion, lista_disparos):
        
        if self.poder == HechizoMultiple:
            separador = 0
            for i in range(self.cantidad_disparos):
                if self.mira_derecha:
                    lado_rect = self.rectangulo_enemigo.right
                else:
                    lado_rect = self.rectangulo_enemigo.left
                    
                nuevo_poder = self.poder(lado_rect,(self.rectangulo_enemigo.top)+ separador,direccion,self.distancia_poder,self.velocidad_poder)
                separador += self.separador_disparos
                lista_disparos.append(nuevo_poder)
                
        return super().disparo(direccion, lista_disparos)
    
    
    
    def barra_vida(self,pantalla,x,y):
        largo = 200
        ancho = 25
        calculo_barra = int((self.vidas / 100) * largo)
        borde = pygame.Rect(x,y,largo,ancho)
        rectangulo = pygame.Rect(x,y,calculo_barra,ancho)
        pygame.draw.rect(pantalla,COLOR_AZUL,borde,3)      #cambiar esto para que quede fachero
        pygame.draw.rect(pantalla,COLOR_NEGRO,rectangulo)
        corazon = pygame.image.load("juego/recursos\decoracion\corazon.png")
        
        pantalla.blit(pygame.transform.scale(corazon,(25,25)),(545,100))
        if self.vidas < 0:
            
            self.vidas = 0
        
    
    def verificar_colisiones(self, limites_enemigo, lados_enemigo, lista_plataformas,rect_jugador):
        
        
        if self.rectangulo_enemigo.colliderect(rect_jugador):
            if self.contador_salto >= FPS * self.cooldown_salto and not self.salta:
                self.salta = True
                self.contador_salto = 0
            
        self.contador_salto += 1
            
        return super().verificar_colisiones(limites_enemigo, lados_enemigo, lista_plataformas,rect_jugador)
    
    
    
    
    def movimiento(self, lados_enemigo):
        
        #modifico la cantidad de disparos segun la ubicacion actual del enemigo
        if self.rectangulo_enemigo.x == 800:
            self.cantidad_disparos = 2
            self.separador_disparos = 60
            
        if self.rectangulo_enemigo.x == 1224 or self.rectangulo_enemigo.x == 376:
            self.cantidad_disparos = 2
            self.separador_disparos = 140
    
        return super().movimiento(lados_enemigo)
    
    
    
    def corregir_desface_lados(self,lados_enemigo):
        
        lados_enemigo["arriba"].topleft = self.rectangulo_enemigo.topleft 
        lados_enemigo["izquierda"].bottomleft = self.rectangulo_enemigo.bottomleft
        lados_enemigo["derecha"].bottomright = self.rectangulo_enemigo.bottomright
        lados_enemigo["abajo"].bottomleft = self.rectangulo_enemigo.bottomleft
    
    
    
    def aplicar_gravedad(self,lista_animaciones,pantalla,lista_plataformas,lados_enemigo):
        
        if self.salta:
            
            self.animar_imagen(lista_animaciones,pantalla,lados_enemigo)
            
            
            for lado in lados_enemigo:
                lados_enemigo[lado].y += self.mover_y
            
            
            if self.mover_y + self.gravedad < self.limite_velocidad_caida:
                
                self.mover_y += self.gravedad

                    
        for plataforma in lista_plataformas:
            
            if lados_enemigo["abajo"].colliderect(plataforma.lados_plataforma["arriba"]):
                self.salta = False
                self.mover_y = 0
                lados_enemigo["principal"].bottom = plataforma.lados_plataforma["principal"].top + 1
                self.corregir_desface_lados(lados_enemigo)
                break
            
            else:
                self.salta = True
    
            if lados_enemigo["arriba"].colliderect(plataforma.lados_plataforma["abajo"]) :
                self.mover_y = self.limite_velocidad_caida
                
                
                
    def update(self, pantalla, limites_enemigo, lados_enemigo, lista_disparos, lista_plataformas, rect_jugador):
        
        self.barra_vida(pantalla,600,100)
        
        self.invocar_fantasmas()
        
        if (self.esta_disparando or self.animacion_disparo) and not self.salta:
            
            if self.contador_animacion_disparo == len(boss_ataque_1_derecha):
                self.animacion_disparo = False
                self.contador_animacion_disparo = 0
                self.esta_disparando = False
            else:
                if self.mira_derecha:
                    self.animar_imagen(boss_ataque_1_derecha,pantalla,lados_enemigo)
                else:
                    self.animar_imagen(boss_ataque_1_izquierda,pantalla,lados_enemigo)
                    
                self.animacion_disparo = True
                self.contador_animacion_disparo += 1
        
        elif self.mira_derecha:
            
            self.aplicar_gravedad(boss_salta_derecha,pantalla,lista_plataformas,lados_enemigo)
            
        else:
            self.aplicar_gravedad(boss_salta_izquierda,pantalla,lista_plataformas,lados_enemigo)
            
        
        if not self.salta:
            self.mover_y = self.salto
            
        if self.vidas <= 0:
            self.eliminar_enemigos = True
            
        return super().update(pantalla, limites_enemigo, lados_enemigo, lista_disparos, lista_plataformas, rect_jugador)