print('{:=^40}'.format(' LOJAS CARLOS CAPONE S.A. '))
preço = float(input('Preço das compras: R$ '))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opção = int(input('Qual sua opção? '))
if opção == 1:
    total = preço * 0.9
elif opção == 2:
    total = preço * 0.95
elif opção == 3:
    total = preço
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R$ {:.2f}.'.format(parcela))
elif opção == 4:
    total = preço * 1.2
    numpar = int(input('Quantas parcelas? '))
    parcela = total / numpar
    print('Sua compra será parcelada em {} vezes de R$ {}.'.format(numpar, parcela))
else:
    total = preço
    print('\033[1;31mOPÇÃO INVÁLIDA. TENTE NOVAMENTE.\033[m')
print('Sua compra de R$ {:.2f} vai custar R$ {:.2f} no final'.format(preço, total))



