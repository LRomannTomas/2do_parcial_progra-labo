import pygame

#para implemetar despues

class Item:
    def __init__(self,nombre,path_imagen,precio,ancho=75,alto=75) -> None:
        self.nombre = nombre
        self.imagen = pygame.transform.scale(pygame.image.load(path_imagen),(ancho,alto))
        self.precio = precio
        
    
    def aplicar(self,jugador):
        pass


