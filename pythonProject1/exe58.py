lista = list()
impares = list()
pares = list()
nm = 0

for c in range(1, 8):
    nm = int(input(f'Digite o valor {c}o: '))
    if nm % 2 == 0:
        pares.append(nm)
    else:
        impares.append(nm)

pares.sort()
impares.sort()
lista.append(pares[:])
lista.append(impares[:])


print(f'esta é sua lista de numeros impares {lista[0]} ')
print(f'Esta é sua lista de numeros pares {lista[1]}')