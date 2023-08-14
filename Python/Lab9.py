"""DADO DOS NUMEROS ENTEROS POSITIVOS, IMPRIMIR TODOS LOS DIGITOS DEL PRIMER NUMERO 
   QUE NO SE ENCUENTREN EN EL SEGUNDO NUMERO."""
from Funciones import *
a=int(input("ingrese un numero:"))
b=int(input("ingrese un numero:"))
r=0
x=0
while a>0:
    x=a%10
    if ContarDig(b,x)==0:
        r=r*10+x
    a=a//10
print(r)