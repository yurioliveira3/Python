# Crie um array do NumPy de uma dimensão com inteiros aleatórios entre 0-10.
# Em seguida escreva código que mostre o array resultante depois de
# remover todos elementos no intervalo inclusivo de 4 a 7 (sem laços)

import numpy as np
import random 

if __name__ == "__main__":
    
    #array with random element between 1 to 10
    #arr = np.random.randint(1,11,10)
    arr = np.random.choice(11,10)
    #                       '  '-> number of elements  
    #                       '-> range of elements [0-10]

    # Delete all occurrences of elements between 4 to 7
    newarr = np.delete(arr, np.argwhere((arr >= 4) & (arr <= 7)))  

    print("Original array:\n", arr,"\nAjusted array:\n",newarr)