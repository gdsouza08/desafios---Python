nome = input('Digite seu nome completo: ')

mai = nome . upper()

print('Nome em letras maiúsculas: {}'.format(mai))



nome = str(input('Digite seu nome completo: ')).strip()

print('Analizando seu nome ...')

print('Nome em letras maiúsculas: {}'.format(nome.upper()))

nome = input('Digite seu nome completo: ')

min = nome.lower()

print('Nome em letra minúsculas: {}'.format(min))



nome = str(input('Digite seu nome completo: ')).strip()

print('Analizando seu nome ...')

print('Nome em letras maiúsculas: {}'.format(nome.upper()))

print('Nome em minúsculas: {}'.format(nome.lower()))

nome = str(input('Digite seu nome completo: ')).strip()

print('Analizando seu nome ...')

print('Nome em letras maiúsculas: {}'.format(nome.upper()))

print('Nome em minúsculas: {}'.format(nome.lower()))

print('Seu nome tem {} letras'.format(len(nome) - nome.count(' ')))

print('Seu primeiro nome é {} e tem {} letras'.format(pn[0], nome.find(' ')))



nome = str(input('Digite seu nome completo: ')).strip()

pn = nome.split()

print('Analizando seu nome ...')

print('Nome em letras maiúsculas: {}'.format(nome.upper()))

print('Nome em minúsculas: {}'.format(nome.lower()))

print('Seu nome completo tem {} letras'.format(len(nome) - nome.count(' ')))

print('Seu primeiro nome é {} e tem {} letras'.format(pn[0], len(pn[0])))
