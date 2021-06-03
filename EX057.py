sexo = ''

while sexo != 'M' and sexo != 'F':

  sexo = str(input('Informe seu sexo: [M/F]: ')).upper()

  if sexo != 'M' and sexo != 'F':

    print('Opção inválida! Seleciona a letra correspondente.')

if sexo == 'M':

  print('Masculino')

if sexo == 'F':

  print('Feminino')

print('O sexo escolhido foi {}'.format(sexo))



sexo = str(input('Informe seu sexo: [M/F]: ')).upper().strip()[0]

while sexo not in 'MF':

  sexo = str(input('Dados inválidos. Informe seu sexo: [M/F]: ')).upper().strip()[0]

print('Sexo {} registrado com sucessso.'.format(sexo))