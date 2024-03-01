import math
cat=float(input(" digite o valor do cateto oposto "))
cat2=float(input(" digite o valor do cateto adjacente "))
hip=math.hypot(cat,cat2)
print("a hipotenusa vai medir {:.2f}".format(hip))
