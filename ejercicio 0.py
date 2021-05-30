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
            tmp[f].append( 0  )
    return tmp

matriz = nueva(3,3)


def indentidad( orden ):
    tmp = nueva( orden, orden)
    for i in range( orden ):
        tmp[i][i] = 1

    return tmp
       

mostrar( indentidad ( 5 ))

