import random
n= random.randint(2,100000)
print(n)
a=2
b=0
while a<n:
    if n%a==0:
        print("No es primo")
        b=1
        break
    a=a+1
if b==0:
    print("Es primo")

import random
p= random.randint(2,100000)
print(p)
a=2
b=0
while a<p:
    if p%a==0:
        print("No es primo")
        b=1
        break
    a=a+1
if b==0:
    print("Es primo")