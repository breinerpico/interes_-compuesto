import math

#input 

C= int(input("Digite el valor del capital inicial: "))

#processing

N = 0 
D = 2 * C

while (C<=D):
    C=1.05 * C
    N = N+1

#output

print("capital inicial: " + str (D / 2))

print("su capital final es:" + str(C))

print("El numero de meses en el que el capital se duplica es: " + str(N))
