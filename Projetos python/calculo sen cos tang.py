import math
angulo=float(input("digite o angulo que você deseja "))
sen=math.sin(math.radians(angulo))
cos=math.cos(math.radians(angulo))
tang=math.cos(math.radians(angulo))
print("o valor do seno é {:.2f}".format(sen))
print("o valor do cosseno é  {:.2f}".format(cos))
print("o valor da tangente é {:2f}".format(tang))
