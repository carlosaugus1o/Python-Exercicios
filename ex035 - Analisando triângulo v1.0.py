# regra do triangulo = 1 segmento tem que ser menor que a soma dos outros 2
print('\033[1;31m=_\033[m'*20)
print('\033[1;31;42m### ANALISADOR DE TRIANGULOS ###\033[m')
print('\033[1;31m=_\033[m'*20)
r1 = float(input('Comprimento da reta 1: '))
r2 = float(input('Comprimento da reta 2: '))
r3 = float(input('Comprimento da reta 3: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('\033[1:33:33mEssas 3 retas formam um triângulo!!!')
else:
    print('Falhou :( Essas 3 retas NÃO formam um triângulo.')
