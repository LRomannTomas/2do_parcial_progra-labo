import pygame
from constantes import *


lista_trampas = [
    pygame.image.load("juego/recursos/trampas/1.png"),
    pygame.image.load("juego/recursos/trampas/2.png"),
    pygame.image.load("juego/recursos/trampas/3.png"),
    pygame.image.load("juego/recursos/trampas/4.png"),
    pygame.image.load("juego/recursos/trampas/5.png"),
]

class Trampa:
    def __init__(self,x,y) -> None:
        #self.imagen = pygame.transform.scale(pygame.image.load("juego/recursos/fuego/0.png"),(25,25)) #provisorio
        self.imagen = lista_trampas
        
        self.rectangulo_poder = self.imagen[0].get_rect()
        self.rectangulo_poder.centerx = x
        self.rectangulo_poder.bottom = y
        
        self.mostrar_trampa = False
        self.colisiono = False
        self.kill = False
        self.enfriamiento_trampa = 0
        self.duracion_trampa = 0
        
        self.frame = 0
    
    def colisiono_personaje (self):
        self.kill = True


    def dibujar_trampa(self,pantalla):
    
        if not self.kill:
            largo = len(self.imagen)
            if self.frame >= largo:
                self.frame = 0
            
            imagen = pygame.transform.scale(self.imagen[self.frame],(30,40))
            pantalla.blit(imagen,(self.rectangulo_poder.x,self.rectangulo_poder.y))
            self.frame += 1
            
            
    
    
    def update(self,pantalla):
    
        self.dibujar_trampa(pantalla)
        self.enfriamiento_trampa += 1
        if self.enfriamiento_trampa == FPS * 3:
            self.kill = False
            self.enfriamiento_trampa = 0
        
        self.duracion_trampa += 1
        if self.duracion_trampa == FPS * 3.5:
            self.kill = True
            self.duracion_trampa = 0