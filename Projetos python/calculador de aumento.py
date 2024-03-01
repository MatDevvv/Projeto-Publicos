#calculador de porcentagem de aumento de salario
salario=int(input("digite seu salario "))
porcentagem1=0.10
porcentagem2=0.15
aumento1= (salario*porcentagem1)
aumento2=(salario*porcentagem2)
if salario>1250:
    print ("O aumento será de {}".format(aumento1))
else:
    print ("O aumento será de {}".format(aumento2))

