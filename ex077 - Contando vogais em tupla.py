# Tupla com todas palavras
palavras = ('carro', 'programar', 'futuro', 'mercado', 'desenvolvimento',
            'ferrari', 'miami', 'brasil', 'python', 'javascript', 'bike',
            'piscina', 'avenida', 'paralelepipedo', 'navio', 'morte')

# Tupla com todas vogais
vogais = ('a', 'e', 'i', 'o', 'u')


print()

# Descobrindo as vogais de cada palavra
for palavra in palavras:  # Pegando as palavras da tupla uma a uma
    print(f'A palavra \33[35m{palavra.upper()}\33[m tem as vogais: ', end='')
    for letra in palavra:  # Pegando a letra da palavra da tupla
        for vogal in vogais:  # Pegando uma letra da tupla vogais
            if vogal == letra:  # Verificando se a vogal é igual a letra da palavra
                print(f'\33[34m{vogal}\33[m', end=' ')
    print()