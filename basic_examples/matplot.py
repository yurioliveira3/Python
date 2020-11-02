# Utilize a função plot do submódulo matplotlib.pyplot para plotar funções 
# no intervalo [0, 10].
# Inclua legendas explicando qual curva representa qual função.
from numpy import *
#import math as m
import matplotlib.pyplot as plt

def f1(t):
    #return np.float((m.e ** ((-t)/10)) * m.sin(m.pi * t))
    return float((exp((-t)/10)) * sin(pi * t))

def f2(t):
    #return np.float(t * (m.e ** ((-t)/3)))
    return float(t * (exp((-t)/3)))

if __name__ == "__main__":
    
    #Define a values of function
    x = linspace(0,4*pi,40)
    
    #Define a vectorized function which takes a nested sequence of objects or numpy arrays 
    # as inputs and returns a single numpy array or a tuple of numpy arrays
    f1_ = vectorize(f1) 
    f2_ = vectorize(f2)

    #plt.ylabel('some numbers')
  
    #Plot functions
    plt.plot(x, f1_(x), 'o--r',label='e^(-t/10) * sen(π * t)')
    plt.plot(x, f2_(x), 'o--b',label='t * e^(-t/3)')

    plt.title('Funções F1 e F2')
    #Pop-up with legends
    plt.legend()
    plt.show()
