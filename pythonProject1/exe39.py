vl = 0
nv = 0
namevl = 0
medidd = 0
for c in range(1,5):
    print('{} pessoa'.format(c))
    name = str(input('Nome: '))
    idd = int(input('Idade: '))
    sex = str(input('M/F: '))
    medidd += idd
    if idd > vl and sex == "M":
        vl = idd
        namevl = name
    if sex == "F" and idd < 20:
        nv += 1
print('O nome e a idade do homen mais velho são: \n Idade: {} \n Nome: {} \n E ha um total de {} mulheres menores de idade'.format(vl, namevl, nv))
print('A media de idade de todas as pessoas é:{}'.format(medidd / 4))
