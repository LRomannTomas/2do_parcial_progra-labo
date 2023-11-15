import pygame
from constantes import *


def obtener_surface_de_sprite(path,columnas,filas,voltear=False):
    lista = []
    lista_quieto_derecha = []
    lista_quieto_izquierda = []
    lista_caminar_derecha = []
    lista_caminar_izquierda = []
    lista_saltar_derecha = []
    lista_saltar_izquierda = []
    lista_caida_derecha = []
    lista_caida_izquierda = []
    
    superficie_imagen = pygame.image.load(path)
    superficie_imagen = pygame.transform.scale(superficie_imagen,(1000,1200))
    
    fotograma_ancho =  int(superficie_imagen.get_width() / columnas)
    fotograma_alto =  superficie_imagen.get_height() / filas + 0.5     #le agrego 0.5 porque si no, se ven los pies arriba randomly
    
    for fila in range(filas):
        for columna in range(columnas):
            x = columna * fotograma_ancho
            y = fila * fotograma_alto
            if fila == 0 and columna < 6:
                superficie_fotograma = superficie_imagen.subsurface(x,y,fotograma_ancho,fotograma_alto)
                lista_quieto_derecha.append(superficie_fotograma)
                
                superficie_fotograma_invertida = pygame.transform.flip(superficie_fotograma,True,False)
                lista_quieto_izquierda.append(superficie_fotograma_invertida)
                
            elif fila == 2:
                superficie_fotograma = superficie_imagen.subsurface(x,y,fotograma_ancho,fotograma_alto)
                lista_caminar_derecha.append(superficie_fotograma)
                
                superficie_fotograma_invertida = pygame.transform.flip(superficie_fotograma,True,False)
                lista_caminar_izquierda.append(superficie_fotograma_invertida)
            
            elif fila == 3 :
                superficie_fotograma = superficie_imagen.subsurface(x,y,fotograma_ancho,fotograma_alto)
                lista_saltar_derecha.append(superficie_fotograma)
                
                superficie_fotograma_invertida = pygame.transform.flip(superficie_fotograma,True,False)
                lista_saltar_izquierda.append(superficie_fotograma_invertida)
                
            elif fila == 4:
                superficie_fotograma = superficie_imagen.subsurface(x,y,fotograma_ancho,fotograma_alto)
                lista_caida_derecha.append(superficie_fotograma)
                
                superficie_fotograma_invertida = pygame.transform.flip(superficie_fotograma,True,False)
                lista_caida_izquierda.append(superficie_fotograma_invertida)
                

    lista.append({"quieto_derecha":lista_quieto_derecha})
    lista.append({"quieto_izquierda":lista_quieto_izquierda})
    lista.append({"caminar_derecha":lista_caminar_derecha})
    lista.append({"caminar_izquierda":lista_caminar_izquierda})
    lista.append({"saltar_derecha":lista_saltar_derecha})
    lista.append({"saltar_izquierda":lista_saltar_izquierda})
    lista.append({"caida_derecha":lista_caida_derecha})
    lista.append({"caida_izquierda":lista_caida_izquierda})
    
                
    #print(x,y,fotograma_ancho,fotograma_alto)
    
    return lista


class Personaje:
    def __init__(self,x,y,velocidad_camina,salto,gravedad):
        self.accion = obtener_surface_de_sprite("imagenes/assets_2/png/green/char_green_1.png",8,11)
        self.frame = 0
        self.estado = "quieto_derecha"
        self.animacion = self.accion
        self.gravedad = gravedad
        self.salto = salto
        self.esta_saltando = False
        self.velocidad_caminata = velocidad_camina
        #self.estado_anterior = self.estado
        self.imagen = self.animacion[0][self.estado][self.frame]
        self.rect = self.imagen.get_rect()
        self.rect.x = 50
        self.rect.y = 400
        self.mover_x = x
        self.mover_y = y
    
    
    def update(self):
        
        if self.estado == "quieto_derecha":
            
            if self.frame < len(self.animacion[0][self.estado]) - 1:
                self.frame += 1
            else:
                self.frame = 0
                if self.esta_saltando == True:
                    self.esta_saltando = False
                    self.mover_y = 0
                
        elif self.estado == "quieto_izquierda":
            
            if self.frame < len(self.animacion[1][self.estado]) - 1:
                self.frame += 1
            else:
                self.frame = 0
                if self.esta_saltando == True:
                    self.esta_saltando = False
                    self.mover_y = 0
                
        elif self.estado == "caminar_derecha":       
            if self.frame < len(self.animacion[2][self.estado]) - 1:
                self.frame += 1
            else:
                self.frame = 0
                if self.esta_saltando == True:
                    self.esta_saltando = False
                    self.mover_y = 0
                
        elif self.estado == "caminar_izquierda":
            if self.frame < len(self.animacion[3][self.estado]) - 1:
                self.frame += 1
            else:
                self.frame = 0
                if self.esta_saltando == True:
                    self.esta_saltando = False
                    self.mover_y = 0
                
        elif self.estado == "saltar_derecha":
            if self.frame < len(self.animacion[4][self.estado]) - 1:
                self.frame += 1
            else:
                self.frame = 0
                if self.esta_saltando == True:
                    self.esta_saltando = False
                    self.mover_y = 0
                    
        elif self.estado == "saltar_izquierda":
            if self.frame < len(self.animacion[5][self.estado]) - 1:
                self.frame += 1
            else:
                self.frame = 0
                if self.esta_saltando == True:
                    self.esta_saltando = False
                    self.mover_y = 0
                
       
        
        # elif self.estado == "saltar_derecha":
        #     self.esta_saltando = True
        #     if self.frame < len(self.animacion[4][self.estado]) - 1:
        #         self.frame += 1
        #     else:
        #         self.frame = 0
        #         if self.esta_saltando == True:
        #             self.mover_y = 0
        #             self.estado = "caida_derecha"
        
        # elif self.estado == "saltar_izquierda" :
        #     self.esta_saltando = True
        #     if self.frame < len(self.animacion[5][self.estado]) - 1:
        #         self.frame += 1
        #     else:
        #         self.frame = 0
        #         if self.esta_saltando == True:        
        #             self.mover_y = 0
        #             self.estado = "caida_izquierda"
                    
        # elif self.estado == "caida_derecha":
        #     if self.frame < len(self.animacion[6][self.estado]) - 1:
        #         self.frame += 1
        #     else:
        #         self.estado = "quieto_derecha"
        #         self.frame = 0
                
        # elif self.estado == "caida_izquierda":
        #     if self.frame < len(self.animacion[7][self.estado]) - 1:
        #         self.frame += 1
        #     else:
        #         self.estado = "quieto_izquierda"
        #         self.frame = 0
        
        if self.rect.y < 400:
            self.rect.y += self.gravedad
        
        
        self.rect.x += self.mover_x
        self.rect.y += self.mover_y
        
        
    def control(self,accion:str):
        
        
        if accion == "caminar_derecha":
            
            self.mover_x = self.velocidad_caminata 
            self.estado = accion
            
            self.animacion = self.accion
            self.frame = 0
            
        elif accion == "caminar_izquierda":
            
            self.mover_x = -self.velocidad_caminata 
            self.estado = accion
            
            self.animacion = self.accion
            self.frame = 0
        
        elif accion == "quieto_derecha":
            self.mover_x = 0
            self.mover_y = 0
           
            self.estado = accion
            
            self.animacion = self.accion
            self.frame = 0
            self.esta_saltando = False
        
        elif accion == "quieto_izquierda":
            self.mover_x = 0
            self.mover_y = 0
            
            self.estado = accion
            
            self.animacion = self.accion
            self.frame = 0
            self.esta_saltando = False
            
        elif accion == "saltar_derecha":
            
            self.mover_y = -self.salto
            
            self.animacion = self.accion
            
            self.estado = accion
            self.frame = 0
            self.esta_saltando = True 
            
            
        elif accion == "saltar_izquierda":
            
            self.mover_y = -self.salto
            self.animacion = self.accion
            
            self.estado = accion
            
            self.frame = 0
            self.esta_saltando = True
            
                
        # if accion == "saltar_derecha" or accion == "saltar_izquierda":
        #     if self.esta_saltando == False:  
                    
        #         self.mover_y = self.velocidad_caminata 

        #         self.estado = accion
                
        #         self.animacion = self.accion
        #         self.frame = 0
                
    
    def dibujar(self,screen):
        if self.estado == "quieto_derecha":
            self.imagen =  self.animacion[0][self.estado][self.frame]
            screen.blit(self.imagen,self.rect)
            
        elif self.estado == "quieto_izquierda":
            self.imagen =  self.animacion[1][self.estado][self.frame]
            screen.blit(self.imagen,self.rect)
            
        elif self.estado == "caminar_derecha":
            self.imagen = self.animacion[2][self.estado][self.frame]
            screen.blit(self.imagen,self.rect)
            
        elif self.estado == "caminar_izquierda":
            self.imagen = self.animacion[3][self.estado][self.frame]
            screen.blit(self.imagen,self.rect)
        
        elif self.estado == "saltar_derecha":
            self.imagen = self.animacion[4][self.estado][self.frame]
            screen.blit(self.imagen,self.rect)
            
        elif self.estado == "saltar_izquierda":
            self.imagen = self.animacion[5][self.estado][self.frame]
            screen.blit(self.imagen,self.rect)
        
        elif self.estado == "caida_derecha":
            self.imagen = self.animacion[6][self.estado][self.frame]
            screen.blit(self.imagen,self.rect)
            
        elif self.estado == "caida_izquierda":
            self.imagen = self.animacion[7][self.estado][self.frame]
            screen.blit(self.imagen,self.rect)
            