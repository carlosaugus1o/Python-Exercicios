import math
co = float(input('Informe o cateto oposto: '))
ca = float(input('Informe o cateto adjacente: '))
hi = math.hypot(co, ca)
print('A hipotenusa é igual a {:.2f}.'.format(hi))

#O exercício também pode ser feito pelo método matemático tradicional: (co**2 + ca**2)**(1/2) = hi