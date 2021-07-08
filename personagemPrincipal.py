from personagem import Personagem
from tempo import Tempo
import random


# from personagemnpc import npc

class PersonagemPrincipal(Personagem):
    
    tempo = Tempo()

    def __init__(self, nome, sexo):
        super().__init__(nome, sexo)
        self.stamina = 10
        self.inventario = {"Alimento":0, "Equipamento":0}    

    def getAlimento(self):
        return self.inventario  ["Alimento"]  

    def getEquipamento(self):
        return self.inventario ["Equipamento"]    
    

    def buscarAlimento(self):

        continuar = True
        while continuar == True and self.tempo.getDia() < 3:    

            self.info()

            print("Digite 1 para ir caçar")
            print("Digite 2 para pedir comida da rua")
            print("Digite 3 para roubar do vizinho")

            try:
                resposta = int(input())
            except:
                print("Opção invalida")
                self.buscarAlimento()

            # gasto de stamina de acordo com a escolha da ação
            if resposta == 1 and self.stamina >= 3:
                self.stamina -= 3
                self.tempo.passarHora(9)
                if self.tempo.getDia() >= 3:
                    return 
            elif resposta == 2 and self.stamina >= 1:
                self.stamina -= 1
                self.tempo.passarHora(9)
                if self.tempo.getDia() >= 3:
                    return 
            elif resposta == 3 and self.stamina >= 3:
                self.stamina -= 2     
                self.tempo.passarHora(9)
                if self.tempo.getDia() >= 3:
                    return 
            else:

                resposta = 0
                
                print("Opa! Parece que você não tem stamina para concluir essa tarefa")
                if self.inventario ["Alimento"] > 0:             
                    
                    print(f"Vc tem {self.inventario ['Alimento']} alimento. Deseja comer? S/N")
                    resp = input()
                    if resp == 's': 
                        print("Digite a quantidade de alimentos para comer: ")
                        c = int(input())
                        if c < self.inventario ["Alimento"]:
                            self.comer(c)      
                        else:
                            print("quantidade maior do que vc possui! Digite novamente")
                    
                    elif resp == 'n':
                        print("Deseja dormir para recuerar energia?")
                        resp = input()
                        if resp == 's':
                            print("quantas horas deseja dormir?")
                            d = int(input())
                            self.dormir(d)
                            break
                        elif resp == 'n':
                            print("Vc desmaiou, pois não tem força") 
                            self.desmaiar()
                            break  
                        
                                                        
                else:      
                    print("Deseja dormir para recuerar energia?")
                    resp = input()
                    if resp == 's':
                        print("quantas horas deseja dormir?")
                        d = int(input())
                        self.dormir(d)
                        break
                    elif resp == 'n':
                        print("Vc desmaiou, pois não tem força") 
                        self.desmaiar()
                        break


            sorteio = random.randint(1,3)

            # quantidade de alimento de acordo com o sorteio
            if sorteio == 1:
                a = 7
            elif sorteio == 2:
                a = 2
            elif sorteio == 3:
                a = 4        

            if resposta == sorteio:
                self.inventario ["Alimento"] += a

            
            
            print("Deseja continuar?") 
            resp = input()
            if resp == 's':
                continuar = True
            elif resp == 'n':
                continuar = False  

            print()
            print()



    def buscarEquipamentos(self):

        continuar = True
        while continuar == True and self.tempo.getDia() < 3:    
            
            self.info()

            print("Digite 1 para buscar no ferro velho")
            print("Digite 2 para fabricar peças")
            print("Digite 3 para roubar peças")

            try:
                resposta = int(input())
            except:
                print("Opção invalida")
                self.buscarEquipamentos()
            
            # gasto de stamina de acordo com a escolha da ação
            if resposta == 1 and self.stamina >= 2:
                self.stamina -= 2
                self.tempo.passarHora(9)
                if self.tempo.getDia() >= 3:
                    return 
            elif resposta == 2 and self.stamina >= 5:
                self.stamina -= 5
                self.tempo.passarHora(9)
                if self.tempo.getDia() >= 3:
                    return 
            elif resposta == 3 and self.stamina >= 3:
                self.stamina -= 3  
                self.tempo.passarHora(9)
                if self.tempo.getDia() >= 3:
                    return 
            else:

                resposta = 0
                
                print("Opa! Parece que você não tem stamina para concluir essa tarefa")
                if self.inventario ["Alimento"] > 0:             
                    
                    print(f"Vc tem {self.inventario ['Alimento']} alimento. Deseja comer? S/N")
                    resp = input()
                    if resp == 's': 
                        print("Digite a quantidade de alimentos para comer: ")
                        c = int(input())
                        if c < self.inventario ["Alimento"]:
                            self.comer(c)      
                        else:
                            print("quantidade maior do que vc possui! Digite novamente")
                    
                    elif resp == 'n':
                        print("Deseja dormir para recuerar energia?")
                        resp = input()
                        if resp == 's':
                            print("quantas horas deseja dormir?")
                            d = int(input())
                            self.dormir(d)
                            break
                        elif resp == 'n':
                            print("Vc desmaiou, pois não tem força") 
                            self.desmaiar()
                            break  
                        
                                                        
                else:      
                    print("Deseja dormir para recuerar energia?")
                    resp = input()
                    if resp == 's':
                        print("quantas horas deseja dormir?")
                        d = int(input())
                        self.dormir(d)
                        break
                    elif resp == 'n':
                        print("Vc desmaiou, pois não tem força") 
                        self.desmaiar()
                        break
                    

            sorteio = random.randint(1,3)

            # quantidade de equipamento de acordo com o sorteio
            if sorteio == 1:
                e = 2
            elif sorteio == 2:
                e = 7
            elif sorteio == 3:
                e = 4        

            if resposta == sorteio:
                self.inventario ["Equipamento"] += e 


            print("Deseja continuar?") 
            resp = input()
            if resp == 's':
                continuar = True
            elif resp == 'n':
                continuar = False  
        
            print()
            print()            
                     


    def relogio (self):
        return self.tempo.getDia()


    def comer (self, comida):
        self.inventario ["Alimento"] -= comida       
        self.stamina += comida

        
    def dormir(self, horasDormidas):
        self.tempo.passarHora(horasDormidas)
        self.stamina += horasDormidas
        if self.stamina >= 10:
            self.stamina = 10
    

    def desmaiar(self):
        self.stamina = 8
        self.tempo.passarHora(8)
    

    def acordar(self):
        if self.stamina >= 10:
            print("Você está com {self.estamina} pontos de stamina. Não está cansado! Tente fazer algumas tarefas")
            print()


    def info(self):
        print("inventário:", self.inventario)
        print("dia:", self.tempo.getDia())
        print("hora:", self.tempo.getHora())
        print("stamina:",self.stamina)
        print()

    
        

    