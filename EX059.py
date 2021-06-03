from time import sleep

n1 = int(input('Primeiro valor: '))

n2 = int(input('Segundo valor: '))

opcao = 0

print('-=-' * 10)

print('''O que deseja fazer: 

  [1] Somar

  [2] Multiplicar

  [3] Maior Valor

  [4] Novos Números

  [5] Sair do Programa''')

print('-=-' * 10)

while opcao != 5:

  opcao = int(input('>>>>>> Qual é a sua opção? '))

  if opcao == 1:

    soma = n1 + n2

    print('A soma entre os números resulta em {}'.format(soma))

  elif opcao == 2:

    multiplicar = n1 * n2

    print('{} x {} é {}'.format(n1, n2, multiplicar))

  elif opcao == 3:

    print('O maior dos números é {}'.format(max(n1, n2)))

  elif opcao == 4:

    novo = int(input('Digite um novo valor: '))

    novo1 = int(input('Digite um novo valor: '))

  elif opcao == 5:

    print('Fechando programa!')

    sleep(3)

    exit('Obrigado por utilizar o sistema Curso em Vídeo!!!')

  else:

    print('Opção inválida! Selecione uma das opções acima.')

