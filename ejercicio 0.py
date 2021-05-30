def mostrar( m ):
    for f in range(m):
        for c in range(n):
            print(tmp[f][c], end=" ")
        print()

def nueva(n, m):
    tmp = []
    for f in range(m):
        tmp.append([])
        for c in range(n):
            tmp[f].append(int(input("Ingrese un numero: ")))
    return tmp

matriz = nueva(2, 3)

mostrar(matriz)
