num = int(input('Digite um número de 1 a 9999: '))
u = num // 1 % 10 #divide por 10 e exibe o resto inteiro da divisão
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Desmembrando o número...')
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))

"""Fazendo com string: apenas se faz o endereçamento pela posição de cada digito na string
num = int(input('Digite um número de 1 a 9999: '))
n = str(num)
print('Desmembrando o número...')
print('Unidade: {}'.format(n[3]))
print('Dezena: {}'.format(n[2]))
print('Centena: {}'.format(n[1]))
print('Milhar: {}'.format(n[0]))"""
