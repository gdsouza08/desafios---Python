m = float(input('Digite o valor a ser conventido: '))
cm = m / 0.010
mm = m / 0.0010
km = m / 1000
dc = m / 10

print('O valor {} em m ² foi convertido em:\ncm² {}\nMilímetros {:.2f}\nKM {:.2f}\nDecímetros {:.2f}'.format(m, cm, mm, km, dc))