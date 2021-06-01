n1 = int(input('Primeiro número: '))

n2 = int(input('Segundo número: '))

if n1 > n2:

  print('\033[32mO PRIMEIRO valor é maior.\033[m')

elif n1 < n2:

  print('\033[32mO SEGUNDO valor é maior.\033[m')

else:

  print('\033[31mNÃO existe valor maior, os dois são IGUAIS.\033[m')