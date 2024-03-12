n=int(input("ingresa un numero -> "))
while n!=1:
    if n%2==0:
        n=n//2
        print(n)
        a=a+1
    else:
        n=n*3+1
        a=a+1
        print(n)
print("Cantidad de intentos":,a)