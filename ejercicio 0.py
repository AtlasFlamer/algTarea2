@nombre n = filas
@nombre m = columnas
def nueva(n, m):
    tmp = []
    m = int(input("Ingrese la cantidad de filas que desea: "))
    n = int(input("Ingrese la cantidad de columnas que desea: "))
    for f in range(m):
        tmp.append([])
        for c in range(n):
            tmp[f].append(int(input("Ingrese un numero: ")))
    for f in range(m):
        for c in range(n):
            print(tmp[f][c], end=" ")
        print()
    return tmp