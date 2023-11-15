import pygame
from item import Item

class Llave(Item):
    def __init__(self) -> None:
        nombre = "llave"
        path_imagen = "juego/recursos\iconos\key.png" 
        ancho_imagen = 25
        alto_imagen = 25
        precio = 0
        
        self.mostrar = True
        
        super().__init__(nombre, path_imagen, precio,ancho_imagen,alto_imagen)
        
        
    