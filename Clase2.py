import random
Jugador_12=input("ingresa el nombre de jugador -->")
Jugador_13=input("ingresa el nombre de jugador -->")
Jugador_1=0
Jugador_2=0
while Jugador_1<5 and Jugador_2<5:
    n=random.randint(1,2)
    if n==1:
        Jugador_1+=1
        print(Jugador_12,"gana")
    if n==2:
        Jugador_2+=1
        print(Jugador_13,"gana")
if Jugador_1==5:
    print(Jugador_12,"Ha ganado")
if Jugador_2==5:
    print(Jugador_13,"Ha ganado")


