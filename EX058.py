from random import randint

from time import sleep #faz o computador "dormir"

computador = randint(0, 10) #fa o computador "pensar"

nome = str(input('Qual o nome do jogador? '))

tentativas = 0

print('---' * 20)

print('Vou pensar em um número entre 0 e 10. Tente Adivinhar...')

print('---' * 20)

jogador = ''#jogador tenta adivinhar

while jogador != computador:

  jogador = int(input('Em que número estou pensando? ')) # jogador tenta adivinhar

  tentativas += 1

  print('PROCESSANDO...')

  sleep(2) #faz o computador "dormir"

  if jogador == computador:

    print('Parabéns {}, você acertou!'.format(nome))

  else:

    if jogador < computador:

      print('Mais... Tente novamente')

    else:

      print('Menos... Tente novamente')

print('Seu número de tentativas foi {}'.format(tentativas))