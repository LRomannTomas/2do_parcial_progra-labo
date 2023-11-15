import pygame
from constantes import *
from jugador import Personaje



pygame.init()
# ocultar_mouse = pygame.mouse.set_visible(False)   --> OCULTAR EL CURSOR

pantalla = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))

imagen_fondo = pygame.image.load("imagenes/assets_1/background/background_layer_1.png")
imagen_fondo = pygame.transform.scale(imagen_fondo,(ANCHO_VENTANA,ALTO_VENTANA))

pygame.display.set_caption("Juego")


#player
jugador_1 = Personaje(0,0,15,15,8)


mira_izquierda = True


flag_correr = True

flag_pj_2_vivo = True

#timer
tiempo_segundos = pygame.USEREVENT
pygame.time.set_timer(tiempo_segundos,100)  # --> esto indica cada cuanto quiero que ocurra el primer parametro, es decir, la variable tiempo_segundos se va leer 1 vez por segundo



#clock
clock = pygame.time.Clock()

while flag_correr:
    pantalla.blit(imagen_fondo,imagen_fondo.get_rect())
    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            flag_correr = False
            
        if evento.type == pygame.USEREVENT:         #esto es por si tengo mas de un timer, para que no me lea todos los demas timer (si es que hay) si no es de tipo userevent.
            if evento.type == tiempo_segundos:
                flag_pj_2_vivo = True
                jugador_1.update()
        
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_RIGHT:
                mira_izquierda = False
                jugador_1.control("caminar_derecha")
                
                
            elif evento.key == pygame.K_LEFT:
                mira_izquierda = True
                jugador_1.control("caminar_izquierda")
                
            
            elif evento.key == pygame.K_UP:
                if mira_izquierda == False:
                    jugador_1.control("saltar_derecha")
                else:
                    jugador_1.control("saltar_izquierda")
            
            
                
                
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_RIGHT or evento.key == pygame.K_LEFT or evento.key == pygame.K_UP:
                if mira_izquierda == False:
                    jugador_1.control("quieto_derecha")
                else:
                    jugador_1.control("quieto_izquierda")
                    
                
            # if evento.key == pygame.K_LEFT or :
                
            #     jugador_1.control("quieto_izquierda")
                
            # if evento.key == pygame.K_UP:
            #     if mira_izquierda == False:
            #         jugador_1.control("quieto_derecha")
            #     else:
            #         jugador_1.control("quieto_derecha")
                
    jugador_1.dibujar(pantalla)
    clock.tick(FPS)
    
    
    
    # lista_teclas = pygame.key.get_pressed()
    
    # if True in lista_teclas:
        
    #     if evento.type == pygame.KEYDOWN:
    #         if lista_teclas[pygame.K_RIGHT]:
    #             jugador_1.control("caminar_derecha",10,0)
    #         elif lista_teclas[pygame.K_LEFT]:
    #             jugador_1.control("caminar_izquierda",-10,0)
    #         elif lista_teclas[pygame.K_UP]:
    #             jugador_1.control("saltar",0,-10)
    #     if evento.type == pygame.KEYUP:
    #         if lista_teclas == [pygame.K_RIGHT] or lista_teclas == [pygame.K_UP]:
    #             jugador_1.control("quieto_derecha",0,0)
    #         if lista_teclas == [pygame.K_LEFT]:
    #             jugador_1.control("quieto_izquierda",0,0)

        
        

    pygame.display.flip()
    
    

pygame.quit()