import random
aluno =input(" digite o nome de um aluno ")
aluno2 =input(" digite o nome de um aluno ")
aluno3 =input(" digite o nome de um aluno ")
aluno4 =input(" digite o nome de um aluno ")
lista = [aluno,aluno2,aluno3,aluno4]
escolhido = random.choice(lista)
print("O aluno escoolhido foi {}".format(escolhido))
