import random
Jugador_12=input("ingresa el nombre de jugador 1 -->")
Jugador_13=input("ingresa el nombre de jugador 2 -->")
Jugador_1_Healt=300
Jugador_2_healt=300
while Jugador_1_Healt>0 and Jugador_2_healt>0:
    n=random.choice([5,10,30,45,46,15,3,3,3,5,5,6,5,7,8,23,43,1,0,0,0,0,0,1,2,3,100])
    print("//",Jugador_12,"Ha hecho",n,"de daño a",Jugador_13,"//")
    if Jugador_1_Healt>0:
        Jugador_2_healt-=n
    n=random.choice([5,10,30,45,46,15,3,3,3,5,5,6,5,7,8,23,43,1,0,0,0,0,0,1,2,3,100])
    print("//",Jugador_13,"Ha hecho",n,"de daño a",Jugador_12,"//")
    if Jugador_2_healt>0:
        Jugador_1_Healt-=n
    n=random.choice([5,10,30,45,46,15,3,3,3,5,5,6,5,7,8,23,43,1,0,0,0,0,0,1,2,3,100])
    if Jugador_1_Healt>0:
        print("++",Jugador_12,"Ha recuperado",n,"puntos de vida ++")
    if Jugador_2_healt>0:
        Jugador_2_healt+=n
    n=random.choice([5,10,30,45,46,15,3,3,3,5,5,6,5,7,8,23,43,1,0,0,0,0,0,1,2,3,100])
    if Jugador_2_healt>0:
        print("++",Jugador_13,"Ha recuperado",n,"puntos de vida ++")
    if Jugador_1_Healt>0:
        Jugador_1_Healt-=n
    if n>0:print("!!",Jugador_12,"Tiene",Jugador_1_Healt,"de vida y",Jugador_13,"tiene",Jugador_2_healt,"de vida !!")
if Jugador_1_Healt<0:
    print(Jugador_13,"Gana con",Jugador_2_healt,"de vida")
if Jugador_2_healt<0:
    print(Jugador_12,"Gana",Jugador_1_Healt,"de vida")