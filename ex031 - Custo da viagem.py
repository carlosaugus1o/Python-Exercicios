distancia = float(input('Qual a distancia da viagem? '))
print('\033[1:33:33mVocê está prestes a começar uma viagem de {} Km.'.format(distancia))
if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
print('\033[mO preço da sua passagem será de R$ {:.2f}.'.format(preco))
