lispes = list()
pessoas = list()
pesoma = pesomn = 0
nomepm = list()
nomepn = list()

while True:
    nm = str(input('Nome: '))
    ps = int(input('Peso: '))
    pessoas.append(nm)
    lispes.append(pessoas[:])
    if ps >= pesoma:
        pesoma = ps
        nomepm.append(nm)
    elif pesomn <= ps:
        pesomn = ps
        nomepn.append(nm)
    sn = str(input('Gostaria de adicionar mais uma pessoa?'))
    if sn in "Nn":
        break

print(f'Ao todo voce cadastrou {len(lispes)}')
print(f'O maior peso foi de {pesoma} de {nomepm} ')
print(f'O menor peso foi de {pesomn} de {nomepn}')

#respota para a adição de nome de pessoas na aula, mais especificamente nos comentarioos
