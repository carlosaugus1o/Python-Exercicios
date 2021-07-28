soma = 0
cont = 0
for c in range(1, 7, 1):
    num = int(input('Digite o {}º valor: '.format(c)))
    if num % 2 == 0:
        soma += num
        cont += 1
if cont == 1:  # improviso para mudar entre singular e plural
    print('A soma do valor PAR é igual a {}.'.format(soma))
else:
    print('A soma dos {} valores PARES é igual a {}.'.format(cont, soma))
