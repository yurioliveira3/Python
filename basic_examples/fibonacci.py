def fibon(N): #calculate fibon

    C = [];
    A,B,num,i = 0,1,0,0;

    while i < N:
        C.append(A); #append fibonacci values in C
        num = A+B;
        B=A;
        A=num;
        i+=1;
    return C;

#main
if __name__ == '__main__':
    print('# Fibonacci  Series #');
    
    n = int(input('Digit one value for n: '));

    print('Result: {rst}'.format(rst=fibon(n)));
