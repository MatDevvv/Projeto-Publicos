nota_1=int(input("digite a primeira nota "))
nota_2=int(input("digite a segunda nota "))
nota_3=int(input("digite a terceira nota "))
soma=(nota_1 + nota_2 + nota_3)
media=soma/3
if (media>6):
    print("Sua nota é {} Parabéns,você foi aprovado".format(media))
elif(media<6):
    print("sua nota é {},Que pena, você foi reprovado".format(media))
