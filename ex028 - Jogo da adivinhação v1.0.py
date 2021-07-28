from random import randint
from time import sleep
computador = randint(0, 5)
print('\033[1:33:33m-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar!')
print('-=-' * 20)
jogador = int(input('\033[mEm que número eu pensei? '))
print('PENSANDO...')
sleep(3)
if jogador == computador:
    print('Parabéns! Você acertou!')
else:
    print('Errou! Eu pensei no número {} e não {}!'.format(computador, jogador))


