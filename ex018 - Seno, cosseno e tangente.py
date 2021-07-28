from math import radians, sin, cos, tan
angulo = float(input('Informe o ângulo desejado: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print('O ângulo informado possuí:\n Seno igual a {:.2f};\n Cosseno igual a {:.2f};\n Tangente igual a {:.2f}'
      .format(seno, cosseno, tangente))

#As funções sin, cos e tan só aceitam os angulos em radianos, então é preciso usar a função radians para fazer a
#conversão
#Como apenas as funções necessárias foram importadas, não é preciso fazer a referencia .math