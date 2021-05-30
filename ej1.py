#!/bin/python
import random
a=[]
a.append(0)
for cont in range(2):
    a.append((int(random.randint(1,6))))

    if a[cont-1] == a[cont]:
        print ( ">>",  a[cont], " ", a[cont-1], end = " " ) 
        print()

    if a[cont] == 1:
        print("Has perdido")
        break
a.remove(0)

print(a)





