resp = 'S'
soma = quant = media = maior = menor = 0
while resp in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    quant += 1
    if quant == 1:  # qnd só se tem um número, o menor e o maior valor são ele mesmo
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Quer continuar? [S/N] '))
media = soma / quant
print('Você digitou {} números e a média deles foi {}.'.format(quant, media))
print('O maior valor foi {}, enquanto o menor valor foi {}.'.format(maior, menor))
