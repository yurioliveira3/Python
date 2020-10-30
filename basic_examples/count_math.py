def count(C): 
    #count how many times i appers in C
    dic = {i:C.count(i) for i in C}
    print(dic);

#main
if __name__ == '__main__': 
    
    C = [1,2,1,4,4];
    count(C);
