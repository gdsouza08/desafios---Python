from time import  sleep

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
opcao = 0
while opcao != 1 | opcao != 2 | opcao != 3 | opcao != 4 | opcao != 5:
    mensagem = print('Escolha a operação a ser realizada:'
                     '\n[1] para adição'
                     '\n[2] para subtração'
                     '\n[3] para multiplicação'
                     '\n[4] para divisão'
                     '\n[5] para sair')
    opcao = int(input('Sua opção: '))
if opcao == 1:
    print(f"Operação: {n1} + {n2} = {n1 + n2}")
elif opcao == 2:
    print(f"Operação: {n1} - {n2} = {n1 - n2}")
elif opcao == 3:
    print(f"Operação: {n1} * {n2} = {n1 * n2}")
elif opcao == 4:
    print(f"Operação: {n1} / {n2} = {n1 / n2}")
elif opcao == 5:
    print('Fechando o programa...')
    sleep(3)
    exit('Obrigado por utilizar a Calculadora!')
else:
    print('OPÇÃO INVÁLIDA, TENTE NOVAMENTE.')


