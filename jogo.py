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
        input()
        print()
        print("\033c")
        self.interface.instrucoes()
        input()
        print()
        print("\033c")
        
        while self.personagem.relogio() < 3: #passagem do tempo do jogo

            while True:
                print("\033c")
                print()
                print(f"{'LISTA DE TAREFAS':^23}")    
                print()
                print("1 - Buscar alimentos")
                print("2 - Buscar equipamentos")
                print()
                try:
                    resposta = int(input())
                    if resposta > 2 or resposta < 1:
                        print('\nOpção inválida!\n')
                    else:
                        break
                except:
                    print('\nDigite apenas números!\n')

            if resposta == 1:
                self.personagem.buscarAlimento()   
            elif resposta == 2:
                self.personagem.buscarEquipamentos()

        print("\033c")   
        print()
        self.fimDoJogo()    
                
    #Função de monitoramento dos parametros de finalização do jogo. Alimento + Ferramentas + tempo
    def fimDoJogo(self):

        if self.personagem.getAlimento() >= 20 and self.personagem.getEquipamento() >= 20:
            return self.interface.venceu()
        elif self.personagem.getAlimento() >= 20 and self.personagem.getEquipamento() < 20:
            return self.interface.perder1()
        elif self.personagem.getAlimento() < 20 and self.personagem.getEquipamento() >= 20:
            return self.interface.perder2()
        else:
            return self.interface.perder3()


    

        
        






    
