from random import randint
from time import sleep
from operator import itemgetter

jogadores = {}
rank = []

# Sorteando valores para dados jogados
for cont in range(1, 5):
    jogada = randint(1, 6)
    jogadores[f'jogador{cont}'] = jogada

# Imprimindo os valores tirados no dado
print('Valores sorteados:')
for chave, valor in jogadores.items():
    print(f'\tO {chave} tirou {valor}')
    sleep(0.5)

rank = sorted(jogadores.items(), key=itemgetter(1), reverse=True)

print('\nColocação dos jogadores:')
for idx, valor in enumerate(rank):
    print(f'\t{idx + 1}º lugar foi: {valor[0]} com {valor[1]} no dado.')
    sleep(0.5)