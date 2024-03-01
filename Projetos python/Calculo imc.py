#Calculo imc
peso=float(input("Digite sua peso "))
altura=float(input("Digite sua altura "))
imc=peso/(altura*altura)
print ("Seu imc é {:.2f}".format(imc))
if imc<18.5:
    print("Você esta abaixo do peso ideal")
elif 18.5<imc<25:
    print("Peso ideal")
elif 25<imc<30:
    print("Sobrepeso")
elif 30<imc<40:
    print("Obesidade")
elif imc>40:
    print("Obesidade morbida")
