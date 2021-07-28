num = cont = soma = 0  # forma simples de atribuir 0 para varias variaveis
num = int(input('Digite um número: [999 para sair] '))
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um número: [999 para sair] '))  # colocando o flag depois do contador e da soma para que ele não seja somado
print('Você digitou {} números e a soma deles foi {}.'.format(cont, soma))
