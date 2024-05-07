matriz = list()
cl1 = list()
cl2 = list()
cl3 = list()

for n in range(0, 3):
    cl1.append(int(input(f'Adicione o valor {n,n}')))
matriz.append(cl1[:])

for n in range(0, 3):
    cl2.append(int(input(f'Adicione o valor {n,n}')))
matriz.append(cl2[:])

for n in range(0, 3):
    cl3.append(int(input(f'Adicione o valor {n,n}')))
matriz.append(cl3[:])

print('--------------------------------------------')

print(matriz[0])
print(matriz[1])
print(matriz[2])