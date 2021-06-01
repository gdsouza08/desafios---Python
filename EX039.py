from datetime import date

print('''Diga-nos seu sexo:

[ 1 } - Feminino

[ 2 ] - Masculino''')

escolha = int(input('Qual sua opção? '))

if escolha == 1:

  print('Dispensada de alistamento, obrigatório somente para pessoas do sexo Masculino.')

else:

  nasc = int(input('Digite o nome de seu nascimento: '))

  atual = date.today().year

  idade = atual - nasc

  faltam = 18 - idade

  passado = idade - 18

  print('Sua idade é de {} anos.'.format(idade))

  if idade < 18 and faltam != 18:

    ano = atual + faltam

    print('\033[33mAinda faltam {} anos para o seu alistamento.'.format(faltam))

    print('Seu alistamento ocrrerá no ano de {}.\033[m'.format(ano))

  elif idade == 18:

    print('\033[32mATENÇÃO! Hora de se alistar!!!\033[m')

  else:

    ano = atual - passado

    print('\033[31mPassaram {} anos do seu alistamento.'.format(passado))

    print('Seu alistamento deveria ter sido feito no ano de {}.\033[m'.format(ano))