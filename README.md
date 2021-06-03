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

--- analisador de textos

22 - crie um programa que leia o nome completo de uma pessoa e mostre:

-> o nome com todas as letras maiúsculas

nome = input('Digite seu nome completo: ')

mai = nome . upper()

print('Nome em letras maiúsculas: {}'.format(mai))



nome = str(input('Digite seu nome completo: ')).strip()

print('Analizando seu nome ...')

print('Nome em letras maiúsculas: {}'.format(nome.upper()))



-> o nome com todas as letras minúsculas

nome = input('Digite seu nome completo: ')

min = nome.lower()

print('Nome em letra minúsculas: {}'.format(min))



nome = str(input('Digite seu nome completo: ')).strip()

print('Analizando seu nome ...')

print('Nome em letras maiúsculas: {}'.format(nome.upper()))

print('Nome em minúsculas: {}'.format(nome.lower()))



-> quantas letras ao todo(sem considerar espaços)



nome = str(input('Digite seu nome completo: ')).strip()

print('Analizando seu nome ...')

print('Nome em letras maiúsculas: {}'.format(nome.upper()))

print('Nome em minúsculas: {}'.format(nome.lower()))

print('Seu nome tem {} letras'.format(len(nome) - nome.count(' ')))



-> quantas letras tem o primeiro nome

print('Seu primeiro nome é {} e tem {} letras'.format(pn[0], nome.find(' ')))



nome = str(input('Digite seu nome completo: ')).strip()

pn = nome.split()

print('Analizando seu nome ...')

print('Nome em letras maiúsculas: {}'.format(nome.upper()))

print('Nome em minúsculas: {}'.format(nome.lower()))

print('Seu nome completo tem {} letras'.format(len(nome) - nome.count(' ')))

print('Seu primeiro nome é {} e tem {} letras'.format(pn[0], len(pn[0])))

----------

--- separando dígitos de um número

23 - faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digítos separados. ex: digite um número: 1283

-> unidade: 3 -> dezena: 8 -> centena: 2 -> milhar: 1

num = int(input('Digite um número entre 0 e 9999: '))

n = str(num)

print('Analisando o número {}...'.format(num))

print('Unidade: {}'.format(n[3]))

print('Dezena: {}'.format(n[2]))

print('Centena: {}'.format(n[1]))

print('Milhar: {}'.format(n[0]))



num = int(input('Digite um número entre 0 e 9999: '))

u = num // 1 % 10

d = num // 10 % 10

c = num // 100 % 10

m = num // 1000 % 10

print('Analisando o número {}...'.format(num))

print('Unidade: {}'.format(u))

print('Dezena: {}'.format(d))

print('Centena: {}'.format(c))

print('Milhar: {}'.format(m))

----------------

--- verificando as letras de um texto

24 - crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO"

cidade = str(input('Digite o nome da cidade: ')).strip().capitalize()

print('Santo' in cidade)



cidade = str(input('Digite o nome da cidade: ')).strip()

print(cidade[:5].upper() == 'SANTO')

-------------------

--- procurando uma string dentro da outra

25 - crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome

nome = str(input('Digite seu nome completo: ')).upper().strip()

print('Tem Silva nesse nome? {}'.format('SILVA' in nome))

--------------------

--- primeira e última ocorrência de uma string

26 - faça um programa que leia uma frase pelo teclado e mostre:

-> quantas vezes aparece a letra "A"

frase = str(input('Digite uma frase: ')).upper()

print('A letra "A" aparece {} vezes na frase.'.format(frase.count('A')))



-> em que posição ela aparece primeira vez

print('A letra "A" aparece pela primeira vez na posição {}'.format(frase.find('A')))



-> em que posição ela aparece a última vez

print('A última letra "A" apareceu na posição {}'.format(frase.rfind('A')+1))

--------------

--- primeiro e último nome de uma pessoa

27 - faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente ex: ana maria de souza

nome = str(input('Digite seu nome completo: ')).strip()

dividido = nome.split()

print('Prazer em te conhecer!!!')

print('Primeiro nome: {}'.format(dividido[0]))

print('Segundo nome: {}'.format(dividido[len(dividido)-1]))



-> primeiro = ana

print('Primeiro nome: {}'.format(dividido[0]))

-> segundo = souza

print('Segundo nome: {}'.format(dividido[len(dividido)-1]))

-----------------

---jogo da adivinhação v1.0

28 - escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. o programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint

from time import sleep #faz o computador "dormir"

computador = randint(0, 5) #fa o computador "pensar"

nome = str(input('Qual o nome do jogador? '))

print('---' * 20)

print('Vou pensar em um número entre 0 e 5. Tente Adivinhar...')

print('---' * 20)

jogador = int(input('Em que número estou pensando? ')) #jogador tenta adivinhar

print('PROCESSANDO...')

sleep(3) #faz o computador "dormir"

if jogador == computador:

  print('Parabéns {}, você acertou!'.format(nome))

else:

  print('Não foi desta vez {}, tente novamente! Pensei no número {} e não no {}.'.format(nome, computador, jogador))

----------------------

--- radar eletrônico

29 - escreva um programa que leia a velocidade de um carro. se ele ultrapassar 80km/h mostre uma mensagem dizendo que ele foi multado. a multa vai custar R$ 7,00 por cada km acima do limite.

from time import sleep

velocidade = int(input('Qual a velocidade do veículo? '))

if velocidade > 80:

  print('MULTADO! Você excedeu o limite de velocidade que é de 80Km/h. ')

  print('PROCESSANDO VALOR...')

  sleep(3)

  multa = (velocidade-80) * 7

  print('Você deve pagar uma multa no valor de R$ {:.2f}, por ter excedido o limite de velocidade em {}Km/h.'.format(multa, (velocidade-80)))

else:

  print('Você está dentro do limite de velocidade, Tenha um bom dia e dirija com segurança!')

---------------

--- par ou ímpar?

30 - crie um programa que leia um número inteiro e mostre se ele é para ou ímpar.

num = int(input('Digite o número qualquer: '))

result = num % 2

if result == 0:

  print('O número {} é PAR!'.format(num))

else:

  print('O número {} é ÍMPAR!'.format(num))

-------------------------

--- custo da viagem 

31 - desenvolva um programa que pergunte a distância em km. calcule o preço da passagem cobrando R$0,50 por km para viagens de até 200km e R$0,45 para viagens mais longas.

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

---------------------------

--- ano bissexto

32 - faça um programa que leia uma ano qualquer e mostre se ele é bissexto.



ano = int(input('Digite o ano: '))

bi = ano % 4

if bi == 0:

  print('Ano de {} é BISSEXTO'.format(ano))

else:

  print('O ano de {} NÃO é Bissexto'.format(ano))

  

from datetime import date

ano = int(input('Digite o ano a ser analisado ou digite 0 para o ano atual do sistema: '))

if ano == 0:

  ano = date.today().year #pega o ano do sistema

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:

  print('Ano de {} é BISSEXTO'.format(ano))

else:

  print('O ano de {} NÃO é Bissexto'.format(ano))

---------------------

--- maior e menor valor

33 - faça um programa que leia 3 números e mostre qual é o maior e qual é o menor.



a = int(input('Primeiro número: '))

b = int(input('Segundo número: '))

c = int(input('Terceiro número: '))

\# verificando o menor

menor = a

if b < a and b < c:

  menor = b

if c < a and c < b:

  menor = c

\# verificando o maior

maior = a

if b > a and b > c:

  maior = b

if c > a and c > b:

  maior = c

print('O menor número digitado foi {}'.format(menor))

print('O maior número digitado foi {}'.format(maior))

----------------

--- aumento múltiplos

34 - escreva um programa que pergunte o salario de um funcionário e calcule o valor do seu aumento. para salários superiores a R$1.250,00 calcule um aumento de 10%. para salários inferiores ou iguais, o aumento é de 15%.

from time import sleep

salario = float(input('Qual o salário? R$ '))

if salario > 1250:

  aumento = salario + (salario * 10 / 100)

  print('Aumento de 10%')

else:

  aumento = salario + (salario * 15 / 100)

  print('Aumento de 15 %')

print('PROCESSANDO FOLHA DE PAGAMENTO...')

sleep(3)

print('O seu salario de R$ {:.2f}, com o aumento passa a ser de R$ {:.2f}.'.format(salario, aumento))

--------------------

--- analisando triângulos v1.0

35 - desenvolva um programa que leia o comprimento de 3 retas e diga ao usuário se elas podem ou não formar um triângulo.

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

-----------------

--- aprovando empréstimo

36 - escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. o programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar. calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

casa = float(input('Qual o valor da casa: R$ '))

salario = float(input('Qual o valor do salário do comprador? R$ '))

anos = int(input('De quantos anos será o financiamento? '))

prestacao = casa / anos / 12

minimo = salario * 30 / 100

print('Para pagar um casa de R$ {:.2f} em {} anos, sua prestação será de R$ {:.2f} ao mês.'.format(casa, anos, prestacao))

emprestimo = salario * 10 / 100

if prestacao <= minimo:

  print('\033[32mEmpréstimo CONCEDIDO!\033[m')

else:

  print('\033[31mEmpréstimo NEGADO!\033[m')

print('Mínimo de 30% do salário para poder pagar a prestação é {}'.format(minimo))

----------------------

--- conversor de bases

37 - escreva um programa que leia um número e peça para o usuario escolher qual será a base de conversão:: 1 para binário, 2 para octal e 8 para hexadecimal.

num = int(input('Digite um número inteiro: '))

print('''Escolha uma das bases para conversão:

[ 1 ] converter para BINÁRIO

[ 2 ] converter para OCTAL

[ 3 ] converter para HEXADECIMAL''')

opcao = int(input('Sua opção: '))

if opcao == 1:

  print('\033[33mO número {} convertido para Binário resulta em {}.\033[m'.format(num, bin(num)[2:]))

elif opcao == 2:

  print('\033[32mO número {} convertido para Octal resulta em {}.\033[m'.format(num, oct(num)[2:]))

elif opcao == 3:

  print('\033[34mO número {} convertido para Hexadecimal resulta em {}.\033[m'.format(num, hex(num)[2:]))

else:

  print('\033[31mOpção inválida, tente novamente.\033[m')

---------------------

--- comparando números

38 - escreva um programa que leia dois números inteiros e compare-os, mostrando a seguinte mensagem na tela: 

\- o primeiro valor é maior

\- o segundo valor é maior

\- não existe valor maior, os dois valores são iguais

n1 = int(input('Primeiro número: '))

n2 = int(input('Segundo número: '))

if n1 > n2:

  print('\033[32mO PRIMEIRO valor é maior.\033[m')

elif n1 < n2:

  print('\033[32mO SEGUNDO valor é maior.\033[m')

else:

  print('\033[31mNÃO existe valor maior, os dois são IGUAIS.\033[m')

---------------------

--- alistamento militar

39 - faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:

-> se ele ainda vai se alistar ao serviço militar

-> se é a hora de se alistar 

-> se já passou o tempo do alistamento

seu programa também deverá mostrar o tempo que falta ou que passou do prazo.



from datetime import date

print('''Diga-nos seu sexo:

[ 1 } - Feminino

[ 2 ] - Masculino''')

escolha = int(input('Qual sua opção? '))

if escolha == 1:

  print('Dispensada de alistamento, obrigatório somente para pessoas do sexo Masculino.')

else:

  nasc = int(input('Digite o nome de seu nascimento: '))

  atual = date.today().year

  idade = atual - nasc

  faltam = 18 - idade

  passado = idade - 18

  print('Sua idade é de {} anos.'.format(idade))

  if idade < 18 and faltam != 18:

​    ano = atual + faltam

​    print('\033[33mAinda faltam {} anos para o seu alistamento.'.format(faltam))

​    print('Seu alistamento ocrrerá no ano de {}.\033[m'.format(ano))

  elif idade == 18:

​    print('\033[32mATENÇÃO! Hora de se alistar!!!\033[m')

  else:

​    ano = atual - passado

​    print('\033[31mPassaram {} anos do seu alistamento.'.format(passado))

​    print('Seu alistamento deveria ter sido feito no ano de {}.\033[m'.format(ano))

-------------

--- média dos alunos

40 - crie um programa que leia duas notas e calcule sua média, mostrando uma mensagem ao final de acordo com a média

-> média abaixo de 5.0: reprovado

-> média entre 5.0 e 6.9: recuperação

-> média 7.0 ou superior? aprovado

n1 = float(input('Primeira nota: '))

n2 = float(input('Segunda nota: '))

media = (n1 + n2) / 2

print('Média do aluno: {}'.format(media))

if media < 5:

  print('\033[31mSituação do aluno: Reprovado\033[m')

elif media >= 5 and media <= 6.9:

  print('\033[33mSituação do aluno: Recuperação\033[m')

else:

  print('\033[32mSituação do aluno: Aprovado\033[m')

------------

--- classificando atletas 

41 - a confederação nacional de natação precisa de um programa que leia o ano de nascimento da pessoa e mostre?

-> até 9 anos: mirim

-> até 14 anos: infantil

-> até 19 anos: júnior

-> até 25 anos:senior

-> acima: master

from datetime import date

ano = int(input('Digite o ano de seu nascimento: '))

anoatual = date.today().year

idade = anoatual - ano

print('Sua idade atual é {} anos.'.format(idade))

if idade <= 9:

  print('\033[36mCategoria: Mirim')

elif idade <= 14:

  print('\033[33mCategoria: Infantil')

elif idade <= 19:

  print('\033[32mCategoria: Júnior')

elif idade <= 25:

  print('\033[30mCategoria: Sênior')

else:

  print('\033[31mCategoria: Master')

-----------------------

--- analisando triângulos v 2.0

42 - reforça o desafio 35, acrescentando o recurso de mostrar que tipo de triangulo será formado:

-> equilatero: todos os lados iguais

-> isosceles: dois lados iguais 

-> escaleno: todos os lados diferentes

print('---' * 10)

print('Analisador de Triângulos')

print('---' * 10)

r1 = int(input('Primeiro valor: '))

r2 = int(input('Segundo valor: '))

r3 = int(input('Terceiro valor: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:

  print('Os segmentos acima FORMAM um triângulo.')

  if r1 == r2 == r3:

​    tipo = 'EQUILATERO'

​    print('Todos os seus LADOS são IGUAIS, portanto é um triângulo {}.'.format(tipo))

  elif r1 == r2 or r1 == r3 or r2 == r3:

​    tipo = 'ISOSCELES'

​    print('O triângulo possui DOIS LADOS iguais, portanto é {}.'.format(tipo))

  else:

​    tipo = 'ESCALENO'

​    print('Todos os LADOS do triângulo são DIFERENTES, portanto temos um triângulo {}.'.format(tipo))

else:

  

  print('Os segmentos acima NÃO PODEM FORMAR um triângulo')

----------------

--- calculando IMC

43 - desenvolva uma logica que leia o peso e altura de uma pessoa e calcule seu IMC e moostre 

-> abaixo de 18.5: abaixo do peso

-> entre 18.5 e 25: peso ideal

-> 25 até 30: sobrepeso

-> 30 até 40: obesidade

-> acima de 40: obesidade mórbida

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

-----------------------------

--- gerenciador de pagamentos

44- elabore um programa que calcule o valor a ser pago por um produto considerando o preço normal e a forma de pagamento:

\- a vista: 10% de desconto

\- a vista no cartão: 5% de desconto

\- em até 2x no cartão: preço normal

\- 3x ou mais no cartão: 20% de juros

from time import sleep

print('-=-' * 15)

print('      SUELY ARTES FLORES')

print('-=-' * 15)

pago = float(input('Valor total da compra: R$ '))

print('''forma de pagamento: 

[ 1 ] À vista

[ 2 ] Débito

[ 3 ] 2x no Crédito

[ 4 ] 3x ou mais no Crédito''')

pagamento = int(input('Selecione uma das opções: '))

if pagamento == 1:

  dinheiro = pago - (pago * 10 / 100)

  print('Valor total à pagar R$ {:.2f}'.format(dinheiro))

elif pagamento == 2:

  debito = pago - (pago * 5 / 100)

  print('Valor total à pagar R$ {:.2f}'.format(debito))

elif pagamento == 3:

  prestacao = pago / 2

  print('PROCESSANDO...')

  sleep(3)

  print('Parcelado em: 2 vezes.\nValor da prestação: R$ {:.2f}.'.format(prestacao))

  print('Valor total à pagar R$ {:.2f}'.format(pago))

elif pagamento == 4:

  vezes = int(input('Em quantas prestações? '))

  credito = pago + (pago * 20 / 100)

  prestacao = credito / vezes

  print('PROCESSANDO...')

  sleep(3)

  print('Parcelado em: {} vezes\nValor da prestação: R$ {:.2f}.'.format(vezes, prestacao))

  print('Valor total à pagar R$ {:.2f}.'.format(credito))

else:

  print('\033[31mOPÇÃO INVÁLIDA!!! Por favor selecione uma da opções acima.\033[m')

----------------------

--- GAME: jokenpo

45 - crie um programa que faça o computador jogar jokenpô com você.

from random import randint

from time import sleep



itens = ('PEDRA', 'PAPEL', 'TESOURA')

computador = randint(0, 2)

print('''SELECIONE UMA DAS OPÇÕES ABAIXO: 

[ 0 ] PEDRA

[ 1 ] PAPEL

[ 2 ] TESOURA''')

jogada = int(input('QUAL É A SUA JOGADA? '))

print('\033[33mJO\033[m')

sleep(1)

print('\033[34mKEN\033[m')

sleep(1)

print('\033[32mPO!!!\033[m')



print('-=-' * 10)

print('O jogador jogou {}'.format(itens[jogada]))

print('O computador jogou {}.'.format(itens[computador]))

print('-=-' * 10)



if computador == 0: # computador jogou PEDRA

  if jogada == 0:

​    print('JOGO EMPATOU')

  elif jogada == 1:

​    print('JOGADOR VENCEU')

  elif jogada == 2:

​    print('COMPUTADOR VENCEU')

  else:

​    print('JOGADA INVÁLIDA!')



elif computador == 1: # computador jogou PAPEL

  if jogada == 0:

​    print('COMPUTADOR VENCEU')

  elif jogada == 1:

​    print('JOGO EMPATOU')

  elif jogada == 2:

​    print('JOGADOR VENCEU')



elif computador == 2: # computador jogou TESOURA

  if jogada == 0:

​    print('JOGADOR VENCEU')

  elif jogada == 1:

​    print('COMPUTADOR VENCEU')

  elif jogada == 2:

​    print('JOGO EMPATOU')

--------

--- contagem regressiva

46 - faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos, indo de 10 até 0, com uma pausa de 1 segundo entre eles.

from time import sleep

print('Contagem regressiva ')

for c in range(10, -1, -1):

  sleep(1)

  print(c)

print('Feliz 2019!!!\nEstouro de fogos')

--------------------------

--- contagem de pares

47 - crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 150.

for c in range(2, 51, 2):

  print(c, end=' ')

print('ACABOU!')

  

for c in range(1, 51,):

  if c % 2 == 0:

​    print(c, end=' ')

print('ACABOU!!!') 

----------------------

48 - faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de 3 e que se encontram no intervalo de 1 até 500.

soma = 0

cont = 0

for n in range(1, 501, 2):

  if n % 3 == 0:

​    cont += 1

​    soma += n

print('A soma de todos os {} valores resulta em {}.'.format(cont, soma))

-----------------------

--- tabuada v2.0

49 - refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

n = int(input('Digite um número inteiro qualquer para ver sua tabuada: '))

print('Tabuada do {}'.format(n))

print('-'*12)

for tab in range(1, 11):

  print(n, ' x {:2} = {}'.format(tab, n * tab))

print('-'*12)

--------------------

--- soma dos pares 

50 - desenvolva um programa que leia seis números inteiros, e mostre a soma apenas daqueles que forem pares. se o valor for ímpar será desconsiderado.

soma = 0

cont = 0

for n in range(1, 7):

  n = int(input('Digite o {}° valor: '.format(n)))

  if n % 2 == 0:

​    soma += n

​    cont += 1

print('Dos 6 números digitados, {} são pares e a soma entre eles resulta em {}.'.format(cont, soma))

---------------

--- progressão aritmética

51 - desenvolva um programa que leia o primeiro termo de uma PA. no final mostre os 10 primeiro termos dessa progressão.

print('==' * 15)

print('  10 TERMOS DE UMA PA')

print('==' * 15)

pt = int(input('Primeiro termo: '))

r = int(input('Razão: '))

decimo = pt + (10 - 1) * r

for pa in range(pt, decimo + r, r):

  print(pa, end=' -> ')

  if r > 0:

​    tipo = '\033[33mProgressão Crescente.\033[m'

  elif r < 0:

​    tipo = '\033[32mProgressão Decrescente.\033[m'

  else:

​    tipo = '\033[34mPA constante, Todos os termos são iguais.\033[m'

print('ACABOU')

print('\n\n', tipo)

-------------

--- numeros primos

52 - faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

num = int(input('Digite um número: '))

tot = 0

for primos in range(1, num + 1):

  if num % primos == 0:

​    print('\033[33m', end='')

​    tot += 1

  else:

​    print('\033[31m', end='')

  print('{} '.format(primos), end='')

print('\n\033[mO número {} foi dividido {} vezes.'.format(num, tot))

if tot == 2:

  print('E por isso ele É PRIMO.')

else:

  print('E por isso ele NÃO É PRIMO.')

---------------

--- palíndromo

53 - crie um programa que leia uma frase e diga se ela é um palíndromo, desconsiderando os espaços. ex: apos a sopa, a sacada da casa, a torre da derrota, o lobo ama o bolo,anotaram a data da maratona.

frase = str(input('Digite uma frase: ')).strip().upper()

palavras = frase.split()

junto = ''.join(palavras)

inverso = ''

for letra in range(len(junto) - 1, -1, -1):

  inverso += junto[letra]

print('O inverso de {} é {}.'.format(junto, inverso))

if inverso == junto:

  print('Temos um palíndromo.')

else:

  print('Não temos palíndromo.')

  

frase = str(input('Digite uma frase: ')).strip().upper()

palavras = frase.split()

junto = ''.join(palavras)

inverso = (junto[::-1])

print('O inverso de {} é {}.'.format(junto, inverso))

if inverso == junto:

  print('Temos um palíndromo.')

else:

  print('Não temos palíndromo.')

----------

--- maioridade

54 - crie um programa que leia o ano de nascimento de sete pessoas. no final mostre quantas pessoas atingiram a maioridade e quantas já são maiores.

from datetime import date

atual = date.today().year

totmaior = 0

totmenor = 0

for p in range(1, 8):

  nasc = int(input('Em que ano a {}° pessoa nasceu? '.format(p)))

  idade = atual - nasc

  print('Sua idade é {} anos'.format(idade))

  if idade < 21:

​    totmenor += 1

  else:

​    totmaior += 1

print('\033[33m{} pessoas são menores de idade.\033[m'.format(totmenor))

print('\033[32m{} pessoas são maiores de idade.\033[m'.format(totmaior))

---------------------------------

--- maior e menor da sequência

55 - faça um programa que leia o peso de cinco pessoas.no final mostre qual foi o maior e o menor peso.

maior = 0

menor = 0

for p in range(1, 6):

  peso = float(input('Digite o peso da {}ª pessoa: '.format(p)))

  if p == 1:

​    maior = peso

​    menor = peso

  else:

​    if peso > maior:

​      maior = peso

​    if peso < menor:

​      menor = peso

print('\033[32mO maior peso lido foi de {}kg\033[m'.format(maior))

print('\033[33mO menor peso lido foi de {}kg\033[m'.format(menor))

--------------------------------------

--- analisador completo

56 - desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. no final mostre:

\- a média de idade.

\- qual é o nome do homem mais velho.

\- quantas mulheres tem menos de 20 anos.

somaidade = 0

mediaidade = 0

maioridadehomem = 0

nomevelho = ''

totmulher20 = 0

for c in range(1, 5):

  print('-' * 5, '{}ª PESSOA'.format(c), '-' * 5)

  nome = str(input('NOME: ')).upper()

  idade = int(input('IDADE: '))

  sexo = str(input('SEXO [M/F]: ')).upper()

  somaidade += idade

  if c == 1 and sexo in 'Mm':

​    maioridadehomem = idade

​    nomevelho = nome

  if sexo in 'Mn' and idade > maioridadehomem:

​    maioridadehomem = idade

​    nomevelho = nome

  if sexo in 'fF' and idade < 20:

​    totmulher20 += 1

mediaidade = somaidade / 4

print('A média de idade do grupo é {} anos.'.format(mediaidade))

print('O homem mais velho tem {} anos e se chama {}'.format(maioridadehomem, nomevelho))

print('Ao todo são {} mulheres com menos de 20 anos'.format(totmulher20))

---------------------------

--- validação de dados

57 - faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = ''

while sexo != 'M' and sexo != 'F':

  sexo = str(input('Informe seu sexo: [M/F]: ')).upper()

  if sexo != 'M' and sexo != 'F':

​    print('Opção inválida! Seleciona a letra correspondente.')

if sexo == 'M':

  print('Masculino')

if sexo == 'F':

  print('Feminino')

print('O sexo escolhido foi {}'.format(sexo))



sexo = str(input('Informe seu sexo: [M/F]: ')).upper().strip()[0]

while sexo not in 'MF':

  sexo = str(input('Dados inválidos. Informe seu sexo: [M/F]: ')).upper().strip()[0]

print('Sexo {} registrado com sucessso.'.format(sexo))

---------------------------------

--- jogo da adivinhação v2.0

58 - melhore o jogo do desafio 028 onde o computador vai 'pensar' em um número entre 0 e 10. só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantas tentativas foram necessárias.

from random import randint

from time import sleep #faz o computador "dormir"

computador = randint(0, 10) #fa o computador "pensar"

nome = str(input('Qual o nome do jogador? '))

tentativas = 0

print('---' * 20)

print('Vou pensar em um número entre 0 e 10. Tente Adivinhar...')

print('---' * 20)

jogador = ''#jogador tenta adivinhar

while jogador != computador:

  jogador = int(input('Em que número estou pensando? ')) # jogador tenta adivinhar

  tentativas += 1

  print('PROCESSANDO...')

  sleep(2) #faz o computador "dormir"

  if jogador == computador:

​    print('Parabéns {}, você acertou!'.format(nome))

  else:

​    if jogador < computador:

​      print('Mais... Tente novamente')

​    else:

​      print('Menos... Tente novamente')

print('Seu número de tentativas foi {}'.format(tentativas))



59 - crie um programa que leia dois valores e mostre um menu na tela:

[1] somar

[2] multiplicar

[3] maior

[4] novos números

[5] sair do programa

seu programa deverá realizar a operação solicitada em cada caso.

from time import sleep

n1 = int(input('Primeiro valor: '))

n2 = int(input('Segundo valor: '))

opcao = 0

print('-=-' * 10)

print('''O que deseja fazer: 

  [1] Somar

  [2] Multiplicar

  [3] Maior Valor

  [4] Novos Números

  [5] Sair do Programa''')

print('-=-' * 10)

while opcao != 5:

  opcao = int(input('>>>>>> Qual é a sua opção? '))

  if opcao == 1:

​    soma = n1 + n2

​    print('A soma entre os números resulta em {}'.format(soma))

  elif opcao == 2:

​    multiplicar = n1 * n2

​    print('{} x {} é {}'.format(n1, n2, multiplicar))

  elif opcao == 3:

​    print('O maior dos números é {}'.format(max(n1, n2)))

  elif opcao == 4:

​    novo = int(input('Digite um novo valor: '))

​    novo1 = int(input('Digite um novo valor: '))

  elif opcao == 5:

​    print('Fechando programa!')

​    sleep(3)

​    exit('Obrigado por utilizar o sistema Curso em Vídeo!!!')

  else:

​    print('Opção inválida! Selecione uma das opções acima.')



-- calculando fatorial

60 - faça um programa que leia um número e mostre o seu fatorial.

n = int(input("Digite um núm para ver seu fatorial: "))

c = n

f = 1

print("Calculando {}".format(n), end = "")

while(c > 0):

  print("{}".format(c), end = "")

  print(" x " if c > 1 else " = ", end = "")

  f *= c

  c -= 1

print("{}".format(f))



61 - refaça o desafio 051 lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos usando a estrutura while.



62 - melhore o desafio 061, perguntando para o usuário se ele quer mostrar mais termos. o programa encerra quando digitar 0.



63 - escreva um programa que leia um número n inteiro e mostre na tela os n primeiros elementos de uma sequência de fibonacci.



64 - crie um programa que leia vários números inteiros. o programa só deve para quando digitar 999, no final mostre quantos números foram digitados e a soma entre eles, desconsiderando o flag.



65 - crie um programa que leia vários números inteiros. no final mostre a média entre todos os valores e quem foi o maior e menor valores lidos. o pregrama deve perguntar se quer continuar ou não a digitar.
