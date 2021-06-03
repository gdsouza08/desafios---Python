num = int(input('Digite um número: '))

tot = 0

for primos in range(1, num + 1):

  if num % primos == 0:

    print('\033[33m', end='')

    tot += 1

  else:

    print('\033[31m', end='')

  print('{} '.format(primos), end='')

print('\n\033[mO número {} foi dividido {} vezes.'.format(num, tot))

if tot == 2:

  print('E por isso ele É PRIMO.')

else:

  print('E por isso ele NÃO É PRIMO.')