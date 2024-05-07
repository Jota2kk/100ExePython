an = int(input('Em que ano voce nasceu?'))
idd = 2023 - an
if idd == 17:
    print('Voce esta na idade de se alistar')
elif idd < 17:
    print('Voce ainda nao tem que se alistar. \n volte aqui para se alistar daqui {} anos'.format(17 - idd))
elif idd > 17:
    print('Voce ja passou da idade de se alistar. \n voce esta {} anos atradaso'.format(idd - 17))
