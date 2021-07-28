from time import sleep
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
opção = 0
while opção != 5:
    print('''    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Qual o maior?
    [ 4 ] Novos números
    [ 5 ] Sair''')
    opção = int(input('Qual é sua opção? '))
    if opção == 1:
        soma = n1 + n2
        print('A soma entre {} e {} é igual a {}.'.format(n1, n2, soma))
    elif opção == 2:
        mult = n1 * n2
        print('O produto entre {} e {} é igual a {}.'.format(n1, n2, mult))
    elif opção == 3:
        if n1 > n2:
            maior = n1
            print('Entre {} e {} o maior valor é {}'.format(n1, n2, maior))
        elif n1 < n2:
            maior = n2
            print('Entre {} e {} o maior valor é {}'.format(n1, n2, maior))
        else:
            print('Os números são iguais!')
    elif opção == 4:
        print('Informe os números novamente:')
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor:'))
    elif opção == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente.')
    sleep(2)
print('Fim do programa! VOLTE SEMPRE!')