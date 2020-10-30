# 13.Escreva uma classe Retangulo que é inicializada com as propriedades lado e
# altura, e uma classe Circulo que é inicializada com a propriedade raio. Ambas
# classes devem conter seus métodos area() que retorna a área de cada
# respectiva figura geométrica. 
# Crie uma lista de dez objetos, contendo objetos aleatórios de ambas classes e
# Faça uma função que calcula a soma das áreas de todos objetos da lista.

# Import math Library
import math
import random 

class Retangulo: 
    #Construtor de Veiculo
    def __init__(self, L,A):
        self.L = L;
        self.A = A;
        
    def area(self):
        return (self.L * self.A);

    def print(self):
        print("Base:", self.L, "Altura:", self.A)

class Circulo: 
    #Construtor de Veiculo
    def __init__(self, R):
        self.R = R;
        
    def area(self):
        return ((self.R**2 * math.pi)/2);

    def print(self):
        print("Raio:", self.R)

if __name__ == "__main__":
    
    randomlist = []

    for i in range(0,10):
        #Cria os objetos
        tmpR = Retangulo(random.randint(1,30),random.randint(1,30)); 
        tmpC = Circulo(random.randint(1,30));
        #Adiciona objetos
        randomlist.append(tmpR)
        randomlist.append(tmpC)

    sum = 0
    
    for i in range(len(randomlist)):  
        randomlist[i].print()
        sum += randomlist[i].area()

    print("O somatório das áreas é: {:.3f}".format(sum));
    
    

    