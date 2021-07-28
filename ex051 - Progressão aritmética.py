primeiro = int(input('Digite o primeiro termo: '))
razão = int(input('Digite a razão: '))
décimo = primeiro + (10 - 1) * razão
for c in range(primeiro, décimo, razão):
    print('{}'.format(c), end=' => ')
print('CONCLUIDO')