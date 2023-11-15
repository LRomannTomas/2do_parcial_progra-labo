import pygame
from constantes import *
from funciones import girar_imagen
from plataforma_1 import *


class Decoraciones:
    def __init__(self,path,eje_x,eje_y,ancho,largo) -> None:
        self.imagen = pygame.image.load(path)
        self.imagen = pygame.transform.scale(self.imagen,(ancho,largo))
        self.rectangulo_imagen = self.imagen.get_rect()
        self.rectangulo_imagen.x = eje_x
        self.rectangulo_imagen.y = eje_y


class DecoracionesAnimadas:
    def __init__(self,pantalla,lista_imagenes,eje_x,eje_y,ancho,alto):
        
        self.lista_imagenes = lista_imagenes
        self.pantalla = pantalla
        self.frame = 0
        self.rectangulo_imagen = pygame.transform.scale(self.lista_imagenes[self.frame],(ancho,alto)).get_rect()
        self.rectangulo_imagen.x = eje_x
        self.rectangulo_imagen.y = eje_y
        self.ancho_imagen = ancho
        self.alto_imagen = alto
        self.mostrar = True
        
    def animar_imagen(self):
        if self.mostrar:
            largo = len(self.lista_imagenes)
            if self.frame >= largo:
                self.frame = 0
            
            imagen = pygame.transform.scale(self.lista_imagenes[self.frame],(self.ancho_imagen,self.alto_imagen))
            self.pantalla.blit(imagen,(self.rectangulo_imagen.x,self.rectangulo_imagen.y))
            self.frame += 1
    
    def update(self):
        self.animar_imagen()
        


pasto_animado = [
    pygame.image.load("juego/recursos\decoracion\grass_1.png"),
    pygame.image.load("juego/recursos\decoracion\grass_1.png"),
    pygame.image.load("juego/recursos\decoracion\grass_1.png"),
    pygame.image.load("juego/recursos\decoracion\grass_2.png"),
    pygame.image.load("juego/recursos\decoracion\grass_2.png"),
    pygame.image.load("juego/recursos\decoracion\grass_2.png"),
    pygame.image.load("juego/recursos\decoracion\grass_3.png"),
    pygame.image.load("juego/recursos\decoracion\grass_3.png"),
    pygame.image.load("juego/recursos\decoracion\grass_3.png"),

    ]

fuego_animado = [
    pygame.image.load("juego/recursos/fuego/0.png"),
    pygame.image.load("juego/recursos/fuego/1.png"),
    pygame.image.load("juego/recursos/fuego/2.png"),
    pygame.image.load("juego/recursos/fuego/3.png"),
    pygame.image.load("juego/recursos/fuego/4.png"),
    pygame.image.load("juego/recursos/fuego/5.png"),
    pygame.image.load("juego/recursos/fuego/6.png"),
    pygame.image.load("juego/recursos/fuego/7.png")
    
    ]

tienda_animada = [
        pygame.image.load("juego/recursos\decoracion/1.png"),
        pygame.image.load("juego/recursos\decoracion/1.png"),
        pygame.image.load("juego/recursos\decoracion/2.png"),
        pygame.image.load("juego/recursos\decoracion/2.png"),
        pygame.image.load("juego/recursos\decoracion/3.png"),
        pygame.image.load("juego/recursos\decoracion/3.png"),
        pygame.image.load("juego/recursos\decoracion/4.png"),
        pygame.image.load("juego/recursos\decoracion/4.png"),
        pygame.image.load("juego/recursos\decoracion/5.png"),
        pygame.image.load("juego/recursos\decoracion/5.png")
        ]

moneda_animada =[
    pygame.image.load("juego/recursos\monedas\moneda_1.png"),
    pygame.image.load("juego/recursos\monedas\moneda_2.png"),
    pygame.image.load("juego/recursos\monedas\moneda_3.png"),
    pygame.image.load("juego/recursos\monedas\moneda_4.png"),
    pygame.image.load("juego/recursos\monedas\moneda_5.png"),
    pygame.image.load("juego/recursos\monedas\moneda_6.png"),
    pygame.image.load("juego/recursos\monedas\moneda_7.png"),
    pygame.image.load("juego/recursos\monedas\moneda_8.png"),
    pygame.image.load("juego/recursos\monedas\moneda_9.png"),
    pygame.image.load("juego/recursos\monedas\moneda_10.png"),
    pygame.image.load("juego/recursos\monedas\moneda_11.png"),
    pygame.image.load("juego/recursos\monedas\moneda_12.png"),
    pygame.image.load("juego/recursos\monedas\moneda_13.png"),
    pygame.image.load("juego/recursos\monedas\moneda_14.png"),
    pygame.image.load("juego/recursos\monedas\moneda_15.png"),
]

lista_imagenes_llave = [
    pygame.image.load("juego/recursos\iconos\key.png")
]

pasto_animado_invertido = girar_imagen(pasto_animado,True,False)