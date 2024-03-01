soma=[]
aluno=str(input("Digite o nome do aluno "))
while True:
  nota=int(input("Digite sua nota "))
  if nota==0:
    media = sum(soma) / len(soma)
    print("Aluno {} sua média é de {:.2f}".format(aluno,media))
    if media<6:
      print("Reprovado!")
    elif media>6:
      print("Aprovado!")
    break
  else:
    soma.append(nota)
