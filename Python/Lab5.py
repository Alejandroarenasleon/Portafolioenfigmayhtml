from Funciones import *
a=int(input("Ingrese los valores para el primer conjunto:\n"))
b=int(input("Ingrese los valores para el segundo conjunto:\n"))
c=a
while b>0:
    x=b % 10
    if ContarDig(c,x)==0:
        c=c*10+x
    b=b//10
print(c)