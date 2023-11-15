import pygame
from nivel_uno import NivelUno
from nivel_dos import NivelDos  
from nivel_tres import NivelTres  


class ManejadorNiveles:
    def __init__(self,pantalla) -> None:
        self.pantalla = pantalla
        self.niveles = {1 : NivelUno, 2:NivelDos, 3 : NivelTres}
    
    def obtener_nivel(self,nombre_nivel,nombre_jugador):
        return self.niveles[nombre_nivel](self.pantalla,nombre_jugador)  