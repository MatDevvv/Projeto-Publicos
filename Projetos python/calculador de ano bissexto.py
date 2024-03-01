#Calculador de ano bissexto
ano=int(input("Digite um ano "))
if ano % 4 ==0:
    print("o ano {} é bissexto".format(ano))
else:
    print("o ano {} não é bissexto".format(ano))
