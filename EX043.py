peso = float(input('Qual seu peso? '))

altura = float(input('Qual sua altura? '))

imc = peso / (altura ** 2)

print('Seu IMC é {:.1f}.'.format(imc))

if imc < 18.5:

  print('Você está ABAIXO DO PESO.')

elif imc >= 18.5 and imc < 25:

  print('Você está no PESO IDEAL.')

elif imc >= 25 and imc < 30:

  print('você está com SOBREPESO.')

elif imc >= 30 and imc <= 40:

  print('Você está com \033[31mOBESIDADE.\033[m')

else:

  print('Você tem \033[31mOBESIDADE MÓRBIDA, CUIDADO!!!\033[m')