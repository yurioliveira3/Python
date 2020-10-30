#main
if __name__ == '__main__':

    d1 = {'Dez': 10, 'Vinte': 20, 'Trinta': 30}
    d2 = {'Trinta': 30, 'Quarenta': 40, 'Cinquenta': 50}
    dtmp = {}
    
    #copy d1
    dtmp = d1.copy();

    #merge d2 with d2
    dtmp.update(d2);

    print(dtmp)