# Imports
import math as m
from numpy import random as rand

class Retangulo: 
    #Construtor
    def __init__(self, L, A):
        self.L = L
        self.A = A

    #Função que calcula a area do Retangulo    
    def area(self):
        return (self.L * self.A)

    def print(self):
        print("Base:", self.L, "Altura:", self.A)

class Circulo: 
    #Construtor
    def __init__(self, R):
        self.R = R

    #Função que calcula a area do Circulo    
    def area(self):
        return ((self.R**2 * m.pi)/2)

    def print(self):
        print("Raio:", self.R)

class Triangulo: 
    #Construtor
    def __init__(self, B, H):
        self.B = B
        self.H = H

    #Função que calcula a area do Triangulo    
    def area(self):
        return ((self.B * self.H)/2)

    def print(self):
        print("Base:", self.B, "Altura:", self.A)

if __name__ == "__main__":
    
    randomlist = []

    for i in range(0,20):
        #Cria os objetos
        tmpR = Retangulo(rand.randint(1,10),rand.randint(1,10)); 
        tmpC = Circulo(rand.randint(1,10));
        tmpT = Triangulo(rand.randint(1,10),rand.randint(1,10));

        #Adiciona objetos
        randomlist.append(tmpR)
        randomlist.append(tmpC)
        randomlist.append(tmpT)

    sum = 0
    
    print(len(randomlist))

    rand.shuffle(randomlist)

    for i in range(len(randomlist)):  
        #randomlist[i].print()
        sum += randomlist[i].area()

    print("O somatório das áreas é: {:.2f}".format(sum));
