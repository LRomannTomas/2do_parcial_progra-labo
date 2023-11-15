
import pygame
from funciones import girar_imagen


personaje_quieto_derecha = [
    pygame.image.load("juego/recursos\personaje/quieto/0.png"),
    pygame.image.load("juego/recursos\personaje/quieto/1.png"),
    pygame.image.load("juego/recursos\personaje/quieto/2.png"),
    pygame.image.load("juego/recursos\personaje/quieto/3.png"),
    pygame.image.load("juego/recursos\personaje/quieto/4.png"),
    pygame.image.load("juego/recursos\personaje/quieto/5.png")
]

personaje_camina = [
    pygame.image.load("juego/recursos\personaje/camina/0.png"),
    pygame.image.load("juego/recursos\personaje/camina/1.png"),
    pygame.image.load("juego/recursos\personaje/camina/2.png"),
    pygame.image.load("juego/recursos\personaje/camina/3.png"),
    pygame.image.load("juego/recursos\personaje/camina/4.png"),
    pygame.image.load("juego/recursos\personaje/camina/5.png"),
    pygame.image.load("juego/recursos\personaje/camina/6.png"),
    pygame.image.load("juego/recursos\personaje/camina/7.png")
    
]

personaje_salta_derecha = [
    pygame.image.load("juego/recursos\personaje/salta/0.png"),
    pygame.image.load("juego/recursos\personaje/salta/1.png"),
    pygame.image.load("juego/recursos\personaje/salta/2.png"),
    pygame.image.load("juego/recursos\personaje/salta/3.png"),
    pygame.image.load("juego/recursos\personaje/salta/4.png"),
    pygame.image.load("juego/recursos\personaje/salta/5.png"),
    pygame.image.load("juego/recursos\personaje/salta/6.png"),
    pygame.image.load("juego/recursos\personaje/salta/7.png"),
    pygame.image.load("juego/recursos\personaje/caida/0.png"),
    pygame.image.load("juego/recursos\personaje/caida/1.png"),
    pygame.image.load("juego/recursos\personaje/caida/2.png"),
    pygame.image.load("juego/recursos\personaje/caida/3.png"),
    pygame.image.load("juego/recursos\personaje/caida/4.png"),
    pygame.image.load("juego/recursos\personaje/caida/5.png"),

]

personaje_golpea_basico = [
    pygame.image.load("juego/recursos\personaje/golpe_basico/0.png"),
    pygame.image.load("juego/recursos\personaje/golpe_basico/1.png"),
    pygame.image.load("juego/recursos\personaje/golpe_basico/2.png"),
    pygame.image.load("juego/recursos\personaje/golpe_basico/3.png"),
    pygame.image.load("juego/recursos\personaje/golpe_basico/4.png"),
    pygame.image.load("juego/recursos\personaje/golpe_basico/5.png"),
    pygame.image.load("juego/recursos\personaje/golpe_basico/6.png"),
    pygame.image.load("juego/recursos\personaje/golpe_basico/7.png")
    
]

personaje_trepa = [
    pygame.image.load("juego/recursos\personaje/trepa/0.png"),
    pygame.image.load("juego/recursos\personaje/trepa/1.png"),
    pygame.image.load("juego/recursos\personaje/trepa/2.png"),
    pygame.image.load("juego/recursos\personaje/trepa/3.png"),
    pygame.image.load("juego/recursos\personaje/trepa/4.png"),
    pygame.image.load("juego/recursos\personaje/trepa/5.png"),
    pygame.image.load("juego/recursos\personaje/trepa/6.png"),
    pygame.image.load("juego/recursos\personaje/trepa/7.png"),
    pygame.image.load("juego/recursos\personaje/trepa/8.png"),
    pygame.image.load("juego/recursos\personaje/trepa/9.png"),
    
]

personaje_quieto_izquierda = girar_imagen(personaje_quieto_derecha,True,False)
personaje_camina_izquierda = girar_imagen(personaje_camina,True,False)
personaje_salta_izquierda = girar_imagen(personaje_salta_derecha,True,False)