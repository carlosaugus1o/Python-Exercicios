maior = 0
menor = 0
for p in range(1, 7):
    peso = float(input('Digite o peso da {}º pessoa: (Kg) '.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso foi de {} Kg.'.format(maior))
print('O menor peso foi de {} Kg.'.format(menor))


