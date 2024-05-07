jog = dict()
ligol = list()
totg = 0

jog['Nome'] = str(input('Nome do jogador:   '))
prt = int(input(f'Quantas partidas {jog["Nome"]} jogou?  '))

for c in range(prt):
    gols = (int(input(f'Quantos gols na partida {c}: ')))
    totg += gols
    jog['Total'] = totg
    ligol.append(gols)
    jog['Gols'] = ligol[:]


print('--------------------------------')
print()
for v, c in jog.items():
    print(f'O campo {v} tem o valor {c}')
print()
print('--------------------------------')

print(f'O jogador {jog["Nome"]} jogou {prt} partidas')
for c, g in enumerate(jog['Gols']):
    print(f'Na partida {c}, fez {g} gols ')
print(f'Foi um total de {jog["Gols"]} gols')

