

def header():
      print('-' * 30 + f'\n{"FATORIAL":^30}\n' + '-' * 30)


def fatorial(num, show=False):
    fato = 1
    for cont in range(num, 0, -1):
        fato *= cont
        if show:
            print(f'{cont}', end=' x ' if cont != 1 else ' = ')
    return fato


print(fatorial(10, True))  # imprimindo calculo e resultado da fatórial do valor informado
print()
print(fatorial(7))  # Imprimindo somente valor retornado pela função fatorial()
print()
help(fatorial)  # Visualizando a docstring da função fatorial()