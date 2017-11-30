def multiplication_table(m, n):
    for i in range(1,10):
        for j in range(m,n+1):
            print("%s x %s = %s\t" % (j,i,i*j),end='')
        print('')
    print('\n')
    
def pyramid(h):
    for i in range(h):
        print(' '*(h-i)+"*"*(i)*2+"*")    
