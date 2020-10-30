import re

def cap(A):
    #Split the list
    _A = A.split();
    #tmp empty list
    tmp = [];

    #iterate in list
    for p in _A:
        #if first letter is upper
        if(p[0].isupper()):
            #append in tmp list
            tmp.append(re.sub('[^A-Za-z]+','', p));

    #return the tmp list
    return tmp

#main
if __name__ == '__main__': 
    
    #test list
    A= 'Test yuri Oliveira txt'
    
    B= 'Test,yuri Oliveira. txt'

    #call function
    print(cap(B))

    #[a-zA-Z]
    
    