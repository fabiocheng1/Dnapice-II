from Especie import *
from random import *

limiteMaximoGene = 1000
tamanhoPopulacao = 10
tamanhoCaracteristica1 = 5
valorTaxaMutacao = 5 #Taxa de resistência a mutações
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
    if randint(1, 100) <= valorTaxaMutacao:
        i = randint(0, tamanhoCaracteristica1 - 1)
        individuo.caracteristica1[i] = randint(1, limiteMaximoGene)
    return individuo

def avaliacaoPopulacao(populacao):
    adaptado = 0
    for individuo in populacao:
        somatorio = sum(individuo.caracteristica1)
        if somatorio > adaptado:
            adaptado = somatorio
    return adaptado * (valorTaxaSelecao / 100)






# ADICIONAR WHILE TRUE COM TRY EXCEPT

populacao = [geracaoIndividuo() for i in range(0, tamanhoPopulacao-1)]


contadorReproducaoFalha = 0
popnewage = []
for i in range(0, len(populacao) - 1):
    par1 = populacao[i]
    par2 = populacao[i+1]
    ind3 = None
    if par1.sexo != par2.sexo:
        ind3 = reproducaoIndividuos(par1, par2)
    else: contadorReproducaoFalha += 1
    

    if ind3 is not None:
        ind3 = mutacaoGenetica(ind3)
        if sum(ind3.caracteristica1) >= avaliacaoPopulacao(populacao):
            popnewage.append(ind3)



    
# FRU FRU PARA O CLIENTE, COLOCAR TIPO: ESPÉCIES COISAS
for individuo in populacao:
    print(f"{individuo.nomeCientifico} - {individuo.sexo}")
    print(f"Característica 1: {individuo.caracteristica1}")
print()

# OUTRO FRU FRU PARA ESPÉCIES SUPER DESENVOLVIDAS
for individuo in popnewage:
    print(f"{individuo.nomeCientifico} - {individuo.sexo}")
    print(f"Característica 1: {individuo.caracteristica1}")


print(f"O número de reproduções que falharam foi: {contadorReproducaoFalha}")



