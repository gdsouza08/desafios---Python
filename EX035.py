print('---' * 10)

print('Analisador de Triângulos')

print('---' * 10)

r1 = int(input('Primeiro valor: '))

r2 = int(input('Segundo valor: '))

r3 = int(input('Terceiro valor: '))

if r1 < r2 + 3 and r2 < r1 + r3 and r3 < r1 + r2:

  print('Os segmentos acima FORMAM um triângulo')

else:

  print('Os segmentos acima NÃO PODEM FORMAR um triângulo')