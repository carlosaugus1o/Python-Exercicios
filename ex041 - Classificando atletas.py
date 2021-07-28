from datetime import date
atual = date.today().year
nasceu = int(input('Qual a data de nascimento? '))
idade = atual - nasceu
print('O aluno tem {} anos.'.format(idade))
if idade <= 9:
    print('Classificação: MIRIM')
elif idade <= 14:
    print('Classificação: INFANTIL')
elif idade <= 19:
    print('Classificação: JUNIOR')
elif idade <= 25:
    print('Classificação: SENIOR')
else:
    print('Classificação: MASTER')

