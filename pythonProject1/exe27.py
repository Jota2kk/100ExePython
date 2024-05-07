ano = int(input('Qual o ano de nascimento do atleta?'))
idd = 2023 - ano
if idd <= 9:
    print('O atleta esta na categoria Mirim')
elif idd > 9 and idd <=14:
    print('O atleta esta na categoria Infantil')
elif idd > 14 and idd <= 19:
    print('O atleta esta na categoria Junior')
elif idd == 20:
    print('O atleta esta na categoria Senior')
elif idd > 20:
    print('O atleta esta na categoria Master')
