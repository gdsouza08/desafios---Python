somaidade = 0

mediaidade = 0

maioridadehomem = 0

nomevelho = ''

totmulher20 = 0

for c in range(1, 5):

  print('-' * 5, '{}ª PESSOA'.format(c), '-' * 5)

  nome = str(input('NOME: ')).upper()

  idade = int(input('IDADE: '))

  sexo = str(input('SEXO [M/F]: ')).upper()

  somaidade += idade

  if c == 1 and sexo in 'Mm':

    maioridadehomem = idade

    nomevelho = nome

  if sexo in 'Mn' and idade > maioridadehomem:

    maioridadehomem = idade

    nomevelho = nome

  if sexo in 'fF' and idade < 20:

    totmulher20 += 1

mediaidade = somaidade / 4

print('A média de idade do grupo é {} anos.'.format(mediaidade))

print('O homem mais velho tem {} anos e se chama {}'.format(maioridadehomem, nomevelho))

print('Ao todo são {} mulheres com menos de 20 anos'.format(totmulher20))