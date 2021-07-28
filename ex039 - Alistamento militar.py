from datetime import date
atual = date.today().year
nasceu = int(input('Ano de nascimento: '))
idade = atual - nasceu
print('Quem nasceu em {} tem {} anos em {}.'.format(nasceu, idade, atual))
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda faltam {} anos para o alistamento.'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {}.'.format(ano))
elif idade > 18:  # como não existe quarta opcão, poderia ter usado else
    saldo = idade - 18
    print('Você deveria ter se alistado há {} anos.'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {}.'.format(ano))
