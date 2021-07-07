import personagem

class npc(personagem):
    def __init__(self, nome, sexo, funcao):
        super().__init__(nome, sexo)
        self.funcao = funcao

vizinha = npc.vizinha("Hebe Camargo", "Feminino", "Vizinha")

dono = npc.ferrovelho("Xaropinho", "Masculino", "Dono do Ferro Velho")

conjunge = npc.conjuge("Eva", "Feminino", "Parceira de Cópula")

 
