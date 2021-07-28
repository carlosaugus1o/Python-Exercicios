from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''SUAS OPÇÕES: 
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
if jogador != 0 and jogador != 1 and jogador != 2:
    print('\033[1;31mJOGADA INVÁLIDA!\033[m')
else:
    sleep(1)
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO')
    sleep(0.5)
    print('-=' * 11)
    print('Computador jogou {}.'.format(itens[computador]))
    print('Jogador jogou {}.'.format(itens[jogador]))
    print('-=' * 11)
    if computador == 0:  # computador joda Pedra
        if jogador == 0:
            print('EMPATE!')
        elif jogador == 1:
            print('Jogador vence!')
        elif jogador == 2:
            print('Computador vence!')
    elif computador == 1:  # computador joga Papel
        if jogador == 0:
            print('Computador vence!')
        elif jogador == 1:
            print('EMPATE!')
        elif jogador == 2:
            print('Jogador vence!')
    elif computador == 2:  # computador joga Tesoura
        if jogador == 0:
            print('Jogador vence!')
        elif jogador == 1:
            print('Computador vence!')
        elif jogador == 2:
            print('EMPATE!')

