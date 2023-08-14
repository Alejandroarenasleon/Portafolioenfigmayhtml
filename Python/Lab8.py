"""DADO DOS NUMEROS ENTEROS POSITIVOS, VERIFICAR SI CADA DIGITO DEL PRIMER NUMERO TIENE SU PARIDAD
   EN EL SEGUNDO NUMERO, PARA TAL EFECTO, SE DEBERÁ IMPRIMIR "EL NUMERO ESTA BALANCEADO", CASO CONTRARIO
   "EL NUMERO NO ESTA BALANCEADO"
   EJ. A=15964722
       B=596433232177 """
from Funciones import *
a=int(input("Ingrese el valor para el primer numero:\n"))
b=int(input("Ingrese el valor para el segundo numero:\n"))
while a>0:
    x=a%10
    if ContarDig(a,x)<=ContarDig(b,x):
        a=ElimDig(a,x)
        b=ElimDig(b,x)
    else:
        a=-1
if a==0:
    print("El numero esta balanceado")
else:
    print("El numero no esta balanceado")
