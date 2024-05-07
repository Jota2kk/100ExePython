from random import randint
print('-'*50)
print('VAMOS JOGAR PAR OU IMPAR')
print('-'*50)
nm = randint(1,10)
cont = 0
while True:
    ip = str(input('Voce quer par ou impar? P/I'))
    n = float(input('Digite um valor: '))
    tl = nm + n
    print('-'*50)
    print(f'Voce jogou {n} e o computador jogou {nm} total de: {tl}')
    print('-'*50)
    if ip in "Pp" and tl % 2 == 0:
        print('Parabens voce venceu')
        cont += 1
    elif ip in "Ii" and tl % 2 != 0:
        print(f'Parabens voce venceu')
        cont += 1
    else:
        print(f'Infelizmente voce perdeu, seu total de vitorias foi de: {cont}')
        break