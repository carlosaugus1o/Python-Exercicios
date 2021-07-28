listaValores = []
contador = 1
print('-' * 35 + f'\n{"CADASTRO DE VALORES":^35}')
while True:
    print('-' * 35)
    valor = int(input(f'Informe o {contador}º valor: '))

    while valor in listaValores:
        print('~' * 44)
        print('Valor duplicado. Não é possível adicionar...')
        valor = int(input(f'Informe o {contador}º valor: '))
    else:
        listaValores.append(valor)

    print('-' * 35)
    op = input('Novo valor ? [S/N]: ').strip().upper()

    while op not in ('S', 'N'):
        print('~' * 35)
        print('Informe a opção corretamente...')
        op = input('Novo valor ? [S/N]: ').strip().upper()
    if op == 'N':
        break

    contador += 1

listaValores.sort()
print('-' * 35)
print(f'\nVALORES DIGITADOS: {listaValores}')