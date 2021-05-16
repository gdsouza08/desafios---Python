salario = float(input('Qual o salário atual? '))
aumento = salario * 15 / 100
novosalario = salario + aumento

print('O seu salário atual é R$ {:.2f} e com 15% de aumento passará a ser R$ {:.2f}. O aumento foi de R$ {:.2f}.'.format(salario, novosalario, aumento))