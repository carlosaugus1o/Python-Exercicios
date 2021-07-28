velocidade = float(input('Qual a sua velocidade? '))
if velocidade > 80:
    multa = (velocidade-80) * 7
    print('Você foi MULTADO! Você irá pagar uma multa de R$ {:.2f}.'.format(multa))
else:
    print('Tenha um bom dia! Dirija com segurança.')
