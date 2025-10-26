from Especie import *
from random import *
import time
import os
from caracteristicas import *


contadorMutacoes  = 0
limiteMaximoGene = 9
tamanhoPopulacao = 10
tamanhoCaracteristica1 = 5
valorTaxaMutacao = 90 
valorTaxaSelecao = 80

def geracaoIndividuo():
    individuo = Especie("Pan Paniscus",choice(["M","F"])) 
    caracteristica = []
    for i in range(0, tamanhoCaracteristica1):
        caracteristica += [randint(1, limiteMaximoGene)]
    individuo.caracteristica1 = caracteristica
    return individuo

def reproducaoIndividuos(par1, par2):
    individuo = Especie("Bonobo", choice(["M","F"])) #  Acho que pode tirar
    caracteristica = []
    if par1.sexo != par2.sexo:

        for (i, j) in zip(par1.caracteristica1, par2.caracteristica1):
            caracteristica += [max(i, j)]
        individuo.caracteristica1 = caracteristica
        return individuo
    
    else: 
        print("ERRO") 
        return None

def mutacaoGenetica(individuo):
    global contadorMutacoes  
    if randint(1, 100) <= valorTaxaMutacao:
        i = randint(0, tamanhoCaracteristica1 - 1)
        individuo.caracteristica1[i] = randint(1, limiteMaximoGene)
        contadorMutacoes += 1  
        
    return individuo

def avaliacaoPopulacao(populacao):
    adaptado = 0
    for individuo in populacao:
        somatorio = sum(individuo.caracteristica1)
        if somatorio > adaptado:
            adaptado = somatorio
    return adaptado * (valorTaxaSelecao / 100)






# ADICIONAR WHILE TRUE COM TRY EXCEPT

while True:

    print("Bem vindo ao DNApice-II")

    try:
        print("Escolha uma opção:")
        resp = int(input("""
        1 - Sair
        2- Analisar características gerais da espécie
        3 - Como funciona o programa?
        4 - Iniciar reprodução
        """))


        if resp == 1:
            break 
            # Código da opção 1

        elif resp == 2:
            pass
            # Código da opção 2
        
        elif resp == 3:
            pass
            # Código da opção 3

        elif resp == 4:
            populacao = [geracaoIndividuo() for i in range(0, tamanhoPopulacao-1)]

            contadorReproducaoFalha = 0
            
            popnewage = []
            for i in range(0, len(populacao) - 1):
                par1 = populacao[i]
                par2 = populacao[i+1]
                ind3 = None
                if par1.sexo != par2.sexo:

                    ind3 = reproducaoIndividuos(par1, par2)
                    ind3 = mutacaoGenetica(ind3)


                    
                    if sum(ind3.caracteristica1) >= avaliacaoPopulacao(populacao):
                        popnewage.append(ind3)

                else: contadorReproducaoFalha += 1



            while True:
                    try:
                        print("Escolha uma opção:")
                        resp2 = int(input("""
                        1 - Mostrar indivíduos selecionados
                        2 - Mostrar número de reproduções falhas
                        3 - Mostrar o número de mutações genéticas que ocorreram em toda a população
                        4 - Mostrar a população inicial
                        5- Sair                     """))
                    
                        if resp2 == 1:
                            for individuo in popnewage:
                                print(f"{individuo.nomeCientifico} - {individuo.sexo}")
                                print(f"Característica 1: {individuo.caracteristica1}")
                                print(f"Por isso, a cor do seu olho é {c1[individuo.caracteristica1[0]]}")

                                # Adicionar limpa tela e etc
                        
                        elif resp2 == 2:
                            print(f"O número de reproduções que falharam foi: {contadorReproducaoFalha}")
                            # Adicionar limpa tela e etc

                        elif resp2 == 3:
                            print(f"O número de mutações que ocorreram foi: {contadorMutacoes}")
                            # Adicionar limpa tela e etc

                        elif resp2 == 4:
                            for individuo in populacao:
                                print(f"{individuo.nomeCientifico} - {individuo.sexo}")
                                print(f"Característica 1: {individuo.caracteristica1}")
                                print(f"Por isso, a cor do seu olho é {c1[individuo.caracteristica1[0]]}")
                                
                                print()
                        elif resp2 == 5:
                            print("Saindo...")
                            break

                        else:
                            print("Erro, opção inválida")



                    except ValueError:
                        print("Erro: Digite um número válido")
                        print("Limpando a tela...")
                        time.sleep(3) 
                        # Será que seria melhor usar um input() vazio para limpar a tela?
                        os.system("cls")
                        # Verificar o sistema operacional para apagar


        else:  
            print("Erro, opção inválida")             
                    
                    


                

        # Mudei aqui pq não fazia sentido verificar se ind3 era diferente de nulo mais uma vez, por isso adicionei logo após a reprodução
        
        # Código da opção 4



    except ValueError:
        print("Erro: Digite um número válido")
        print("Limpando a tela...")
        time.sleep(3)
        os.system("cls")

    

        
            



        
    # FRU FRU PARA O CLIENTE, COLOCAR TIPO: ESPÉCIES COISAS
   

    # OUTRO FRU FRU PARA ESPÉCIES SUPER DESENVOLVIDAS
    

    


