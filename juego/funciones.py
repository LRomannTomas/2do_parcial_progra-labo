
import pygame


def girar_imagen(lista_animaciones,flip_x,flip_y):
    lista_animaciones_invertidas = []
    for imagen in lista_animaciones:
        lista_animaciones_invertidas.append(pygame.transform.flip(imagen,flip_x,flip_y))
    
    return lista_animaciones_invertidas

def mostrar_imagenes(pantalla,lista_imagenes):
    
    for imagen in lista_imagenes:
        pantalla.blit(imagen.imagen,(imagen.rectangulo_imagen.x,imagen.rectangulo_imagen.y))
                  
        
def obtener_rectangulos(principal):
    diccionario = {}
    #main - bottom - lef - top - right
    diccionario["principal"] = principal
    diccionario["abajo"] = pygame.Rect(principal.left,principal.bottom - 15 ,principal.width, 15)
    diccionario["derecha"] = pygame.Rect(principal.right - 10,principal.top ,10, principal.height)
    diccionario["izquierda"] = pygame.Rect(principal.left, principal.top, 10,principal.height)   
    diccionario["arriba"] = pygame.Rect(principal.left, principal.top, principal.width ,15)
    
    return diccionario


    
