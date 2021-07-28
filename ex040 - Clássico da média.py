n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
print('Com as notas {} e {} a média do aluno será {:.2f}.'.format(n1, n2, media))
if media >= 5 and media < 7:
    print('O aluno está em recuperação.')
elif media < 5:
    print('O aluno está \033[1;31mREPROVADO.\033[m')
else:
    print('O aluno está aprovado.')
