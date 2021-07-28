from math import trunc
num = float(input('Digite um número real: '))
print('O número digitado é {} e sua porção inteira é {}.'.format(num, trunc(num)))

## o mesmo pode ser feito usando uma função interna da seguinte forma: .format(num, int(num))