import numpy as np

if __name__ == "__main__":
    #Cria o objeto
    a = [5,7,1,6]

    b = "444Y5&4  URI.!54654"
    #print(a[::-1])
    #print(b[::-1])

    x = [1,5,10]

    x2 = np.array([1,5,10])

    print([x-y for x,y in zip(x[1:],x[:-1])])

    print([x-y for x,y in zip(x2[1:],x2[:-1])])

    
    print("".join([c for c in b if c.isalpha()]))
    print("".join(b.split(" ")))
