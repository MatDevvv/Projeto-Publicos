import random
nome=str(input("digite seu nome "))
a=int(input("digite um valor entre 1 e 5 "))
b=(1,2,3,4,5)
c=random.choice(b)
if a==c:
    print("Parabéns {} , Você acertou".format(nome))
else:
    print("Que pena {} ,Você errou".format(nome))
print("o numero escolhido foi {}".format(c))
