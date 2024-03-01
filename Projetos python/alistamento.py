#Alistamento militar
idade=int(input("Digite seu ano de nascimento "))
a= 2023 - idade
if a<18:
    print("Você ainda vai se alistar!")
    print("Faltam {} anos".format(a))
elif a==18:
    print("apresente-se ao quartel!")
elif a>18:
    print("Seu periodo de alistamento ja passou!")
    print ("Você deveria ter se alistado a {} anos".format(a))
