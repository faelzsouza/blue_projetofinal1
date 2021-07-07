from personagem import Personagem

class npc(Personagem):
    def __init__(self, nome, sexo, funcao = "npc"):
        super().__init__(nome, sexo)
        self.funcao = funcao

vizinha = npc("Hebe Camargo", "Feminino", "vizinha")

dono = npc("Xaropinho", "Masculino", "Dono do Ferro Velho")

conjunge = npc("Eva", "Feminino", "Parceira de Cópula")
 
