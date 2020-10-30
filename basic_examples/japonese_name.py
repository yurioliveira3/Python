def jname(name): 

    newname = '';

    dic = {'A':"KA",'B':"TU",'C':"MI",'D':"TE",'E':"KU",'F':"LU",'G':"JI",'H':"RI",'I':"KI",'J':"ZU",'K':"ME",'L':"TA",'M':"RIN",'N':"TO",'O':"MO",'P':"NO",'Q':"KE",'R':"SHI",'S':"ARI",'T':"CHI",'U':"DO",'V':"RU",'X':"NA",'W':"MEI",'Y':"FU",'Z':"RA",' ':" "}

    for l in name:
        for k,v in dic.items():
            if(l.upper() == k):
                #print(v)
                newname+=v;

    return newname;

#main
if __name__ == '__main__': 
    
    name = input('Digite seu nome:')
    #name = 'Gabriela'
    print(jname(name));
