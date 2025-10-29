from Especie import *
from random import *
import time
import os
from caracteristicas import *



contadorMutacoes  = 0
limiteMaximoGene = 10
tamanhoPopulacao = 10
tamanhoCaracteristica1 = 5
tamanhoCaracteristica2 = 5
tamanhoCaracteristica3 = 5
valorTaxaMutacao = 90 
valorTaxaSelecao = 80
contadorReproducaoFalha = 0
popnewage = []
novaGeracao = []
melhor_valor = 0


def limpar():
    print("digite enter para continuar!")
    input()
    s = os.name
    if s == "nt":
        os.system('cls')
    else:
        os.system('clear')
def limpar2():
    
    s = os.name
    if s == "nt":
        os.system('cls')
    else:
        os.system('clear')


def geracaoIndividuo():
    individuo = Especie("Pan Paniscus",choice(["M","F"])) 

    caracteristica1 = []
    caracteristica2 = []
    caracteristica3 = []    
    

    for i in range(0, tamanhoCaracteristica1): #Característica 1
        caracteristica1 += [randint(1, limiteMaximoGene)]
    individuo.caracteristica1 = caracteristica1

    
    # Característica 2


    for i in range(0, tamanhoCaracteristica2):
            caracteristica2 += [randint(1, limiteMaximoGene)]
            individuo.caracteristica2 = caracteristica2



    #Característica 3

    for i in range(0, tamanhoCaracteristica3):
            caracteristica3 += [randint(1, limiteMaximoGene)]
    individuo.caracteristica3 = caracteristica3





    return individuo




def reproducaoIndividuos(par1, par2):
    individuo = Especie("Bonobo", choice(["M","F"])) #  Acho que pode tirar
    caracteristica1 = []
    caracteristica2 = []
    caracteristica3 = []    

    if par1.sexo != par2.sexo:

        for (i, j) in zip(par1.caracteristica1, par2.caracteristica1):
            caracteristica1 += [max(i, j)]
        individuo.caracteristica1 = caracteristica1 #Característica 1



        # Característica 2

        for (i, j) in zip(par1.caracteristica2, par2.caracteristica2):
            caracteristica2 += [max(i, j)]
        individuo.caracteristica2 = caracteristica2

        #Característica 3

        for (i, j) in zip(par1.caracteristica3, par2.caracteristica3):
            caracteristica3 += [max(i, j)]
        individuo.caracteristica3 = caracteristica3
        
   
        


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



    if randint(1, 100) <= valorTaxaMutacao:
        i = randint(0, tamanhoCaracteristica2 - 1)
        individuo.caracteristica2[i] = randint(1,limiteMaximoGene)
        contadorMutacoes += 1


    if randint(1, 100) <= valorTaxaMutacao:
        i = randint(0, tamanhoCaracteristica3 - 1)
        individuo.caracteristica3[i] = randint(1, limiteMaximoGene)
        contadorMutacoes += 1
        
    return individuo

def avaliacaoPopulacao(populacao): ######
    melhor_individuo = None
    melhor_valor = float('-inf')

    for individuo in populacao:
        soma_total = (
            sum(individuo.caracteristica1) +
            sum(individuo.caracteristica2) +
            sum(individuo.caracteristica3)
        )

        if soma_total > melhor_valor:
            melhor_valor = soma_total
            melhor_individuo = individuo

    return melhor_individuo, melhor_valor * (valorTaxaSelecao / 100)
    





# ADICIONAR WHILE TRUE COM TRY EXCEPT


limpar()
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
        limpar2()


        if resp == 1:
            break 
            # Código da opção 1

        elif resp == 2:
            print("""
            Bonobos (Pan paniscus)
                  
                              Visão geral:
                  - Bonobo ou macaco-pigmeu;
                  - Rio Zaire, na República Democrática do Congo;
                  - Pacifícos e altamente sociais;
                  - Comportamento sexual;
                  - Disponibilidade de plantas.

                              Reprodução:
                  - As fêmeas têm ciclos estrais e entram em cio ativo;
                  - Gestação dura cerca de 8 meses;
                  - Relações hetereossexuais e homossexuais;
                  - resolvem conflitos; Fortalecimento de laços sociais; 
                    Reduzir o estresse.
                  
                              Curiosidades:
                  - 98,7% do DNA igual ao dos humanos;
                  - Comunidade matriaracal;
                  - Brincalões e inteligentes;
                  - Empatia -> Compartilha alimento;
                  - Risco de extinção;
                  - Automedicação -> Zoofarmacognosia.


""")
            limpar()
            # Código da opção 2
        
        elif resp == 3:
            print(""" 🧬 O DNApice-II é um programa que simula, de forma bem simplificada, o processo de reprodução e evolução genética de uma espécie fictícia chamada 
                    Pan Paniscus (o nome científico do bonobo, um tipo de macaco). 
                    Ele cria uma pequena população de indivíduos, cada um com suas características genéticas, 
                    e depois faz com que eles se reproduzam, gerando novos indivíduos com mistura dos genes dos “pais”. 
                    Durante esse processo, o programa também simula a mutação genética, ou seja, 
                    pequenas mudanças aleatórias que podem acontecer no DNA de um indivíduo — o que imita o que ocorre na natureza.

            ⚙ Etapas principais do programa

                1- Criação dos indivíduos iniciais
                    O programa gera uma população com alguns indivíduos.
                    Cada um tem:
                    Um nome científico (“Pan Paniscus”);
                    Um sexo (masculino ou feminino, escolhido aleatoriamente);
                    Um conjunto de características genéticas (números que representam “genes”).

                2-Reprodução
                    O programa tenta formar pares de indivíduos de sexos diferentes.
                    Cada par “gera um novo indivíduo”, combinando os genes dos pais — 
                    geralmente escolhendo o melhor gene de cada par (como se pegasse o mais forte de cada um).

                3-Mutação genética
                    Às vezes (com uma certa chance), 
                    um dos genes do novo indivíduo muda para outro número aleatório — 
                    isso representa uma mutação, que pode deixar o novo indivíduo mais ou menos adaptado.
                    Avaliação dos indivíduos
                    O programa soma os valores dos genes de cada indivíduo para medir quem é o mais adaptado (ou mais forte).
                    Só os novos indivíduos com características boas o suficiente são considerados selecionados para continuar.

                4-Relatórios e estatísticas
                    Depois da simulação, o usuário pode escolher o que quer ver:
                    Os indivíduos selecionados (os “melhores”);
                    Quantas tentativas de reprodução falharam (pares do mesmo sexo, por exemplo);
                    Quantas mutações genéticas aconteceram;
                    Ou a lista da população inicial.

                💡 Em resumo
                    O DNApice-II é uma simulação simples de evolução biológica.
                    Ele mostra como reprodução, seleção natural e mutação genética podem mudar uma população ao longo do tempo, 
                  
                    mesmo que de forma bem simbólica e usando números em vez de DNA real.  

        """)
            limpar()

        elif resp == 4:

            tamanhoPopulacao = int(input("Qual será o tamanho da população inicial?"))
            tamanhoPopNewAge = int(input("Quantos indivíduos poderão fazer parte dos selecionados?"))
            limpar2()

            if tamanhoPopNewAge > tamanhoPopulacao:
                print("ERRO! O NÚMERO DE INDIVÍDUOS SELECIONADOS NÃO PODE SER MAIOR QUE A POPULAÇÃO TOTAL")
                limpar()
                break


            populacao = [geracaoIndividuo() for i in range(0, tamanhoPopulacao)]

            
            
            
          
            for i in range(0, len(populacao) - 1):
                par1 = populacao[i]
                par2 = populacao[i + 1]

                if par1.sexo != par2.sexo:
                    ind3 = reproducaoIndividuos(par1, par2)
                    ind3 = mutacaoGenetica(ind3)

                    valor_ind3 = sum(ind3.caracteristica1) + sum(ind3.caracteristica2) + sum(ind3.caracteristica3)
                    

        
                    if valor_ind3 >= melhor_valor and len(popnewage) < tamanhoPopNewAge:
                        popnewage.append(ind3)
                else:
                    contadorReproducaoFalha += 1

            while True:
                    try:
                        print("Escolha uma opção:")
                        resp2 = int(input("""
                        1 - Mostrar indivíduos selecionados
                        2 - Mostrar número de reproduções falhas
                        3 - Mostrar o número de mutações genéticas que ocorreram em toda a população
                        4 - Mostrar a população inicial
                        6- Taxa de manutenção genética
                        5- Sair                     """))
                        limpar2()
                    
                        if resp2 == 1:
                            
                            if len(popnewage) == 0:
                                print("Nenhum indivíduo sobreviveu")

                            else:

                                for individuo in popnewage:
                                    # Adicionar mais dois para as outras características
                                    print(f"{individuo.nomeCientifico} - {individuo.sexo}")
                                    print(f"Característica 1: {individuo.caracteristica1}")
                                    print(f"Por isso, a cor do seu olho é {c1[individuo.caracteristica1[0]]}")

                                    print(f"Característica 2: {individuo.caracteristica2}")
                                    print(f"Por isso, seu comportamento é {c2[individuo.caracteristica2[0]]}")

                                    print(f"Característica 3: {individuo.caracteristica3}")
                                    print(f"Por isso, a cor do seu pelo é {c3[individuo.caracteristica3[0]]}")

                                limpar()
                        
                        elif resp2 == 2:
                            print(f"O número de reproduções que falharam foi: {contadorReproducaoFalha}")

                            limpar()
                        elif resp2 == 3:
                            print(f"O número de mutações que ocorreram foi: {contadorMutacoes}")
                            limpar()

                        elif resp2 == 4:
                            for individuo in populacao:
                                # Adicionar mais dois para as outras características
                                    print(f"{individuo.nomeCientifico} - {individuo.sexo}")
                                    print(f"Característica 1: {individuo.caracteristica1}")
                                    print(f"Por isso, a cor do seu olho é {c1[individuo.caracteristica1[0]]}")

                                    print(f"Característica 2: {individuo.caracteristica2}")
                                    print(f"Por isso, seu comportamento é {c2[individuo.caracteristica2[0]]}")

                                    print(f"Característica 3: {individuo.caracteristica3}")
                                    print(f"Por isso, a cor do seu pelo é {c3[individuo.caracteristica3[0]]}")
                                
                                    print()
                                    limpar()
                        elif resp2 == 5:
                            print("Saindo...")
                            time.sleep(2)
                            limpar2()
                            break

                        
                            
                        elif resp2 == 6:
    
                            if not popnewage or not populacao:
                                print("Erro: É necessário ter uma população e uma nova geração para calcular a taxa genética.")
                                limpar()
                            else:
                                genes_mantidos1 = genes_totais1 = 0
                                genes_mantidos2 = genes_totais2 = 0
                                genes_mantidos3 = genes_totais3 = 0

                                # Compara indivíduo a indivíduo entre as gerações
                                for i in range(min(len(popnewage), len(populacao))):
                                    filho = popnewage[i]
                                    pai = populacao[i]  # Supondo correspondência de índice (mesmo "número" de indivíduo)

                                    # Característica 1
                                    for g1, g2 in zip(filho.caracteristica1, pai.caracteristica1):
                                        genes_totais1 += 1
                                        if g1 == g2:
                                            genes_mantidos1 += 1

                                    # Característica 2
                                    for g1, g2 in zip(filho.caracteristica2, pai.caracteristica2):
                                        genes_totais2 += 1
                                        if g1 == g2:
                                            genes_mantidos2 += 1

                                    # Característica 3
                                    for g1, g2 in zip(filho.caracteristica3, pai.caracteristica3):
                                        genes_totais3 += 1
                                        if g1 == g2:
                                            genes_mantidos3 += 1

                                # Exibição dos resultados
                                if genes_totais1 > 0:
                                    porcentagem = (genes_mantidos1 / genes_totais1) * 100
                                    print(f"{porcentagem:.2f}% dos genes se mantiveram entre as gerações na característica 1.")
                                    limpar()
                                else:
                                    print("Nenhum gene foi mantido na característica 1.")
                                    limpar()

                                if genes_totais2 > 0:
                                    porcentagem = (genes_mantidos2 / genes_totais2) * 100
                                    print(f"{porcentagem:.2f}% dos genes se mantiveram entre as gerações na característica 2.")
                                    limpar()
                                else:
                                    print("Nenhum gene foi mantido na característica 2.")
                                    limpar()

                                if genes_totais3 > 0:
                                    porcentagem = (genes_mantidos3 / genes_totais3) * 100
                                    print(f"{porcentagem:.2f}% dos genes se mantiveram entre as gerações na característica 3.")
                                    limpar()
                                else:
                                    print("Nenhum gene foi mantido na característica 3.")
                                    limpar()
                                    


                            

                        else:
                            print("Erro, opção inválida")
                            limpar()



                    except ValueError:
                        print("Erro: Digite um número válido")
                        print("Limpando a tela...")
                        time.sleep(3)
                        limpar2()
                        # Será que seria melhor usar um input() vazio para limpar a tela?
                        
                        # Verificar o sistema operacional para apagar


        else:  
            print("Erro, opção inválida")
            limpar()           
                    
                    


                

        # Mudei aqui pq não fazia sentido verificar se ind3 era diferente de nulo mais uma vez, por isso adicionei logo após a reprodução
        
        # Código da opção 4



    except ValueError:
        print("Erro: Digite um número válido")
        print("Limpando a tela...")
        time.sleep(3)
        limpar2()

    

        
            



        
    # FRU FRU PARA O CLIENTE, COLOCAR TIPO: ESPÉCIES COISAS
   

    # OUTRO FRU FRU PARA ESPÉCIES SUPER DESENVOLVIDAS
    

    


