soma = 0

cont = 0

for n in range(1, 7):

  n = int(input('Digite o {}° valor: '.format(n)))

  if n % 2 == 0:

    soma += n

    cont += 1

print('Dos 6 números digitados, {} são pares e a soma entre eles resulta em {}.'.format(cont, soma))