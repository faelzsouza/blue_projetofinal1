from tempo import Tempo
from interface import Interface
from personagemPrincipal import PersonagemPrincipal

class Jogo:

    personagem = PersonagemPrincipal("L.U.C.A", "M")
    interface = Interface()
    
    def __init__(self):
        pass
        

    def tarefas(self):

        self.interface.introducao()

        
        while self.personagem.relogio() < 3:

            
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
                

    def fimDoJogo(self):

        if self.personagem.inventario ["Alimento"] >= 20 and self.personagem.inventario ["Equipamento"] >= 20:
            return self.interface.venceu
        elif self.personagem.inventario ["Alimento"] >= 20 and self.personagem.inventario ["Equipamento"] < 20:
            return self.interface.perder1()
        elif self.personagem.inventario ["Alimento"] < 20 and self.personagem.inventario ["Equipamento"] >= 20:
            return self.interface.perder2()
        else:
            return self.interface.perder3()


    

        
        






    
