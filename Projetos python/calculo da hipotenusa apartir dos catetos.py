cat=float(input(" digite o valor do cateto oposto "))
cat2=float(input(" digite o valor do cateto adjacente "))
pitagoras=(cat ** 2 + cat2 ** 2) ** (1/2)
hipotenusa=pitagoras
print("a hipotenusa vai medir {:.2f}".format(pitagoras))
