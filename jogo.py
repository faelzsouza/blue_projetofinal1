from tempo import Tempo
from personagemPrincipal import PersonagemPrincipal

class Jogo:

    def __init__(self):
        pass
        

    def tarefas(self):
       
        personagem = PersonagemPrincipal("Fernando", "M")
        dia = Tempo()
    
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

        print(personagem.inventario)
        
    
    def fim():
        #condição para validar se o peronagem vencou ou perdeu o jogo

        # finais diferentes de acordo com os itens

        pass
        






    
