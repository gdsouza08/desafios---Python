print('---' * 10)

print('Analisador de Triângulos')

print('---' * 10)

r1 = int(input('Primeiro valor: '))

r2 = int(input('Segundo valor: '))

r3 = int(input('Terceiro valor: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:

    print('Os segmentos acima FORMAM um triângulo.')

    if r1 == r2 == r3:

        tipo = 'EQUILATERO'

        print('Todos os seus LADOS são IGUAIS, portanto é um triângulo {}.'.format(tipo))

    elif r1 == r2 or r1 == r3 or r2 == r3:

        tipo = 'ISOSCELES'

        print('O triângulo possui DOIS LADOS iguais, portanto é {}.'.format(tipo))

    else:

        tipo = 'ESCALENO'

        print('Todos os LADOS do triângulo são DIFERENTES, portanto temos um triângulo {}.'.format(tipo))

else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo')