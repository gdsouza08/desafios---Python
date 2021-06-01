from time import sleep

salario = float(input('Qual o salário? R$ '))

if salario > 1250:

  aumento = salario + (salario * 10 / 100)

  print('Aumento de 10%')

else:

  aumento = salario + (salario * 15 / 100)

  print('Aumento de 15 %')

print('PROCESSANDO FOLHA DE PAGAMENTO...')

sleep(3)

print('O seu salario de R$ {:.2f}, com o aumento passa a ser de R$ {:.2f}.'.format(salario, aumento))