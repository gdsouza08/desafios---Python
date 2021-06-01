from datetime import date

ano = int(input('Digite o ano de seu nascimento: '))

anoatual = date.today().year

idade = anoatual - ano

print('Sua idade atual é {} anos.'.format(idade))

if idade <= 9:

  print('\033[36mCategoria: Mirim')

elif idade <= 14:

  print('\033[33mCategoria: Infantil')

elif idade <= 19:

  print('\033[32mCategoria: Júnior')

elif idade <= 25:

  print('\033[30mCategoria: Sênior')

else:

  print('\033[31mCategoria: Master')