vl1 = int(input('Qual é o primeiro valor?'))
vl2 = int(input('QUal é o segundo valor?'))
op = 0
while op != 5:
    print('Oque voce gostaria de fazer com esses valores? escolha uma das opções abaixo')
    print('[1] somar \n [2] multiplicar \n [3] maior \n [4] novos numeros \n [5] sair')
    op = int(input('Eu escolho: '))
    if op == 1:
        print(vl1+vl2)
    elif op == 2:
        print(vl1*vl2)
    elif op == 3:
        if vl1 > vl2:
            print('O maior numero é:{}'.format(vl1))
        else:
            print('O maior valor é:{}'.format(vl2))
    elif op == 4:
        vl1 = int(input('Qual é o primeiro valor?'))
        vl2 = int(input('QUal é o segundo valor?'))

