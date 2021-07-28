n = int(input('Insira um número e veja sua tabuada: '))
for c in range(1, 11, 1):
    print('{:2} x {} = {}'.format(c, n, n*c))
