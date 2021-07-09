class Tempo:

    def __init__(self):  #Controle de tempo fictício 1 - dias e 2 - horas.
        self.dia = 1
        self.hora = 8
        

    def getDia(self): #encapsulamento dos atributos
        return self.dia

    def getHora(self): #encapsulamento dos atributos
        return self.hora    


    def passarHora(self, valor): #Função de progresso da hora
        self.hora += valor
        h = self.hora - 24
        if self.hora >= 24:
            self.hora = h
            self.avancarDia()
            
        return self.hora


    def avancarDia(self): #Função de progresso do dia
        self.dia += 1 

    
       
       
        

