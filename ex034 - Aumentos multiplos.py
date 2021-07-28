salário = float(input('Informe o salário do funcionário: R$ '))
if salário < 1250:
    aumento = salário * 1.15
else:
    aumento = salário * 1.1
print('O novo salário do funcionário será de {:.2f}'.format(aumento))
