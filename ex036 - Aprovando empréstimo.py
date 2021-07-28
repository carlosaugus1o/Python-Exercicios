casa = float(input('Qual o valor da casa? R$ '))
salario = float(input('Qual o salário do comprador? R$ '))
anos = int(input('Em quantos anos será feito o pagamento? '))
prestacao = casa / (anos * 12)
minimo = salario * 0.3
print('O valor da casa é de R$ {:.2f} e a prestação mensal será de R$ {:.2f}.'.format(casa, prestacao))
if prestacao > minimo:
    print('Seu financiamento foi \033[1;31mNEGADO\033[m, pois o valor da prestação excede 30% da sua renda.')
else:
    print('Empréstimo \033[1;36mCONCEDIDO!\033[m')

