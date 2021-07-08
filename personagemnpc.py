from personagem import Personagem
import random

class npc(Personagem):
    def __init__(self, nome, sexo, funcao = "npc"):
        super().__init__(nome, sexo)
        self.funcao = funcao

    def abrirEstoque(self):

            print (f"Parece que Hebe tem um estoque de comida guardado! Quando você clica na fechadura eletrônica a seguinte mensagem aparece:\n 'Olá gracinha! para abrir o estoque responda a charada:\nMeu avô tem 5 filhos, cada filho tem 3 filhos. Quantos primos eu tenho?\nQue velha doida, né?\n")
            
            resp = int(input("De qualquer forma digite a resposta para abrir o cofre: "))
            if resp == (12):
                print
                print("Deu certo!")
                self.inventario ["Alimento"] += 50
                return
            else:
                print("A senha está errada e o alarme disparou! É melhor você correr pra casa!")
        
       
    def eventoestoque(self):

        sorteio = random.randint(0, 99)

        if sorteio < 40:
            self.abrirEstoque()

    def eventoCofre(self):

        lista = list(range(20))
        sorteio = random.randint(0, 99)

        if sorteio in lista:
            self.abrirCofre()


    def abrirCofre(self):

        print ("Vc achou um cofre..... ")

        for i in range(5):

            senha = 1234
            chute = input("Digite a senha: ")

            if senha == chute:
                self.inventario ["Equipamento"] += 50
                return
        
        print("Vc não conseguiu abrir o cofre... tururu! ")

    # vizinha = npc("Hebe Camargo", "Feminino", "vizinha")

    # dono = npc("Xaropinho", "Masculino", "Dono do Ferro Velho")

    # conjunge = npc("Eva", "Feminino", "Parceira de Cópula")
 
