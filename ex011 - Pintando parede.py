l = float(input('Insira a largura da parede em metros:'))
h = float(input('Insira a altura da parede em metros:'))
a = l * h
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m².'.format(l, h, a))
tinta = a / 2
print('Para pintar sua parede você precisará de {}l de tinta.'.format(tinta))
