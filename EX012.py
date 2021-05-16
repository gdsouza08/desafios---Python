larg = float(input('Qual a largura da parede? '))
alt = float(input('Qual a altura da parede? '))
area = larg * alt
print("A área da sua parede é {} m²".format(area))
tinta = area / 2
print('Para pintar a parede será necessário {} litros de tinta.'.format(tinta))