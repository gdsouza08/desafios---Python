LISTA DE DESAFIOS EM PYTHON

--- respondendo ao usuário

01 - crie um script python que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas de acordo com o valor digitado

print('=========== DESAFIO 01 ===========')

nome = input ('Qual é o seu nome? ')

print('Olá ' + nome + ', Prazer em te conhecer"')

-----------------------------------------------

--- data formatada

02 - crie um script python que leia o dia, mês e ano de nascimento de uma pessoa e mostre uma mensagem com a data formatada

print('=========== DESAFIO 02 ===========')

dia = input ('Dia = ')

mes = input ('Mês = ')

ano = input ('Ano = ')

print('Você nasceu no ' + dia + ' de' + mes + ' de' + ano + ', Certo?')

-------------------------

--- somando números

03 - crie um script python que leia dois numeros e tente mostrar a soma entre eles

print('=========== DESAFIO 03 ===========')

num1 = input ('Digite o primeiro número: ')

num2 = input ('Digite o segundo número: ')

soma = (int(num1) + int(num2))

print('A soma é: ' + str(soma))

--------------------------------------

print('=========== DESAFIO 03 ===========')

num1 = input ('Digite o primeiro número: ')

num2 = input ('Digite o segundo número: ')

soma = (int(num1) + int(num2))

print('A soma entre ', num1 , ' e ', num2, 'vale' + str(soma))

------------------------

print('=========== DESAFIO 03 ===========')

num1 = input ('Digite o primeiro número: ')

num2 = input ('Digite o segundo número: ')

soma = (int(num1) + int(num2))

print('A soma entre {} e {} vale {}'.format(num1, num2, soma))

--------------------------

--- somando números

04 - crie um programa que leia dois numeros e mostre a soma entre eles.

print('=========== DESAFIO 04 ===========')

num1 = int(input ('Digite o primeiro número: '))

num2 = int(input ('Digite o segundo número: '))

soma = num1 + num2

print('A soma entre {} e {} vale {}'.format(num1, num2, soma))

------------------

--- dissecando uma variável

05 - faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

print('=========== DESAFIO 05 ===========')

algo = input('Digite algo: ')

print(type(algo))

print('Só tem espaços? ', algo.isspace())

print('É um número? ', algo.isnumeric())

print('É alfabético? ', algo.isalpha())

print('É alfanumérico ', algo.isalnum())

print('Esta em maiúsculas? ', algo.isupper())

print('Esta em minúsculas? ', algo.islower())

print('Esta capitalizada? ', algo.istitle())

-----------------

--- sucessor e antecessor

06 - faça um programa que leia um numero inteiro e mostre na tela o seu sucessor e seu antecessor

n = int(input('Digite um número: '))

print('O número digitado foi: {}'.format(n))

print('O número anterior ao digitado é: ', n-1)

print('O número sucessor ao digitado é: ', n+1)



n = int(input('Digite um número: '))

print('O número digitado foi: {}, O número anterior ao digitado é: {}, O número sucessor ao digitado é: {}'.format(n, (n-1), (n-2)))

----------

--- dobro, triplo e raiz quadrada

07 - crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada

n = int(input('Digite um númerro: '))

dobro = n * 2

triplo = n * 3

raiz = n ** (1/2)

print('O número digitado foi: {}'.format(n))

print('O dobro do valor digitado é: {}, O triplo do valor digitado é: {}, A raiz quadrada desse valor é: {}'.format(dobro, triplo, raiz))

----------

--- média aritimética

08 - desenvolva um programa que leia as duas notas de um aluno, calcule e mostre sua média

aluno = ('Digite o nome do aluno: ')

n1 = int(input('Primeira nota: '))

n2 = int(input('Segunda nota: '))

media = (n1 + n2) * 2

print('A média do aluno {} foi de {}'.format(aluno, media))

-------------

--- conversor de medidas

09 - escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros

m = float(input('Digite um valor para ser convertido: '))

cm = m / 0.010

mm = m / 0.0010

km = m / 1000

dc = m * 10

print('Valor em m² {}\nValor em Centímetros {}\nValor em Milímetros {}\nValor em KM {}\nValor em Decímetro {}'.format(m, cm, mm, km, dc))

-----------

--- tabuada

10 - faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada

n = int(input('Digite um número inteiro qualquer: '))

n1 = n * 1

n2 = n * 2

n3 = n * 3

n4 = n * 4

n5 = n * 5

n6 = n * 6 

n7 = n * 7

n8 = n * 8

n9 = n * 9

n10 = n * 10

print('Tabuada do {}'.format(n))

print(n, ' x 1 = {}'.format(n1))

print(n, ' x 2 = {}'.format(n2))

print(n, ' x 3 = {}'.format(n3))

print(n, ' x 4 = {}'.format(n4))

print(n, ' x 5 = {}'.format(n5))

print(n, ' x 6 = {}'.format(n6))

print(n, ' x 7 = {}'.format(n7))

print(n, ' x 8 = {}'.format(n8))

print(n, ' x 9 = {}'.format(n9))

print(n, ' x 10 = {}'.format(n10))



n = int(input('Digite um número inteiro qualquer para ver sua tabuada: '))

print('-'*12)

print('Tabuada do {}'.format(n))

print(n, ' x {:2} = {}'.format(1, n*1))

print(n, ' x {:2} = {}'.format(2, n*2))

print(n, ' x {:2} = {}'.format(3, n*3))

print(n, ' x {:2} = {}'.format(4, n*4))

print(n, ' x {:2} = {}'.format(5, n*5))

print(n, ' x {:2} = {}'.format(6, n*6))

print(n, ' x {:2} = {}'.format(7, n*7))

print(n, ' x {:2} = {}'.format(8, n*8))

print(n, ' x {:2} = {}'.format(9, n*9))

print(n, ' x {:2} = {}'.format(10, n*10))

print('-'*12)

----------------

--- conversor de moedas

11 - crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos doláres ela pode comprar. considere US$ 1,00 = R$ 3,27

real = float(input('Quanto dinheiro você tem na carteira? '))

dolar = real / 3.27

print('Com R${} você pode comprar US$ {}'.format(real, dolar)) 

------------

--- pintando parede

12 - faça um programa que leia a largura e altura de parede em metros, calcule a sua area e a quantidade de tinta necessaria para pintá-la, sabendo que cada litro de tinta pinta uma area de 2m

larg = float(input('Largura da parede: '))

alt = float(input('Altura da parede: '))

area = larg * alt

print('A área da sua parede é: {}m²'.format(area))

tinta = area / 2

print('Para pintar a parede será necessário {} litros de tinta.'.format(tinta))

----------

--- calculando descontos 

13 - faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto

p = float(input('Digite o preço do produto: R$ '))

pd = p - (p * 5 / 100)

d = p * 5 / 100

print('O produto que custava {:.2f}, na promoção com 5% de desconto custará {:.2f}. E seu desconto foi de: {:.2f}.'.format(p, pd, d))

-------------

--- reajuste salarial

14 - faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento

f = input('Digite o nome do funcionário: ')

s = float(input('Qual o salário? R$ '))

sa = s + (s * 0.15)

a = s * 15 / 100

print('O salário original do funcionário {} é R$ {:.2f}, O seu salário com aumento de 15% passa a ser de: R$ {:.2f}.\nO auamento no salário foi de: R$ {:.2f}.'.format(f, s, sa, a))

--------------

--- conversor de temperaturas

15 - escreva um programa que converta uma temperatura digitada em C° e converta para °F

c = float(input('Informe a temperatura em C°: '))

f = 9 * c / 5 + 32

print('A temperatura de {}°C corresponde a {}°F!'.format(c, f))

-----------

--- aluguel de carros

16 - escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade de dias pelo qual ele foi alugado. calcule o preço a pagar sabendo que o carro custa R$ 85,00 por dia e 0,30 por km rodado.

km = float(input('Quantidade de quilometros rodados: '))

dias = int(input('Quantos dias alugado: '))

pago = (dias * 60) + (km * 0.15)

print('O equivalente ao aluguel do carro por {} dias e com {} km rodados ficará no valor de R$ {:.2f}.'. format(dias, km, pago))

-----------

--- quebrando um número

17 - crie um programa que leia um número pelo teclado e mostre na tela a sua porção inteira ex: 6.127 o numero 6.127 tem a parte inteira 6

from math import trunc

num = float(input('Digite um número flutuante: '))

print('O número digitado foi {}, e seu valor inteiro é {}'.format(num, trunc(num)))



num = float(input('Digite um valor: '))

print('O valor digitado foi {} e sua parte inteira é {}'.format(num, int(num))

-------------

--- catetos e hipotenusa

17 - faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retângulo, calcule e mostre o comprimento da hipotenusa



from math import sqrt

cateto1 = float(input('Digite o valor do cateto A: '))

cateto2 = float(input('Digite o valor do cateto B: '))

hipotenusa = (cateto1 * cateto1) + (cateto2 * cateto2)

print('Valor do Cateto A: {}\nValor do Cateto B: {}\nValor da Hipotenusa: {:.4f}'.format(cateto1, cateto2, sqrt(hipotenusa)))



cateto1 = float(input('Digite o valor do cateto A: '))

cateto2 = float(input('Digite o valor do cateto B: '))

hipotenusa = (cateto1 ** 2 + cateto2 ** 2) ** (1/2)

print('Valor do Cateto A: {}\nValor do Cateto B: {}\nValor da Hipotenusa: {:.2f}'.format(cateto1, cateto2, hipotenusa))



from math import hypot

cateto1 = float(input('Digite o valor do cateto A: '))

cateto2 = float(input('Digite o valor do cateto B: '))

hipotenusa = hypot(cateto1, cateto2)

print('Valor do Cateto A: {}\nValor do Cateto B: {}\nValor da Hipotenusa: {:.2f}'.format(cateto1, cateto2, hipotenusa))

----------

--- seno, cosseno e tangente

18 - faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo



from math import hypot

co = float(input('Digite o valor do cateto oposto: '))

ca = float(input('Digite o valor do cateto adjacente: '))

hi = hypot(co, ca)

sen = co / hi

cos = ca / hi

tg = co / ca

print('Valor do Cateto A: {}\nValor do Cateto B: {}\nValor da Hipotenusa: {:.2f}\nValor do Seno: {:.3f}\nValor do Cosseno: {:.3f}\nValor da Tangente: {:.3f}'.format(co, ca, hi, sen, cos, tg))



from math import radians, sin, cos, tan

angulo = float(input('Digite o ângulo: '))

seno = sin(radians(angulo))

cos = cos(radians(angulo))

tg = tan(radians(angulo))

print('O valor de {}° tem o:\nSeno: {:.2f}\nCosseno: {:.2f}\nTangente: {:.2f}'.format(angulo, seno, cos, tg))

--------

--- sorteando um item na lista

19 - um professor quer sortear um dos seus quatro alunos para apagar o quadro. faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido

--- utilizando modulo choice(escolha) escolhe um entre todos

from random import choice

a1 = input('Primeiro nome: ')

a2 = input('Segundo nome: ')

a3 = input('Terceiro nome: ')

a4 = input('Quarto nome: ')

lista = [a1, a2, a3, a4]

escolhido = choice(lista)

print('O escolhido para apagar o quadro foi: {}'.format(escolhido))

----

--- sorteando uma ordem na lista

20 - o mesmo professor quer sortear a ordem de apresentação dos trabalhos de alunos. faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada

--- utilizando modulo shuffle(embaralhar)embaralha os nomes

from random import shuffle

a1 = input('Primeiro nome: ')

a2 = input('Segundo nome: ')

a3 = input('Terceiro nome: ')

a4 = input('Quarto nome: ')

lista = [a1, a2, a3, a4]

shuffle(lista)

print('A ordem de apresentação do trabalho será: ')

print(lista)

----

--- tocando um MP3

21 - faça um programa em python que abra e reproduza o aúdio de um arquivo MP3

import pygame

pygame.init()

pygame.mixer.music.load("undertale.mp3")

pygame.mixer.music.play()

pygame.event.wait()

---------

