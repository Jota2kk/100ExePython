km = float(input('Qual é a distancia da viagen?'))
pr = km * 0.50
if km > 200:
    print('O valor da passagem vai ser:{}'.format(km * 0.45))
else:
    print('O valor da passagem é {}'.format(pr))
