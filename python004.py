# Dia 4 -- Utilizando Modulos
import math
import random
import pygame

# Cod 1 -- Anotações
'''
import math 
from math import sqrt
ceil ##arredonda pra cima
floor ##aredonda para baixo 
trunc ##elimina da virgula pra frente
pow ##potencia
sqrt ## raiz 
factorial ##calculo de fatorial
lista=[numero1 ou string1, numero2 ou string2.....]
'''

# Cod 2 -- Aula 08
'''
import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print(f'A raiz de {num} é igual a {math.ceil(raiz)}!')
'''

# Cod 3 -- Aula 08
'''
from math import sqrt, florr, ceil
um = int(input('Digite um número: '))
raiz = math.sqrt(num)
print(f'A raiz de {num} é igual a {math.ceil(raiz)}!')
'''

# Cod 4 -- Aula 08
'''
import random
num=random.randint(1,99) #gera um numero aleatorio de 1 a 99
import emoji
print(emoji.emojize("Ola, mundo :earth_americas: ", use_aliases=True))
'''

# Cod 5 -- Desafio 16 Parte inteira 
##Aqui eu poderia ter usado o math.trunc(numero) para pegar a parte inteira

'''
numero=float(input('Digite um número qualquer, pertencente aos reais: '))
print(f'O número {numero} tem como parte real {math.floor(numero)}')
'''

# Cod 6 -- Desafio 17 hipotenusa 
##Poderia ter utilizado a função math.hypot(x,y)

'''
catOposto = float(input('Forneça o cateto Oposto: \n'))
catAdjacente = float(input('Forneça o cateto Adjacente: \n'))
hipotenusa = math.sqrt(math.pow(catAdjacente, 2)+math.pow(catOposto, 2))
print(
    f'A hipotenusa a partir do cateto oposto {catOposto:.0f} e do cateto adjacente {catAdjacente:.0f} é {hipotenusa:.0f}')
'''

# Cod 7 -- Desafio 18 angulos
'''
ang = float(input('Forneça o angulo: (em graus)\n'))

##ja existe essa função no python, chama math.radians(angulo)
def converterGrausParaRad(numero):
    rad = (numero/180)*math.pi
    return rad


angEmRad = converterGrausParaRad(ang)

print(f'O seno é {math.sin(angEmRad):.2f}, o cosseno é {math.cos(angEmRad):.2f} e a tangente é: {math.tan(angEmRad)}!')
'''

# Cod 8 -- Desafio 19 professor
#poderia usar o random.choice(lista)
'''
aluno01 = str(input('Digite o nome do primeiro aluno! \n'))
aluno02 = str(input('Digite o nome do segundo aluno! \n'))
aluno03 = str(input('Digite o nome do terceiro aluno! \n'))
aluno04 = str(input('Digite o nome do quarto aluno! \n'))

sorteio = random.randint(1, 4)
print('-'*23)
print('Numero - Nome do Aluno')
print('-'*23)
print(f' 01 - {aluno01} \n 02 - {aluno02} \n 03 - {aluno03} \n 04 - {aluno04}')
print('-'*23)
print(f'A partir dos nomes listados, vamos sortear o aluno para apagar o quadro', end=". E ")
if sorteio == 1:
    print(f'o aluno sorteado foi o aluno {aluno01}!\n')
if sorteio == 2:
    print(f'o aluno sorteado foi o aluno {aluno02}!\n')
if sorteio == 3:
    print(f'o aluno sorteado foi o aluno {aluno03}!\n')
if sorteio == 4:
    print(f'o aluno sorteado foi o aluno {aluno04}!\n')
'''

#Cod 9 -- Desafio 20 professor cuzao
#posso usar o random.shuffle(lista) <-embaralha a lista

'''
aluno01 = str(input('Digite o nome do primeiro aluno! \n'))
aluno02 = str(input('Digite o nome do segundo aluno! \n'))
aluno03 = str(input('Digite o nome do terceiro aluno! \n'))
aluno04 = str(input('Digite o nome do quarto aluno! \n'))


print('-'*23)
print('Numero - Nome do Aluno')
print('-'*23)
print(f' 01 - {aluno01} \n 02 - {aluno02} \n 03 - {aluno03} \n 04 - {aluno04}')
print('-'*23)
print(f'A partir dos nomes listados, vamos sortear a ordem de apresentação dos alunos', end=". E ")

print(f'a orde de apresentação dos alunos é: {random.sample([aluno01,aluno02,aluno03,aluno04], k = 4)}') #radom.sample = sorteia a ordem de um numero de uma string
'''

# Cod 10 -- Desafio 21 musica mp3
#Não funcionou, mas fiquei com preguiça de procurar a solução

'''
pygame.init()
pygame.mixer.music.load('musga.mp3')
pygame.mixer.music.play()
pygame.mixer.music.wait()
'''



