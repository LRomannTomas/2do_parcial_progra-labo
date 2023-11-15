import pygame
from item import Item

class Botas(Item):
    def __init__(self) -> None:
        
        nombre = "botas"
        path_imagen = "juego/recursos\iconos/botas.png"
        precio = 600
                
        super().__init__(nombre, path_imagen, precio)
        
        
    def aplicar(self,jugador):
        jugador.velocidad_camina += 2
        
    