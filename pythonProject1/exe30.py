from random import randint
print('VAMOS JOGAR PEDRA PAPEL TESOURA')
pe = int(input('escolha um numero de acordo com qual quer jogar \n (1)PEDRA \n (2)TESOURA \n (3)PAPEL \n'))
com = radint (1, 3)
if (com == 1 and pe == 2) or (com == 2 and pe == 3) or (com == 3 and pe == 1):
    print('Eu escolhi {} e voce escolheu {} eu venci'.format(com, pe))
elif (pe == 1 and com == 2) or (pe == 2 and com == 3) or (pe == 3 and pe == 1)
    print('Voce escolheu {} e eu escolhi {} voce venceu'.format(pe, com))
else:
    print('Eu escolhi {} e voce escolheu {} entao temos um empate'.format(com, pe))









