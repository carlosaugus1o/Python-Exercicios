soma = cont = 0
while True:
    num = int(input('Digite um valor, ou 999 para parar: '))
    if num == 999:
        break
    cont += 1
    soma += num
print(f'Você digitou {cont} valores e a soma dos valores foi {soma}.')
