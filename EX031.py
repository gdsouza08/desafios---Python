distancia = float(input('Qual a distância? '))

dc = distancia * 0.5

dl = distancia * 0.45

if distancia <= 200:

  print('Para a distância de {} KM, sua passagem custará o valor de R$ {:.2f}'.format(distancia, dc))

else:

  print('Para a distância de {} KM, o valor de sua passagem será de R$ {:.2f}'.format(distancia, dl))



distancia = float(input('Qual a distância? '))

preco = distancia * 0.5 if distancia <= 200 else distancia * 0.45

print('Sua viagem de {} KM, custará R$ {:.2f}'.format(distancia, preco))



distancia = float(input('Qual a distância? '))

if distancia <= 200:

  preco = distancia * 0.5

else:

  preco = distancia * 0.45

print('A viagem de {} KM, terá o valor de R$ {:.2f}'.format(distancia, preco))