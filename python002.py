# DIA 2 = Tipos primitivos e saida de dados

# Anotações
'''
 int =inteiros
 float =numeros reais ou ponto flutuantes
 bool =de boleanos (True / False)
 str =caracter ou string
 print(' #string {}'.format(#o que aparece dentro do {}))
 type() retorna o tipo do valor
'''

# Cod1 <-- Aula 06
'''
n1=input('valor? ')
print(type(n1))
n2=int(input('valor2? '))
print(type(n2), 'o Valor 2 é: {}'.format(n2))
'''
# Cod 2 <-- Aula 06
''' 
n3=n1+n2  <-- isso não rola pq está somando uma string com um int  
print(n3)
print(type(n3))
'''
# Cod3 <-- Aula 06
'''
n1 = int(input("Digite um valor: "))
n2 = int(input("Digite um valor: "))
s = n1+n2
print('A soma de {} + {} é igual a: {}'.format(n1, n2, s))
'''

# Cod 4 //Importante uso do .is (teste de método)  <-- Aula 06
'''
n = input('Digite algo: ')
# varivel.is(alguma coisa) é um metodo de pergutar qual é o tipo do caractere, por exemplo: isnumeric (é um numero?)
print(n.isnumeric())
'''

# cod 5 <-- Aula 06
'''
a = input('Digite qualquer coisa: ')
#No Python 3.7, não precisa colocar o .format() no final, basta colocar "f" na frente das aspas e inserir os valores dentro dos colchetes
#O "a" seria a variavel, mas no python ele acaba virando um objeto
print(f'O tipo primitivo desse valor é {type(a)}')
print(f'Só tem espaços? {a.isspace()}')
print(f'É um número? {a.isnumeric()}')
print(f'É alfabético? {a.isalpha()}')
print(f'É alfanumérico? {a.isalnum()}')
print(f'Está em maiúsculas? {a.isupper()}')
print(f'Está em minúsculas? {a.islower()}')
print(f'Está capitalizado? {a.istitle()}')
'''
# cod 6 <-- aula 07
'''
** potencia --> pow()
// divisão inteira --> para quanddo for por o ponto
% resto da divisão 
Ordem de precedencia --> () -> ** -> *,/,//,% -> +,- 

para raiz n == 'numeroqualquerx'**(1/n)
'''

# Cod 7 <-- aula 07
'''
nome = input('Qual o seu nome? ')
print('Prazer em te conhecer {}!'.format(nome))
# utiliza 20 espaços para escrever o nome
print('Prazer em te conhecer {:20}!'.format(nome))
print('Prazer em te conhecer {:>20}!'.format(nome))  # coloca na direita
print('Prazer em te conhecer {:<20}!'.format(nome))  # coloca na esquerda
print('Prazer em te conhecer {:^20}!'.format(nome))  # centraliza
# coloca sinais de = em volta da variavel
print('Prazer em te conhecer {:=^20}!'.format(nome))
'''

# Cod 8 <-- aula 07
'''
n1 = int(input("Digite um valor: "))
n2 = int(input("Digite um valor: "))
print('A soma de {} + {} é igual a: {}'.format(n1, n2, n1+n2)) #Posso economizar uma variavel 
'''

# Cod 9 <-- aula 07
n1 = int(input("Digite um valor: "))
n2 = int(input("Digite um valor: "))
s = n1+n2
m = n1*n2
d = n1/n2
di = n1//n2
e = n1**n2

print('A soma é {}; \nO produto é: {}; \na divisão é {:.3f}'.format(s, m, d), end=';\n')
print('Divisão inteira {} e potência {}'.format(di, e))

