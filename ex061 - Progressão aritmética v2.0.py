print('GERADOR DE PA')
print('-=' * 20)
primeiro = int(input('Insira o primeiro termo: '))
razão = int(input('Insira a razão: '))
termo = primeiro
cont = 1
while cont <= 10:
    print(' {} → '.format(termo), end='')
    termo += razão
    cont += 1
print('FIM')
