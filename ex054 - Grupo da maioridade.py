from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pessoa in range(1, 8):
    nasc = int(input('Digite o ano que a {}º pessoa nasceu: '.format(pessoa)))
    idade = atual - nasc
    if idade >= 18:
        totmaior += 1
    else:
        totmenor += 1
print('Dessas pessoas, {} são maiores de idade e {} são menores.'.format(totmaior, totmenor))
