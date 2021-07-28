sexo = str(input('Informe o seu sexo: ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()[0]
print('O sexo {} foi registrado com sucesso!'.format(sexo))
