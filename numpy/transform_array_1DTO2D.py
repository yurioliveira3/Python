# Transforme um array do NumPy de uma dimensão e comprimento igual a 10
# em um array de duas dimensões, com 2 linhas e 5 colunas (sem utilizar laços)
import numpy as np

if __name__ == "__main__":
    
    #array 1 to 10
    arr = np.arange(1, 11, 1)

    #reshape the array 2 lin, 5 col
    newarr = arr.reshape(2, 5)

    print("Original array:\n", arr,"\nReshaped array:\n",newarr)