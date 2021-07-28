listaValores = []
for cont in range(5):
    valor = int(input(f'Informe o {cont + 1}º valor: '))

    # Em caso o valor já exista dentro da lista
    while valor in listaValores:
        print('~' * 52)
        print('Valor duplicado. Tente novamente...')
        valor = int(input(f'Informe o {cont + 1}º valor: '))

    # Caso seja o primeiro valor digitado ou o valor seja maior que todos contidos na lista
    if len(listaValores) == 0 or valor > max(listaValores):
        listaValores.append(valor)
        print('O valor foi adicionado na última posição da lista...')
        print('-' * 52)
        continue

    # Percorrendo a lista para verificar se o valor informado é menor que todos valores da lista
    for idx, v in enumerate(listaValores):
        if valor < v:
            listaValores.insert(idx, valor)
            print(f'O valor foi adicionado na posição {idx} da lista...')
            print('-' * 52)
            break

print(f'VALORES DA LISTA EM ORDEM CRESCENTE: {listaValores}')