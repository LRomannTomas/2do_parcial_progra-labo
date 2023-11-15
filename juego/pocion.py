import pygame
from item import Item

class Pocion(Item):
    def __init__(self) -> None:
        nombre = "pocion"
        path_imagen = "juego/recursos\iconos\pocion.png" 
        precio = 300
        
        
        super().__init__(nombre, path_imagen, precio)
        
        
    def aplicar(self,jugador):
        jugador.vidas += 1