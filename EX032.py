ano = int(input('Digite o ano: '))

bi = ano % 4

if bi == 0:

    print('Ano de {} é BISSEXTO'.format(ano))

else:

    print('O ano de {} NÃO é Bissexto'.format(ano))

from datetime import date

ano = int(input('Digite o ano a ser analisado ou digite 0 para o ano atual do sistema: '))

if ano == 0:
    ano = date.today().year  # pega o ano do sistema

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:

    print('Ano de {} é BISSEXTO'.format(ano))

else:

    print('O ano de {} NÃO é Bissexto'.format(ano))