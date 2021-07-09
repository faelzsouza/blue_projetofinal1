from tempo import Tempo
from interface import Interface
from personagemPrincipal import PersonagemPrincipal

#Classe de execução do jogo. 
class Jogo:

    personagem = PersonagemPrincipal("L.U.C.A", "M")
    interface = Interface()
    
    def __init__(self):
        pass
        

    def tarefas(self): #função das tarefas que o usuário deve realizar no decorrer do jogo

        self.interface.introducao()

        
        while self.personagem.relogio() < 3: #passagem do tempo do jogo

            
            print("LISTA DE TAREFAS")    
            print()
            print("1 - Buscar alimentos")
            print("2 - Buscar equipamentos")
            print()
            
            resposta = int(input())

            if resposta == 1:
                self.personagem.buscarAlimento()   
            elif resposta == 2:
                self.personagem.buscarEquipamentos()

           
        self.fimDoJogo()    
                
    #Função de monitoramento dos parametros de finalização do jogo. Alimento + Ferramentas + tempo
    def fimDoJogo(self):

        if self.personagem.getAlimento() >= 20 and self.personagem.getEquipamento() >= 20:
            return self.interface.venceu
        elif self.personagem.getAlimento() >= 20 and self.personagem.getEquipamento() < 20:
            return self.interface.perder1()
        elif self.personagem.getAlimento() < 20 and self.personagem.getEquipamento() >= 20:
            return self.interface.perder2()
        else:
            return self.interface.perder3()


    

        
        






    
