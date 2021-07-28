soma = 0
conta = 0
for c in range(3, 500, 2):
    if c % 3 == 0:
        print(c)
        soma = soma + c
        conta += 1  # o simbolo de += é usado para significar conta = conta + 1
print('O somatório dos {} números é igual a {}.'.format(conta, soma))


