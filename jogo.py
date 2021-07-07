from tempo import Tempo
from personagemPrincipal import PersonagemPrincipal

class Jogo:

    def __init__(self):
        pass
        

    def tarefas(self):
       
        personagem = PersonagemPrincipal("Fernando", "M")
        dia = Tempo()

        continuar = True
        while continuar:
    
            print("LISTA DE TAREFAS")    
            print()
            print("1 - Buscar alimentos")
            print("2 - Buscar equipamentos")
            
            resposta = int(input())


            if resposta == 1:
                dia.avancarDia()
                personagem.buscarAlimento()
                
            elif resposta == 2 :
                dia.avancarDia()
                personagem.buscarEquipamentos()
            
            
            

            

            # print("Deseja continuar? S/N") 
            # resp = input()
            # if resp == 's':
            #     continuar = True
            # else:
            #     continuar = False 
        
    
    def fim(self):
        #condição para validar se o peronagem vencou ou perdeu o jogo

        # finais diferentes de acordo com os itens

        pass
        






    
