#possiblidade de existencia de um triangulo
l1=int(input("Digite o lado 1 "))
l2=int(input("Digite o lado 2 "))
l3=int(input("Digite o lado 3 "))
if l1+l2<=l3:
    print("esse triangulo não pode existir")
elif l2+l3<=l1:
    print("esse triangulo não pode existir")
elif l3+l1<=l2:
    print("esse triangulo não pode existir")
else:
    print("esse triangulo pode existir")
