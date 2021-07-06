from personagem import Personagem
from tempo import Tempo
import random

class PersonagemPrincipal(Personagem):

    # metodo trabalho
    
    tempo = Tempo()

    def __init__(self, nome, sexo):
        super().__init__(nome, sexo)
        self.stamina = 10
        self.inventario = {"Alimento":0, "Equipamento":0}


    def buscarAlimento(self):

        print("Digite 1 para ir caçar")
        print("Digite 2 para pedir comida da rua")
        print("Digite 3 para rouar do vizinho")

        resposta = int(input())
        
        # gasto de stamina de acordo com a escolha da ação
        if resposta == 1:
            self.stamina -= 3
            self.tempo.passarHora(1)
        elif resposta == 2:
            self.stamina -= 1
            self.tempo.passarHora(1)
        elif resposta == 3:
            self.stamina -= 2     
            self.tempo.passarHora(1)


        sorteio = random.randint(1,3)

        # quantidade de alimento de acordo com o sorteio
        if sorteio == 1:
            a = 7
        elif sorteio == 2:
            a = 2
        elif sorteio == 3:
            a = 4        

        if resposta == sorteio:
            self.inventario ["Alimento"] += a


    def buscarEquipamentos(self):
        
        print("Digite 1 para buscar no ferro velho")
        print("Digite 2 para fabricar peças")
        print("Digite 3 para roubar peças")

        resposta = int(input())
        
        # gasto de stamina de acordo com a escolha da ação
        if resposta == 1:
            self.stamina -= 2
            self.tempo.passarHora(1)
        elif resposta == 2:
            self.stamina -= 5
            self.tempo.passarHora(1)
        elif resposta == 3:
            self.stamina -= 3  
            self.tempo.passarHora(1)

        sorteio = random.randint(1,3)

        # quantidade de equipamento de acordo com o sorteio
        if sorteio == 1:
            e = 2
        elif sorteio == 2:
            e = 7
        elif sorteio == 3:
            e = 4        

        if resposta == sorteio:
            self.inventario ["Equipamento"] += e 

        
    def dormir(self):

        



        pass

        