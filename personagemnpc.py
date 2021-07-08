from personagem import Personagem
import random
import personagemPrincipal

class Npc(Personagem):
    def __init__(self, nome, sexo, funcao = "npc"):
        super().__init__(nome, sexo)
        self.funcao = funcao
    
    def abrirEstoque(self):

            print (f"Parece que Hebe tem um estoque de comida guardado! Quando você clica na fechadura eletrônica a seguinte mensagem aparece:\n 'Olá gracinha! para abrir o estoque responda a charada:\nMeu avô tem 5 filhos, cada filho tem 3 filhos. Quantos primos eu tenho?\nQue velha doida, né?\n")
            
            resp = int(input("De qualquer forma digite a resposta para abrir o cofre: "))
            if resp == (12):
                print
                print("Deu certo!")
                return 50
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
        print ("Que sorte! No meio das pilhas de ferramentas você encontrou um cofre! Provavelmente é do dono Xaropinho\nEmbaixo do cofre está um papel escrito:\n'rapaiz... senha: 2683'\n(claramente, ele não entende muito de segurança, não é mesmo?) Mas parece que os ratos roeram o quinto número do papel. Vale a pena chutar alguns números para abrir o cofre!")

        for i in range(5):

            senha = 1234
            chute = input("Digite a senha: ")

            if senha == chute:
                return 50
        
        print("Vc não conseguiu abrir o cofre... tururu! ")

    # vizinha = npc("Hebe Camargo", "Feminino", "vizinha")

    # dono = npc("Xaropinho", "Masculino", "Dono do Ferro Velho")

    # conjunge = npc("Eva", "Feminino", "Parceira de Cópula")
 
