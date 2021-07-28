valores = [int(input(f'Informe o valor da posição {cont}º: ')) for cont in range(5)]
print('-' * 35)
print(f'VALORES INFORMADOS: {valores}')

print(f'\nO maior valor digitado foi: {max(valores)} nas posições: ', end='')
for indice, valor in enumerate(valores):
    if valor == max(valores):
        print(f'{indice}...', end=' ')

print(f'\nO menor valor digitado foi: {min(valores)} nas posições: ', end='')
for indice, valor in enumerate(valores):
    if valor == min(valores):
        print(f'{indice}...', end=' ')