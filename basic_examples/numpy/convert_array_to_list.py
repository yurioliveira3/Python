# Função que recebe um array do NumPy de duas dimensões e retorna
# duas listas:
# a primeira contendo os maiores elementos de cada coluna
# segunda contendo os maiores elementos de cada linha.

import numpy as np

def convert_arr(array):
    list_ = array.tolist() #simple convert
    list1, list2 = [], []

    #range(array.ndim) 
    #(len(list_[0]) -> get the len of list 1
    #list_[A][B] -> acesse element B in list A

    for i in range(len(array)-1):
        for j in range(len(list_[0])):
            if list_[i][j] > list_[i+1][j]: #colun 1 > 2
                list1.append(list_[i][j])
            else:
                list1.append(list_[i+1][j]) #colun 2 > 1

    for i in range(array.ndim):
       list2.append(max(list_[i])) # get the high value of lists

    return list1,list2


if __name__ == "__main__":

    arr = np.array([[1, 2, 3, 4, 5], 
                    [6, 4 ,3 ,2 ,1]])

    print(convert_arr(arr))

    # print(arr.ndim) #dimension of array
    # print(type(arr))