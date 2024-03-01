#atleta
data_de_nascimento=int(input("Digite seu ano de nascimento "))
b=2023-data_de_nascimento
if b <=9:
    print("CATEGORA MIRIM")
elif b<=14:
    print("CATEGORIA INFANTIL")
elif b<=19:
    print("CATEGORIA JUNIOR")
elif b<=20:
    print("CATEGORIA SÊNIOR")
else:
    print("CATEGORIA MASTER")
print(b)