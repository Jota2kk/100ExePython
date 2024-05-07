x = float(input('Qual o valor da primeira reta?'))
y = float(input('Qual o valor da segunda reta?'))
r = float(input('Qual o valor da terceira reta'))
if x + y > r and x + r > y and y + r > x:
    print('Voce tem um triangulo')
else:
    print('Voce nao tem um triangulo')