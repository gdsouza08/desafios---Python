from time import sleep

velocidade = int(input('Qual a velocidade do veículo? '))

if velocidade > 80:

  print('MULTADO! Você excedeu o limite de velocidade que é de 80Km/h. ')

  print('PROCESSANDO VALOR...')

  sleep(3)

  multa = (velocidade-80) * 7

  print('Você deve pagar uma multa no valor de R$ {:.2f}, por ter excedido o limite de velocidade em {}Km/h.'.format(multa, (velocidade-80)))

else:

  print('Você está dentro do limite de velocidade, Tenha um bom dia e dirija com segurança!')