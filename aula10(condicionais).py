tempo = int(input('Há quantos anos você comprou o seu carro? '))
if tempo <= 3:
    print('Seu carro é novo!')
else:
    print('Seu carro é velho!')
print('--FIM--')

#print('carro novo' if tempo <= 3 else 'carro velho') <---- forma alternativa

nome = str(input('Qual é seu nome? '))
if nome == 'Carlos':
    print('Que nome fantástico!')
print('Bom dia, {}!'.format(nome))
