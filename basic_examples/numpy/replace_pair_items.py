#Replace all even number of numpy array 
# not using looping
import numpy as np

def replace_pair(arr):

    arr[arr%2==0] = -1

    return arr

if __name__ == "__main__":

    #create arr with itens of 1 to 5 
    arr2 = np.arange(1, 6, 1)
    #same form of above
    arr = np.array((1, 2, 3, 4, 5))

    print(replace_pair(arr))

    print(replace_pair(arr2))
