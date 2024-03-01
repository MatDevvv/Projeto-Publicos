distancia=float(input("Digite a distância da viagem "))
maior= distancia * 0.50
menor= distancia * 0.45
if distancia >200:
    print("o valor a ser pago é R${}",format(maior))
else :
    print("o valor a ser pago é R${}".format(menor))
