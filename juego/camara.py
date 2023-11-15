from typing import Iterable, Union
import pygame
from pygame.sprite import AbstractGroup

class CamaraEjeY(pygame.sprite.Group):
    def __init__(self) :
        super().__init__()
    
        self.pantalla = pygame.display.get_surface()