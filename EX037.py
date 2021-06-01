num = int(input('Digite um número inteiro: '))

print('''Escolha uma das bases para conversão:

[ 1 ] converter para BINÁRIO

[ 2 ] converter para OCTAL

[ 3 ] converter para HEXADECIMAL''')

opcao = int(input('Sua opção: '))

if opcao == 1:

  print('\033[33mO número {} convertido para Binário resulta em {}.\033[m'.format(num, bin(num)[2:]))

elif opcao == 2:

  print('\033[32mO número {} convertido para Octal resulta em {}.\033[m'.format(num, oct(num)[2:]))

elif opcao == 3:

  print('\033[34mO número {} convertido para Hexadecimal resulta em {}.\033[m'.format(num, hex(num)[2:]))

else:

  print('\033[31mOpção inválida, tente novamente.\033[m')