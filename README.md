# algTarea2

1.- (20 pts) El dadoloco es un juego muy popular entre los niños de la aldea de PUCV-LAND. El juego consiste en lanzar varias veces un dado. Si en alguno de los lanzamientos aparece el número 1, el jugador PIERDE EL JUEGO. Para ganar, al jugador debe aparecerle un número (distinto de 1) tantas veces consecutivas como indica el mismo número (por ejemplo, el 2 dos veces seguidas). Escriba un algoritmo en Python que almacene en un arreglo todos los números obtenidos al lanzar un dado hasta que termine el juego, y le indique al usuario si ganó o perdió. El juego termina “sin ganadores” si alguno de los jugadores llega a los 100 tiros. Ocupe la función randint() para simular el tiro del dado.


2.- (20 pts) Un número se dice circular si es posible recorrerlo de la siguiente manera: Se toma el dígito de más a la izquierda y su valor indicará la cantidad de veces que se debe contar hacia la derecha, esta cuenta se detiene en un dígito del número el cual también indicará la cantidad de veces que se debe contar hacia la derecha y así sucesivamente. Este proceso da origen a un número circular si todos los dígitos del número se consideran tan sólo una vez (como número Originador de un conteo) y además se retorna al dígito de más a la izquierda que fue el que comenzó el conteo. Escriba un algoritmo en Python que permita determinar si un número es circular o no. Valide que no existan dígitos repetidos. El algoritmo DEBE guardar el número ingresado por el usuario en un arreglo. El usuario podrá ingresar números entre 100 y 100.000. Se recomienda usar arreglo(s) para implementar este algoritmo. El usuario ingresa un número entre 100 y 100.000, no una secuencia de dígitos
Ejemplo:
Si el un número ingresado es 81362
(1) 8 1 3 6 2
(2) 8 1 3 6 2
(3) 8 1 3 6 2
(4) 8 1 3 6 2
(5) 8 1 3 6 2
(6) 8 1 3 6 2
Este es un número circular!


3.- (20 pts) El determinante de una matriz es un escalar que sólo se puede calcular si se trata de una matriz cuadrada. El determinante de una matriz determina si los sistemas son singulares o mal condicionados. En otras palabras, sirve para determinar la existencia y la unicidad de los resultados de los sistemas de ecuaciones lineales. El determinante de una matriz es un número. En esta tarea usted deberá estudiar cómo se calculan los determinantes de matrices cuadradas de 2x2, 3x3 y 4x4 e implementar un algoritmo en Python que lo calcule. Dicho algoritmo deberá solicitar:

    La dimensión de la matriz (2, 3 o 4). El sistema deberá enviar un error     si el número no esta en el rango y terminar su ejecución.
    
    Los números con los que se llenan la matriz

    El valor del determinante de la matriz

Estudiar el concepto del determinante es fundamental para la correcta implementación del algoritmo ya que existen algunos casos especiales en los que el cálculo del determinente cambia.
