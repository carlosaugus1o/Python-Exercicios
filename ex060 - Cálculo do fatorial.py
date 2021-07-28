from time import sleep
n = int(input('Digite um número para calcular seu fatorial: '))
c = n
f = 1
print('Calculando {}!'.format(n))
sleep(1)
while c > 0:
    print('{}'.format(c), end=" ")
    print(' x ' if c > 1 else ' = ', end=' ')
    f *= c  # a cada ciclo o produto do ciclo anterior se multiplica pelo c diminuido de 1
    c -= 1  # a cada ciclo c se diminui por 1
print('{}'.format(f))
# é possível usar a função factorial da biblioteca math