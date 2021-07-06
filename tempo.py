class Tempo:
    
    def __init__(self):
        self.dia = 1
        self.hora = 8
        
    def passarHora(self, valor):
        self.hora += valor
        if self.hora == 24:
            self.hora = 0

        return self.hora

    def avancarDia(self):
        self.dia += 1 


       
        

