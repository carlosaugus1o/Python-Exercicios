medida = float(input('Insira uma distância em metros: '))
mm = medida * 1000
cm = medida * 100
dc = medida * 10
dm = medida / 10
hm = medida / 100
km = medida / 1000
print('Essa distância equivale a: \n{:.0f} milimetros, \n{:.0f} centimetros, \n{:.0f} decimetros,'
      '\n{} decametros, \n{} hectometros \ne {} quilometros.'.format(mm, cm, dc, dm, hm, km))
