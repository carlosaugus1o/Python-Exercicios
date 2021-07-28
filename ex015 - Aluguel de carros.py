dias = int(input('Qual a quantidade de dias? '))
km = float(input('Insira a quantidade de km rodados: '))
valor = (60 * dias) + (km * 0.15)
print('O valor total do aluguel do carro será de R$ {:.2f}.'.format(valor))
