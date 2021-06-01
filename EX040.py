n1 = float(input('Primeira nota: '))

n2 = float(input('Segunda nota: '))

media = (n1 + n2) / 2

print('Média do aluno: {}'.format(media))

if media < 5:

  print('\033[31mSituação do aluno: Reprovado\033[m')

elif media >= 5 and media <= 6.9:

  print('\033[33mSituação do aluno: Recuperação\033[m')

else:

  print('\033[32mSituação do aluno: Aprovado\033[m')