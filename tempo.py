class Tempo:
    
    def __init__(self):
        self.dia = 1
        self.hora = 8
        
    def passarHora(self, valor):
        self.hora += valor
        return self.hora

    def avancarDia(self):
        self.dia += 1 


       
        

