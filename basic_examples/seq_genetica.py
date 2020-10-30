# Faça um programa que recebe uma sequência genética de aminoácidos na
# forma de uma string longa com as letras A, C, G, T (por exemplo
# “ACGAATTCCGCGAATTC”) e retorna todas as substrings de exatamente 10
# aminoácidos que se repete pelo menos uma vez.
from collections import Counter

#verify if sequence not exists
def append_ifnotexists(n,C): 
    #verify is a valid sequence
    if(len(n) == 10):
        return C.append(n);
    else: 
        return C;
        
#main
if __name__ == '__main__': 
    
    seq= "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
    # result = ["AAAAACCCCC","CCCCCAAAAA"]
    # seq = "AAAAAAAAAAAA"
    # result = ["AAAAAAAAAA"]

    tmp= '';
    result = [];

    i,j = 0,0;
    
    for i in range(len(seq)):
        #verify all possible sequences
        tmp+=seq[i:i+10];

        #verify if is a valid sequence
        if(len(n) == 10):
            result.append(n);
        
        tmp = '';

#dictionary with count of sequences
result_ordered = Counter(result)

#save only sequece counter is > 1 
res = [k for k, v in result_ordered.items() if v > 1]

print(res)

    