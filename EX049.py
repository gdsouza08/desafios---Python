from time import sleep

n = int(input('Digite um número inteiro qualquer para ver sua tabuada: '))

print('Gerando tabuada do {}...'.format(n))
sleep(3)

print('-'*20)

for tab in range(1, 11):

  print(n, ' x {:2} = {}'.format(tab, n * tab))

print('-'*20)