n = str(input('Insira seu nome completo: ')).strip()
nome = n.split()  #cria uma lista com os nomes
print('Muito prazer em te conhecer!')
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu último nome é {}.'.format(nome[len(nome)-1]))