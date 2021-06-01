casa = float(input('Qual o valor da casa: R$ '))

salario = float(input('Qual o valor do salário do comprador? R$ '))

anos = int(input('De quantos anos será o financiamento? '))

prestacao = casa / anos / 12

minimo = salario * 30 / 100

print('Para pagar um casa de R$ {:.2f} em {} anos, sua prestação será de R$ {:.2f} ao mês.'.format(casa, anos, prestacao))

emprestimo = salario * 10 / 100

if prestacao <= minimo:

  print('\033[32mEmpréstimo CONCEDIDO!\033[m')

else:

  print('\033[31mEmpréstimo NEGADO!\033[m')

print('Mínimo de 30% do salário para poder pagar a prestação é {}'.format(minimo))