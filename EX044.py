from time import sleep

print('-=-' * 15)

print('      SUELY ARTES FLORES')

print('-=-' * 15)

pago = float(input('Valor total da compra: R$ '))

print('''forma de pagamento: 

[ 1 ] À vista

[ 2 ] Débito

[ 3 ] 2x no Crédito

[ 4 ] 3x ou mais no Crédito''')

pagamento = int(input('Selecione uma das opções: '))

if pagamento == 1:

  dinheiro = pago - (pago * 10 / 100)

  print('Valor total à pagar R$ {:.2f}'.format(dinheiro))

elif pagamento == 2:

  debito = pago - (pago * 5 / 100)

  print('Valor total à pagar R$ {:.2f}'.format(debito))

elif pagamento == 3:

  prestacao = pago / 2

  print('PROCESSANDO...')

  sleep(3)

  print('Parcelado em: 2 vezes.\nValor da prestação: R$ {:.2f}.'.format(prestacao))

  print('Valor total à pagar R$ {:.2f}'.format(pago))

elif pagamento == 4:

  vezes = int(input('Em quantas prestações? '))

  credito = pago + (pago * 20 / 100)

  prestacao = credito / vezes

  print('PROCESSANDO...')

  sleep(3)

  print('Parcelado em: {} vezes\nValor da prestação: R$ {:.2f}.'.format(vezes, prestacao))

  print('Valor total à pagar R$ {:.2f}.'.format(credito))

else:

  print('\033[31mOPÇÃO INVÁLIDA!!! Por favor selecione uma da opções acima.\033[m')