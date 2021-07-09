# Classe de diálogos com o usuário, introduzindo o enredo do game, do personagem principal e com algumas saídas de diálogo.
class Interface:

        def introducao(self):
                print("Bem vindo a Nibiru; Uma corrida pela vida")

                print(f"Olá, que bom que você chegou, realmente precisamos de ajuda! Nibiru já foi um planeta desenvolvido e bem organizado, mas houve um acidente na usina nuclear da província de Namu que lançou material radioativo na atmosfera, desde então a radiação já cobriu 70 por cento do planeta, e, segundo as previsões, em até 5 dias essas toxinas chegarão até aqui!\n")

                #Luca acrônimo de Last Universal Common Ancestor
                print("Felizmente, nosso herói L.U.C.A, conseguiu fazer os cálculos para uma viagem para um planeta azul na Via Láctea. Mas para finalizar o projeto ele precisa de ferramentas para a manutenção de sua nave, além de um estoque de comida para os dias que ficará no espaço! Você está pronto para ajudá-lo nesta jornada interestelar? \U0001F680")

                print()
                print("Enter para continuar.")

        def instrucoes (self): #Instruções para o usuário
                print("Para auxiliá-lo nessa jornada você vai precisar buscar alimentos e equipamentos o suficiente para a longa viagem no sistema solar. Mas fique atento, pois todas as suas ações gastam sua stamina, e você pode recuperá-la dormindo ou comendo, caso zere sua stamina você pode desmaiar de sono! Não esqueça, essa é uma corrida contra o tempo.")
                print()        
                print("Enter para continuar.")

        #Funções de retorno ao usuários das finalizações do jogo:
        def venceu(self):
                print("Wow! Deu certo, apesar de todas as dificuldades, você foi capaz de fugir do planeta a tempo, em pouco tempo você estará entrando na atmosfera do planeta azul! Se prepare para a colisão!")

        def perder1(self):
                print("Puxa! Você conseguiu decolar, porém devido a salta de equipamento sua nave não teve impulso suficiente para chegar na atmosfera do planeta azul e agora está vagando no espaço.")

        def perder2(self):
                print("Puxa! Você conseguiu decolar, porém não levou alimento suficiente para a longa viagem... A nave vai chegar lá, mas você não...")

        def perder3(self):
                print("Ah não! Infelizmente você não conseguiu montar a nave a tempo, a radioatividade tomou o planeta inteiro!")      

                        

















       


            