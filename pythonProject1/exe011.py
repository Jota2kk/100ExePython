ctp = float(input('Cateto oposto:'))
ctd = float(input('Cateto adjascente'))
re = (ctp * ctp) + (ctd * ctd)
print('A hipotenusa é: {:.3f}'.format(re ** (1/2)))