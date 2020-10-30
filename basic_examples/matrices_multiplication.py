def mat_mul(A, B): #função que multiplica A E B
    m_a, n_a = len(A), len(A[0]) #Calculando linhas,colunas de A
    m_b, n_b = len(B), len(B[0]) #Calculando linhas,colunas de B

    C = [] #criando C
    for linha in range(m_a):
        C.append([]) #adicionando uma linha na mat
        for coluna in range(n_b):
            C[linha].append(0) #adicionando uma nova coluna na mat
            for k in range(n_a):
                C[linha][coluna] += A[linha][k] * B[k][coluna] #multiplicando

    return C #retornando C

#main
if __name__ == '__main__': 
    print ("#" * 40)
    print ('# Programa que multiplica 2 matrizes #')
    print ("#" * 40)

    #DEFINE A
    A = [[12,7,3],
         [4 ,5,6],
         [7 ,8,9]]

    #DEFINE B
    B = [[5,8,1,2],
         [6,7,3,0],
         [4,5,9,1]]
    
    print ('\nC:')
    print(mat_mul(A,B)) #apresentando o resultado
