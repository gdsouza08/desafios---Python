from math import sqrt

cateto1 = float(input('Digite o valor do cateto A: '))
cateto2 = float(input('Digite o valor do cateto B: '))
hipotenusa = (cateto1 * cateto2) + (cateto1 * cateto2)

print('Valor do Cateto A: {}\nValor do Cateto B: {}\nValor da Hipotenusa {:.4f}'.format(cateto1, cateto2, sqrt(hipotenusa)))