from random import randint

from time import sleep #faz o computador "dormir"

computador = randint(0, 5) #fa o computador "pensar"

nome = str(input('Qual o nome do jogador? '))

print('---' * 20)

print('Vou pensar em um número entre 0 e 5. Tente Adivinhar...')

print('---' * 20)

jogador = int(input('Em que número estou pensando? ')) #jogador tenta adivinhar

print('PROCESSANDO...')

sleep(3) #faz o computador "dormir"

if jogador == computador:

  print('Parabéns {}, você acertou!'.format(nome))

else:

  print('Não foi desta vez {}, tente novamente! Pensei no número {} e não no {}.'.format(nome, computador, jogador))