# DIA 3 = Desafios

# Cod 1 -- Atividade 5
'''
n1 = int(input('Digite um número: '))
print('Analisando o valor {}, seu antecessor é {} e seu sucessor é {}'.format(
    n1, (n1-1), (n1+1)))
'''

# Cod 2 -- Atividade 6
'''
n1 = int(input('Digite um número: '))
print('O dobro de {} é {} \nO triplo de {} é {} \nA raiz quadrada de {} é {:.2f}.'.format(
    n1, (n1*2), n1, (n1*3), n1, (n1**(1/2))))
'''

# Cod 3 -- Atividade 6 // so que escrita de outra forma
'''
n = int(input('Digite um número: '))
print(
    f'O dobro de {n} é {n*2}.\nO triplo é {n*3}\nA raiz quadrada é {n**(1/2):.2f}.')
'''

# Cod 4 -- Atividade 7
'''
n = float(input('Qual foi a primeira nota do aluno? '))
n2 = float(input('Qual foi a segunda nota do aluno? '))
print(f'A média entre {n} e {n2} é {(n+n2)/2:.1f}')
'''

# Cod 5 -- Atividade 8
'''
distancia = float(input('Digite uma dinstância em metros: '))
print(f'{(distancia*1000):.2f}Km \n{(distancia*100):.2f}hm \n{(distancia*10):.2f}dam \n{(distancia/10):.2f}dm \n{(distancia/100):.2f}cm \n{(distancia/1000)}mm \nDaledeledole')
'''

# Cod 6 -- Atividade 9
'''
t = int(input('Digite um numero para ver sua tabuada: '))
print('----------------')
print(f'{t*1} = {t} x 1 \n{t*2} = {t} x 2 \n{t*3} = {t} x 3 \n{t*4} = {t} x 4 \n{t*5} = {t} x 5 \n{t*6} = {t} x 6 \n{t*7} = {t} x 7\n{t*8} = {t} x 8 \n{t*9} = {t} x 9 \n{t*10} = {t} x 10')
print('----------------')
'''

# Cod 7 -- Atividade 10
'''
c = float(input('Quanto dinheiro você tem na carteira? R$'))
print(f'Com {c} você pode comprar U${(c/5.59):.2f}')
'''

# Cod 8 -- Atividade 11 // Cada 2m² de parede precisa de 1L de tinta para ser pintado
'''
l = float(input('Qual a largura da parede: '))
a = float(input('Qual a altura da parede: '))
area = l*a
tinta = (area/2)
tintaresto = (area % 2)
# Arredonda o numero pra cima, round(tinta - 0.5) arredonda pra baixo
tinta2 = round(tinta + 0.5)
price = 47.50
orcamento = 0
print(
    f'Sua parede tem a dimensão de {l}x{a} e sua área é de {area:.2f}m².')
if tintaresto == 0:
    print(f'Para pintar essa parede, você precisará de {tinta:.0f}L')
    orcamento = price*tinta
else:
    print(f'Para pintar essa parede, você precisará de {tinta2:.0f}L')
    orcamento = price*tinta2

venda = input(
    'O(A) senhor(a) deseja realizar o orçamento do valor da tinta? S/N\n')
if venda == 'S' or venda == 's':  # lemprar de sempre por a variável dps do operador lógico
    # or = operador lógico para ou
    print(f'O orçamento da sua tinta ficará de R${orcamento}!')

print('Obrigado, volte sempre!')
'''

# Cod 9 -- Atividade 12
'''
price = float(input('Qual é o preço do produto? \nR$'))
desc = float(input('Quanto de desconto deseja aplicar? (em porcentagem % ) \n'))
valorDoDesc = (desc/100)*price
newPrice = price-valorDoDesc

print(
    f'O produto que antes custava R${price:.2f}, agora, com o desconto de {desc:.0f}%, custa: R${newPrice:.2f}')
'''

# Cod 9 -- Atividade 13 //desafio
'''
parcelas = 0
samsung = 1999.99
apple = 12999.99
motorola = 1599.99


def qualpreco(n):
    preco = 0

    if n == 1:
        x = samsung

    if n == 2:
        x = apple

    if n == 3:
        x = motorola

    pagamento = str(input(
        'Qual o método que você deseja realizar o pagamento: "A vista" ou "A prazo"? (Responda com "vista ou prazo"\n'))

    if pagamento == 'vista':
        preco = x-((10/100)*x)
        print(f'O valor do produto para pagamento a vista é de: R${preco:.2f}')
    if pagamento == 'prazo':
        parcelas = int(
            input('Em quantas parcelas você deseja pagar o produto? (Até 5x)\n'))
        if parcelas == 1:
            preco = x-((10/100)*x)
            print(
                f'\nO valor do produto para pagamento a prazo, porém em 1x é de: R${preco:.2f}')

        if parcelas == 2:
            preco = x+((2.5/100)*x)
            if n == 2:
                print(
                    f'\nO preço final do produto vai ser de R${preco:.2f}, sendo que, cada parcela será de R${preco/2:.2f}. Boa sorte comprando um celular com preço de Celta!')
            else:
                print(
                    f'\nO preço final do produto vai ser de R${preco:.2f}, sendo que, cada parcela será de R${preco/2:.2f}. Boas compras!')

        if parcelas == 3:
            preco = x+((3.5/100)*x)
            if n == 2:
                print(
                    f'\nO preço final do produto vai ser de R${preco:.2f}, sendo que, cada parcela será de R${preco/3:.2f}. Boa sorte comprando um celular com preço de Celta!')
            else:
                print(
                    f'\nO preço final do produto vai ser de R${preco:.2f}, sendo que, cada parcela será de R${preco/3:.2f}. Boas compras!')

        if parcelas == 4:
            preco = x+((4.5/100)*x)
            if n == 2:
                print(
                    f'\n O preço final do produto vai ser de R${preco:.2f}, sendo que, cada parcela será de R${preco/4:.2f}. Boa sorte comprando um celular com preço de Celta!')
            else:
                print(
                    f'\nO preço final do produto vai ser de R${preco:.2f}, sendo que, cada parcela será de R${preco/4:.2f}. Boas compras!')

        if parcelas == 5:
            preco = x+((5.5/100)*x)
            if n == 2:
                print(
                    f'\n O preço final do produto vai ser de R${preco:.2f}, sendo que, cada parcela será de R${(preco/5):.2f}. Boa sorte comprando um celular com preço de Celta!')
            else:
                print(
                    f'O preço final do produto vai ser de R${preco:.2f}, sendo que, cada parcela será de R${preco/5:.2f}. Boas compras!')


print('\n\tBem vindo as casas Python!!!\n')
print('Escolha um produto da nossa galeria:')
print('-'*23)
print('Cod - Nome do produto')
print('-'*23)
print(' 01 - Celular Samsung \n 02 - Celular Apple \n 03 - Celular Motorola')
print('-'*23)
cod = int(input('Qual o "Cod" do produto escolhido? '))


if cod == 1:
    print(f'O valor desse produto é de: R${samsung}')
    qualpreco(1)
if cod == 2:
    print(f'O valor desse produto é de: R${apple}')
    qualpreco(2)
if cod == 3:
    print(f'O valor desse produto é de: R${motorola}')
    qualpreco(3)

print('\nObrigado!')
'''

# Cod 10 -- Atividade 14
'''
temp = float(input('Informe a temperatura em °C: '))
newTemp = (temp*(9/5))+32
print(f'A temperatura de {temp}°C é correspondente a {newTemp}°F! ')
'''

# Cod 11 -- Atividade 15 
'''
dias=int(input('Quantos dias você ficou com o carro? '))
km=float(input('Quantos km você andou com o carro? '))
preco=(dias*60)+(km*0.15)
print(f'O valor do aluguel do carro ficou em: R${preco:.2f}')
'''
