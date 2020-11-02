#normalize o array sepallength para todos valores fiquem na escala 0 a 1.
import numpy as np

def norm(x):
    return x / np.sqrt(np.sum(x**2))

if __name__ == '__main__':

    url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data' 
    sepallength = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0])
    
    print(norm(sepallength))