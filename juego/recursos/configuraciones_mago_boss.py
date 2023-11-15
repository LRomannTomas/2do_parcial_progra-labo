import pygame
from funciones import girar_imagen


boss_quieto_derecha = [
    pygame.transform.scale(pygame.image.load("juego/recursos\primer_boss\quieto\quieto_1.png"),(150,200)),
    pygame.transform.scale(pygame.image.load("juego/recursos\primer_boss\quieto\quieto_2.png"),(150,200)),
    pygame.transform.scale(pygame.image.load("juego/recursos\primer_boss\quieto\quieto_3.png"),(150,200)),
    pygame.transform.scale(pygame.image.load("juego/recursos\primer_boss\quieto\quieto_4.png"),(150,200)),
    pygame.transform.scale(pygame.image.load("juego/recursos\primer_boss\quieto\quieto_5.png"),(150,200)),
    
]

boss_camina_derecha = [
    pygame.transform.scale(pygame.image.load("juego/recursos\primer_boss\camina\camina_1.png"),(150,200)),
    pygame.transform.scale(pygame.image.load("juego/recursos\primer_boss\camina\camina_1.png"),(150,200)),
    pygame.transform.scale(pygame.image.load("juego/recursos\primer_boss\camina\camina_2.png"),(150,200)),
    pygame.transform.scale(pygame.image.load("juego/recursos\primer_boss\camina\camina_2.png"),(150,200)),
    pygame.transform.scale(pygame.image.load("juego/recursos\primer_boss\camina\camina_3.png"),(150,200)),
    pygame.transform.scale(pygame.image.load("juego/recursos\primer_boss\camina\camina_3.png"),(150,200)),
    pygame.transform.scale(pygame.image.load("juego/recursos\primer_boss\camina\camina_4.png"),(150,200)),
    pygame.transform.scale(pygame.image.load("juego/recursos\primer_boss\camina\camina_4.png"),(150,200)),
    pygame.transform.scale(pygame.image.load("juego/recursos\primer_boss\camina\camina_5.png"),(150,200)),
    pygame.transform.scale(pygame.image.load("juego/recursos\primer_boss\camina\camina_5.png"),(150,200)),
    pygame.transform.scale(pygame.image.load("juego/recursos\primer_boss\camina\camina_6.png"),(150,200)),
    pygame.transform.scale(pygame.image.load("juego/recursos\primer_boss\camina\camina_6.png"),(150,200)),
    pygame.transform.scale(pygame.image.load("juego/recursos\primer_boss\camina\camina_7.png"),(150,200)),
    pygame.transform.scale(pygame.image.load("juego/recursos\primer_boss\camina\camina_7.png"),(150,200)),
    pygame.transform.scale(pygame.image.load("juego/recursos\primer_boss\camina\camina_8.png"),(150,200)),
    pygame.transform.scale(pygame.image.load("juego/recursos\primer_boss\camina\camina_8.png"),(150,200))
]

boss_salta_derecha = [
    pygame.transform.scale(pygame.image.load("juego/recursos\primer_boss\salta\salta_1.png"),(150,200)),
    pygame.transform.scale(pygame.image.load("juego/recursos\primer_boss\salta\salta_2.png"),(150,200))
]

boss_ataque_1_derecha = [
    pygame.transform.scale(pygame.image.load("juego/recursos\primer_boss/ataque_1/ataque_1.png"),(150,200)),
    pygame.transform.scale(pygame.image.load("juego/recursos\primer_boss/ataque_1/ataque_2.png"),(150,200)),
    pygame.transform.scale(pygame.image.load("juego/recursos\primer_boss/ataque_1/ataque_3.png"),(150,200)),
    pygame.transform.scale(pygame.image.load("juego/recursos\primer_boss/ataque_1/ataque_4.png"),(150,200)),
    pygame.transform.scale(pygame.image.load("juego/recursos\primer_boss/ataque_1/ataque_5.png"),(150,200)),
    pygame.transform.scale(pygame.image.load("juego/recursos\primer_boss/ataque_1/ataque_6.png"),(150,200)),
    pygame.transform.scale(pygame.image.load("juego/recursos\primer_boss/ataque_1/ataque_7.png"),(150,200)),
    pygame.transform.scale(pygame.image.load("juego/recursos\primer_boss/ataque_1/ataque_8.png"),(150,200))
]


boss_quieto_izquierda = girar_imagen(boss_quieto_derecha,True,False)
boss_camina_izquierda = girar_imagen(boss_camina_derecha,True,False)
boss_salta_izquierda = girar_imagen(boss_salta_derecha,True,False)
boss_ataque_1_izquierda = girar_imagen(boss_ataque_1_derecha,True,False)