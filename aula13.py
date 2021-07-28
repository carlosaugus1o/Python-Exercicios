for c in range(0, 6):
    print('Oi')

for c in range(0, 6):
    print(c)

for c in range(6, 0, -1):
    print(c)

for c in range(0, 10, 2):
    print(c)
i = int(input('Inicio='))
f = int(input("Fim="))
p = int(input('Passo='))
for c in range (i, f+1, p):
    print(c)
s = 0
for c in range(0,5):
    n = int(input('Digite um valor: '))
    s = s + n
print('O somatório dos valores é igual a {}.'.format(s))
