

class Menu:
    def __init__(self,lista_widgets,pantalla) -> None:    
        self.lista_widgets = lista_widgets
        self.dialogo = ""
        self.pantalla = pantalla
        self.formulario_hijo = None
        
        
    def set_dialogo(self,dialogo):
        self.dialogo = dialogo
        
        
    def leer_dialogo(self):   #metodo abstracto
        
        dialogo = self.get_dialogo()
        
        if dialogo == "volver":
            self.eliminar_hijo()
    
    
    def set_hijo(self,hijo):
        self.formulario_hijo = hijo
        
        
    def eliminar_hijo(self):
        self.formulario_hijo = None
        
        
    def get_dialogo(self):
        return self.formulario_hijo.dialogo
        
        
    def update(self,lista_eventos):
        if self.formulario_hijo == None:
            for widget in self.lista_widgets:
                widget.update(self.pantalla,lista_eventos)
        else:
            self.formulario_hijo.update(lista_eventos)
            self.leer_dialogo()
    


        
        
    
        