from random import randint

from time import sleep



itens = ('PEDRA', 'PAPEL', 'TESOURA')

computador = randint(0, 2)

print('''SELECIONE UMA DAS OPÇÕES ABAIXO: 

[ 0 ] PEDRA

[ 1 ] PAPEL

[ 2 ] TESOURA''')

jogada = int(input('QUAL É A SUA JOGADA? '))

print('\033[33mJO\033[m')

sleep(1)

print('\033[34mKEN\033[m')

sleep(1)

print('\033[32mPO!!!\033[m')



print('-=-' * 10)

print('O jogador jogou {}'.format(itens[jogada]))

print('O computador jogou {}.'.format(itens[computador]))

print('-=-' * 10)



if computador == 0: # computador jogou PEDRA

  if jogada == 0:

    print('JOGO EMPATOU')

  elif jogada == 1:

    print('JOGADOR VENCEU')

  elif jogada == 2:

    print('COMPUTADOR VENCEU')

  else:

    print('JOGADA INVÁLIDA!')



elif computador == 1: # computador jogou PAPEL

  if jogada == 0:

    print('COMPUTADOR VENCEU')

  elif jogada == 1:

    print('JOGO EMPATOU')

  elif jogada == 2:

    print('JOGADOR VENCEU')


elif computador == 2: # computador jogou TESOURA

  if jogada == 0:

    print('JOGADOR VENCEU')

  elif jogada == 1:

    print('COMPUTADOR VENCEU')

  elif jogada == 2:

    print('JOGO EMPATOU')