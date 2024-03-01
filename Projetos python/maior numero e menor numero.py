n1 = int(input("digite um numero "))
menor=n1
maior=n1
n2=int(input("digite um numero"))
if n2>maior:
    maior=n2
n3 = int(input("digite um numero"))
if n3>maior:
    maior=n3
if n1<n2:
    menor=n1
if n2<menor:
    menor=n2
if n3<menor:
    menor=n3
print("{} é o maior".format(maior))
print("{} é o menor numero".format(menor))

