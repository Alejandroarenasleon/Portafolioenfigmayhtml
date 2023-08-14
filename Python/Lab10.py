"""DADO TRES NUMEROS ENTEROS POSITIVOS, IMPRIMIR EL NUMERO QUE CONTENGA LA MAYOR CANTIDAD 
   DE DIGITOS PARES, CON RESPECTO A LOS OTROS DOS NUMEROS."""
from Funciones1 import *
a=int(input("Ingrese el valor para el primer numero:\n"))
b=int(input("Ingrese el valor para el segundo numero:\n"))
c=int(input("Ingrese el valor para el tercer numero:\n"))
if ContarDigPares(a)>ContarDigPares(b) and ContarDigPares(a)>ContarDigPares(c):
    print("Los valos del primer numero es:",a)
elif ContarDigPares(b)>ContarDigPares(a) and ContarDigPares(b)>ContarDigPares(c):
    print("Los valos del segundo numero es:",b)
else:
    print("Los valos del tercer numero es:",c)