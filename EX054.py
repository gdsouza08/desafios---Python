from datetime import date

atual = date.today().year

totmaior = 0

totmenor = 0

for p in range(1, 8):

  nasc = int(input('Em que ano a {}° pessoa nasceu? '.format(p)))

  idade = atual - nasc

  print('Sua idade é {} anos'.format(idade))

  if idade < 21:

    totmenor += 1

  else:

    totmaior += 1

print('\033[33m{} pessoas são menores de idade.\033[m'.format(totmenor))

print('\033[32m{} pessoas são maiores de idade.\033[m'.format(totmaior))