from tempo import Tempo
from personagemPrincipal import PersonagemPrincipal

class Jogo:

    personagem = PersonagemPrincipal("L.U.C.A", "M")
    tempo = Tempo()

    def __init__(self):
        pass
        

    def tarefas(self):

        continuar = True
        while continuar:
    
            print("LISTA DE TAREFAS")    
            print()
            print("1 - Buscar alimentos")
            print("2 - Buscar equipamentos")
            print()
            
            resposta = int(input())


            if resposta == 1:
                self.personagem.buscarAlimento()
                
            elif resposta == 2 :
                self.personagem.buscarEquipamentos()

            
            c = self.tempo.fimDoTempo()
            continuar = c


    def encerramento(self):

        print("fim de jogo")     

        
        






    
