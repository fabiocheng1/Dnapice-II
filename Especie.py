from random import *

class Especie:

    def __init__(self, nomeCientifico, sexo):
        
        self.nomeCientifico = nomeCientifico  
        self.sexo = sexo
        self.caracteristica1 = [] #Cor dos olhos
        self.caracteristica2 = [] #Comportamento
        self.caracteristica3 = [] #Cor do pelo
    
    