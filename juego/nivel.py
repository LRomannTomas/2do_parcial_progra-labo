import pygame
from modo import *
from constantes import *
from funciones import *
from decoraciones import *
from poder_mago import HechizoFuego
from hechizo_multiple import HechizoMultiple
from llave import Llave
from glosario_items import glosario_de_items
import json

class Nivel:
    
    def __init__(self,pantalla,personaje_principal,lados_personaje,lista_enemigos,lista_plataformas,lista_img_estaticas,lista_img_animadas,limites_enemigo,
                lista_disparos,lista_monedas,lista_llaves,lista_escaleras,lista_puertas,nombre_jugador):
            
            
            #jugador-------------------------------------------------------------------|
            self.jugador = personaje_principal
            self.lados_jugador = lados_personaje
            self.nombre_jugador = nombre_jugador
            self.leer_progreso_partida()
          
            
            self.jugador.dinero = self.progreso["dinero"]
            self.jugador.lista_items = self.progreso["items"]
            
            #plataforma e imagenes decorativas-----------------------------------------|
            self.plataformas = lista_plataformas
            self.lista_img_estaticas = lista_img_estaticas
            self.lista_img_animadas = lista_img_animadas            
            
            #estructuras interactivas
            self.lista_escaleras = lista_escaleras
            self.lista_puertas = lista_puertas
            
            #enemigo-------------------------------------------------------------------|
            self.lista_enemigos = lista_enemigos  
            self.limites_enemigo = limites_enemigo
            
            #disparos------------------------------------------------------------------|
            self.lista_disparos = lista_disparos
                        
            #pantalla------------------------------------------------------------------|
            self.pantalla = pantalla
            self.ancho_pantalla = self.pantalla.get_width()
            self.largo_pantalla = self.pantalla.get_height()
            self.limite_pantalla_derecha = self.ancho_pantalla - self.jugador.velocidad_camina - self.lados_jugador["principal"].width
            
            #menu tienda
            self.abrir_tienda = False
            self.tienda = None
            
            #menu niveles
            self.abrir_menu = False
            
            self.mostrar_menu_main = True
            
            
            #recursos
            self.lista_monedas = lista_monedas
            self.lista_llaves = lista_llaves
            
            self.abrir_puerta = False
            
            #pasaje de nivel
            self.supero_nivel = False
            
            #poner las condiciones 
            
            
           #self.menu_pausa = SelectorNiveles(self.pantalla) HACER ESTO6 
    
    
    def leer_progreso_partida(self):
        
        try:
            lista_items = []
            
            with open('data.json') as file:
                data = json.load(file)
                
            
            data = data[self.nombre_jugador]
            
                
            for item_str in data["items"]:
                if item_str != "llave":
                    nuevo_item = glosario_de_items[item_str]()
                
                    lista_items.append(nuevo_item)
                    
                
            data["items"] = lista_items
            
        except:
            data = {
                "ultimo_nivel_ganado": 0,
                "dinero" : 0,
                "items": []
                }
                
        self.progreso = data
               
    
    def guardar_progreso_partida(self):
        lista = []
        for item in self.jugador.lista_items:
            lista.append(item.nombre)
        
        
        self.progreso["dinero"] = self.jugador.dinero
        self.progreso["items"] = lista
        
        try:
            with open('data.json') as file:
                data = json.load(file)
        except:
            data = {}
        
        data[self.nombre_jugador] = self.progreso
       
            
        with open('data.json', 'w') as file:
            json.dump(data, file, indent=4, ensure_ascii=False )

                
                
    def dibujar_texto(self,texto,fuente,color,x,y):
        imagen = fuente.render(texto,True,color)
        self.pantalla.blit(imagen,(x,y))
    
    
    def cerrar_menu(self,cerrar_menu):
        if cerrar_menu:
            self.abrir_menu = False
        
        
    def update(self,lista_eventos):
        
        for evento in lista_eventos:        
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_TAB:
                    cambiar_modo()
                    
                
                if evento.key == pygame.K_b:
                    if self.tienda != None and self.jugador.rectangulo_personaje.colliderect(self.tienda.rectangulo_imagen):
                        self.abrir_tienda = True
                
                if evento.key == pygame.K_1:
                    if len(self.jugador.lista_items) > 0:
                        if type(self.jugador.lista_items[0]) != Llave:
                            self.jugador.lista_items[0].aplicar(self.jugador)
                            self.jugador.lista_items.pop(0)
                            
                        elif self.jugador.toco_puerta:
                            self.jugador.lista_items[0].aplicar(self.jugador)
                            self.abrir_puerta = True
                            self.jugador.lista_items.pop(0)

                
                if evento.key == pygame.K_ESCAPE:
                    self.abrir_menu = True
                    self.guardar_progreso_partida()
    
            
        else:
            self.leer_inputs()
            self.actualizar_pantalla()
            self.dibujar_rectangulos()
    
    
    def leer_inputs(self):
        teclas = pygame.key.get_pressed()
    
    
        if teclas[pygame.K_UP] and self.jugador.esta_saltando == False and not self.jugador.toco_escalera:
            self.jugador.estado = "salta"

        elif teclas[pygame.K_UP] and self.jugador.toco_escalera:
            self.jugador.estado = "sube escalera"
                    
        elif teclas[pygame.K_r]:
            self.jugador.atacar(self.lista_enemigos)
            
            
        elif teclas[pygame.K_RIGHT] and self.lados_jugador["principal"].x < self.limite_pantalla_derecha :
            self.jugador.estado = "derecha"
                
        elif teclas[pygame.K_LEFT] and (self.lados_jugador["principal"].x > self.jugador.velocidad_camina):
            self.jugador.estado = "izquierda"
        
        else:
            self.jugador.estado = "quieto"
    
    
    def verificar_kill_moneda(self):
        indice = 0
        while indice < len(self.lista_monedas):
            moneda = self.lista_monedas[indice]
            if not moneda.mostrar:
                self.lista_monedas.pop(indice)
                indice -= 1
                
            indice += 1
            
            
    def verificar_kill_llave(self):
        indice = 0
        while indice < len(self.lista_llaves):
            llave = self.lista_llaves[indice]

            if not llave.mostrar:
                
                self.lista_llaves.pop(indice)
                indice -= 1
            
                
            indice += 1
    
    
    def verificar_kill_poder(self):        
        indice = 0
    
        while indice < len(self.lista_disparos):
            disparo = self.lista_disparos[indice]
            if type(disparo) == HechizoFuego or  type(disparo) == HechizoMultiple:
                disparo.update(self.pantalla,self.plataformas)
            else:
                disparo.update(self.pantalla)
                
            if disparo.kill:
                self.lista_disparos.pop(indice)
                indice -= 1
                
            indice += 1
    
    
    def verificar_kill_enemigo(self):
        indice = 0
        while indice < len(self.lista_enemigos):
            enemigo = self.lista_enemigos[indice]
            
            if enemigo.kill:
                if enemigo.eliminar_enemigos:
                    self.lista_enemigos = []
                else:   
                    self.lista_enemigos.pop(indice)
                    indice -= 1
                
            indice += 1


    def mostrar_items(self):
        x = 250 
        for item in self.jugador.lista_items: 
            imagen = pygame.transform.scale(item.imagen,(35,35))
            self.pantalla.blit(imagen,(x,30))
            x += imagen.get_width() + 2
            
            
            
    def mostrar_dinero(self):
        fuente = pygame.font.SysFont("8bitoperator8",30)
        moneda = pygame.transform.scale(pygame.image.load("juego/recursos\monedas\moneda_1.png"),(20,20))
        texto = fuente.render(f"{self.jugador.dinero}",True,COLOR_BLANCO)
        self.pantalla.blit(moneda,(20,20))
        self.pantalla.blit(texto,(45,20))
        
    
    
    def actualizar_pantalla(self):
        
       
        mostrar_imagenes(self.pantalla,self.lista_img_estaticas)
        mostrar_imagenes(self.pantalla,self.lista_escaleras)
        
        
        self.mostrar_dinero()
        
        self.mostrar_items()
        
        self.verificar_kill_moneda()
        self.verificar_kill_poder()
        self.verificar_kill_enemigo()
        self.verificar_kill_llave()
        
        
        for llave_recolectable in self.lista_llaves:
            llave_recolectable.update(self.jugador,self.pantalla)
        
        for moneda in self.lista_monedas:
            moneda.update()
            
        for imagen in self.lista_img_animadas:
            imagen.update()
        
        for enemigo in self.lista_enemigos:
            enemigo.update(self.pantalla,self.limites_enemigo,enemigo.lados_enemigo,self.lista_disparos,self.plataformas,self.jugador.rectangulo_personaje) 
            
            if enemigo.invocacion != None and not enemigo.kill:
                self.lista_enemigos.append(enemigo.invocacion)
                enemigo.invocacion = None
            
        
        for puerta in self.lista_puertas:   
            if self.abrir_puerta:
                puerta_cerrada = self.lista_puertas[1]
                self.pantalla.blit(puerta_cerrada.imagen,(puerta_cerrada.rectangulo_imagen.x,puerta_cerrada.rectangulo_imagen.y))
            else:
                puerta_abierta = self.lista_puertas[0]
                self.pantalla.blit(puerta_abierta.imagen,(puerta_abierta.rectangulo_imagen.x,puerta_abierta.rectangulo_imagen.y))
        
        
        self.jugador.update(self.pantalla,self.lados_jugador,self.lista_disparos,self.plataformas,self.lista_enemigos,self.lista_monedas,
                            self.lista_llaves,self.lista_escaleras,self.lista_puertas)
        
        
        if self.tienda != None and self.jugador.rectangulo_personaje.colliderect(self.tienda.rectangulo_imagen):
            self.pantalla.blit(pygame.transform.scale(pygame.image.load("juego/recursos/botones/texto_interactuar_tienda.png"),(300,60)),(550,20))
            
            
        
    def dibujar_rectangulos(self):
        if obtener_modo():  

            for lado in self.lados_jugador:
                pygame.draw.rect(self.pantalla,COLOR_ROJO,self.lados_jugador[lado],2)
                
                
            for plataforma in self.plataformas:
                pygame.draw.rect(self.pantalla,COLOR_ROJO,plataforma.lados_plataforma[lado],2)

                
            for enemigo in self.lista_enemigos:
                for lado in enemigo.lados_enemigo:
                    pygame.draw.rect(self.pantalla,COLOR_ROJO,enemigo.lados_enemigo[lado],2)
            
            for disparo in self.lista_disparos:
                pygame.draw.rect(self.pantalla,COLOR_ROJO,disparo.rectangulo_poder,2)
                
           
            for limite in self.limites_enemigo:
                for lado in limite.lados_plataforma:
                    pygame.draw.rect(self.pantalla,COLOR_ROJO,limite.lados_plataforma[lado],2)
                
                    
            
           
            
            
            