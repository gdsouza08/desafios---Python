print('==' * 15)

print('  10 TERMOS DE UMA PA')

print('==' * 15)

pt = int(input('Primeiro termo: '))

r = int(input('Razão: '))

decimo = pt + (10 - 1) * r

for pa in range(pt, decimo + r, r):

  print(pa, end=' -> ')

  if r > 0:

    tipo = '\033[33mProgressão Crescente.\033[m'

  elif r < 0:

    tipo = '\033[32mProgressão Decrescente.\033[m'

  else:

    tipo = '\033[34mPA constante, Todos os termos são iguais.\033[m'

print('ACABOU')

print('\n\n', tipo)

