gp = dict()
pess = list()

while True:
    nm = str(input('Nome: '))
    idd = int(input('Idade: '))
    sx = str(input('Sexo: [M/F]'.upper()))
    pess.append(nm)
    pess.append(idd)
    pess.append(sx)
    gp['P1'] = pess[:]
    cn = str(input('Gostaria de continuar? [S/N]'.upper()))
    if cn in "N":
        break
    else:
        pess.clear()
print(gp)