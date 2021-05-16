produto = float(input('Qual o valor do produto? R$ '))
novo = produto - (produto * 5 /100)
desconto = produto * 5 /100

print('O produto que antes custava R$ {} está com 5% de desconto e custará R$ {:.2f}.\nSeu desconto foi de: R$ {:.2f}.'.format(produto, novo, desconto))