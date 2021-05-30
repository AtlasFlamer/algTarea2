#!/bin/python
from random import randint
def pedirJugadores () :
    return int(input("Ingrese la cantidad de jugadores: "))

log = []
def tirarDado():
    for f in range(m):
        a.append([])
        a[f].append(0)
        for c in range(100):
            a[f].append(int(randint(1,6)))

            if  (a[f][c+1] == 1 ):
                
                break

            if a[f][c+1] == a[f][c]:
                veces +=1
                if a[f][c+1] == veces:
                    log.append("gana jugador " + str(f+1))
                    break
            else: 
                veces = 1
        a[f].remove(0)
        if c == 99:
           log.append("todos pierden")
           break
def mostrar( m ):

    for f in range(len (m)):
        print ("jugador", f+1,": ", end = ""  )
        for c in range( len (m[f])):
            print(a[f][c], end=" ")
             

        print()

a = []
m = pedirJugadores()

tirarDado()
        


mostrar(a)

for i in range (len (log)):
    print (log[i])





