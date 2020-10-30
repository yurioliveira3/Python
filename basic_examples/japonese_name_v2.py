def jname(name): 

    newname = '';

    dic = {'A':"KA",'B':"TSU",'C':"MI",'D':"TE",'E':"KU",'F':"RU",'G':"JI",'H':"RI",'I':"KI",'J':"ZU",'K':"ME",'L':"TA",'M':"RIN",'N':"TO",'O':"MO",'P':"NO",'Q':"KE",'R':"SHI",'S':"ARI",'T':"CHI",'U':"DO",'V':"RU",'X':"NA",'W':"MEI",'Y':"FU",'Z':"RA",' ':" "}
    
    dic_hir = {'A':"か",'B':"つ",'C':"み",'D':"て",'E':"く",'F':"る",'G':"じ",'H':"り",'I':"き",'J':"ず",'K':"め",'L':"た",'M':"りん",'N':"と",'O':"も",'P':"の",'Q':"け",'R':"し",'S':"あり",'T':"ち",'U':"ど",'V':"る",'X':"な",'W':"めい",'Y':"ふ",'Z':"ら",' ':" "}

    for l in name:
        for k,v in dic.items():
            if(l.upper() == k):
                #print(v)
                newname+=v;

    return newname;

def jname_hir(name): 

    newname = '';
    
    dic_hir = {'A':"か",'B':"つ",'C':"み",'D':"て",'E':"く",'F':"る",'G':"じ",'H':"り",'I':"き",'J':"ず",'K':"め",'L':"た",'M':"りん",'N':"と",'O':"も",'P':"の",'Q':"け",'R':"し",'S':"あり",'T':"ち",'U':"ど",'V':"る",'X':"な",'W':"めい",'Y':"ふ",'Z':"ら",' ':" "}

    for l in name:
        for k,v in dic_hir.items():
            if(l.upper() == k):
                #print(v)
                newname+=v;

    return newname;

#main
if __name__ == '__main__': 
    
    name = input('Digite seu nome:')
    #name = 'Gabriela'
    # print(jname(name));
    # print('\n')
    print(jname_hir(name));
