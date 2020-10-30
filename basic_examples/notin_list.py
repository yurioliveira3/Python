def append_ifnotexists(n,C): 

    if(n not in C): #verify if n is in the list
        print('The number {_n} not existis in the list'.format(_n=n));
        C.append(n);
        print('Add:',C);
    else: 
        print('The number {_n} already existis in the list'.format(_n=n));

#main
if __name__ == '__main__': 
    
    #n,C = 5,[1,2,3,4];
    n,C = "AAAAAAAAAA",["AAAAAAAAAB","AAAAAAAAAA"]

    append_ifnotexists(n,C);
