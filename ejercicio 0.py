from copy import deepcopy

def mostrar( m ):
    for f in range(len(m)):
        for c in range(len(m[0])):
            print  (m[f][c], end= " " )
        print ()
    print ()

def nueva(n, m):
    tmp = []
    for f in range(m):
        tmp.append([])
        for c in range(n):
            tmp[f].append( '*'  )
    return tmp

def chop(m):
    tmp = deepcopy(m)
    l = len(m) -1 
    y =  int( ( len(m)-1  )/ 2)
    for i in range (y):
        for j in range ( y - i):
            tmp[i][j] = 0
            tmp[-i - 1][-j -1] = 0
            tmp[i][-j-1] = 0
            tmp[-i -1 ][j] = 0


    
    return tmp


entrada = 15

matriz = nueva(entrada,entrada)


       

mostrar( chop(matriz) )

