import time

dias = int(input('Quantidade de dias que o carro ficou alugado: '))
km = float(input('Quantidade de KM rodados: '))
preco = (dias * 85) + (km * 0.30)

print('O carro foi alugado por: {} dias.\nEm {} dias o veículo percorreu {} KM.'.format(dias, dias, km))
print('PROCESSANDO...')
time.sleep(3)
print('TOTAL À PAGAR: R$ {}'.format(preco))
