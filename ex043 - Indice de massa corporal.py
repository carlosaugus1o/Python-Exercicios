peso = float(input('Digite seu peso: (Kg) '))
altura = float(input('Digite sua altura: '))
imc = peso / (altura ** 2)
print('O IMC dessa pessoa é de {:.1f}.'.format(imc))
if imc < 18.5:
    print('Essa pessoa está abaixo do peso ideal.')
elif imc < 25:
    print('Essa pessoa está no peso ideal!')
elif imc < 30:
    print('Essa pessoa está com sobrepeso.')
elif imc < 40:
    print('Essa pessoa está obesa.')
else:
    print('Essa pessoa está com obesidade mórbida.')


