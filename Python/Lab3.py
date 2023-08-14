def DigMasRep(n):
    Dig=0
    contDig=0
    x=0
    y=0
    r=0
    cont=1
    while n>0:
        x= n % 10
        n= n // 10
        while n > 0:
            y= n % 10
            if x==y:
                cont+=1
            else:
                r=r*10+y
            n= n // 10
        if cont>contDig:
            contDig=cont
            Dig=x
        cont=1
        n=r
        r=0
    return Dig

def ElimDig(n,dig):
    r=0
    x=0
    while n>0:
        x= n % 10
        if x != dig:
            r= r*10+x
        n= n//10
    return r

m=int(input("Ingrese el valor del numero:\n"))
for i in range(1,3):
    m=ElimDig(m,DigMasRep(m))
print(m)