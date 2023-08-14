from Funciones import *
a=int(input("Ingrese el valor para el primer numero:\n"))
b=int(input("Ingrese el valor para el segundo numero:\n"))
dig=int(input("Ingrese el valor del digito a buscar:\n"))
if ContarDig(a,dig)>ContarDig(b,dig):
    print(a)
else:
    print(b)