def func(A,B): #função que soma A E B
    
    if A*B > 1000:
        return A+B
    else:
        return A*B      

#main
if __name__ == '__main__': 
    print('# Programa que soma 2 numeros #')
    
    A = int(input('Digite um valor para A: '))
    B = int(input('Digite um valor para B: '))
    
    print('Resultado: {rst}'.format(rst=func(A,B)))
