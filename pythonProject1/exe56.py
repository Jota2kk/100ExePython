nume = list()
imp = list()
par = list()

while True:
    nume.append(int(input('Adicione um valor a lista: ')))
    sn = str(input('Gostaria de continuar? (S/N) \n'))
    if sn in "Nn":
        break

for v in nume:
    if v % 2 == 0:
        par.append(v)
    else:
        imp.append(v)

print(f'Essa é sua lista: {nume}')
print(f'Esses sao os numeros impares na sua lista: {imp}')
print(f'Esses sao os numeros pares na sua lista: {par}')

