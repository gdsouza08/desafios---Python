from math import hypot
from time import sleep

co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
print('PROCESSANDO...')
sleep(2)
hi = hypot(co, ca)
sen = co / hi
cos = ca / hi
tg = co / ca

print('Valor do Cateto Oposto: {}\nValor do Cateto Adjacente: {}\nValor da Hipotenusa: {:.4f}\nValor do Seno: {:.4f}\n'
      'Valor do Coseno: {:.4f}\nValor da Tangente: {:.4f}'.format(co, ca, hi, sen, cos, tg))