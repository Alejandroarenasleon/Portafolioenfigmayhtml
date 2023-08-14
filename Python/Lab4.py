def Contar(n):
    cont=0
    while n>0:
        cont+=1
        n=n//10
    return cont

n=int(input("Ingrese el valor del numero:\n"))
while n>0:
    x=n // 10**(Contar(n)-1)
    print(x)
    n=n % 10**(Contar(n)-1)
    