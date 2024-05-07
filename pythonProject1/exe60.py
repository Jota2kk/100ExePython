matriz = list()
cl1 = list()
cl2 = list()
cl3 = list()
pa = cln3 = mai = vl = 0

#linha 1
for n in range(0, 3):
    vl = (int(input(f'Adicione o elemento {n} da 1 coluna')))
    cl1.append(vl)
    if vl % 2 == 0:
        pa = pa + vl
    if n == 2:
        cln3 = cln3 + vl
matriz.append(cl1[:])

#linha 2
for n in range(0, 3):
    vl = (int(input(f'Adicione o elemento {n} da 2 coluna')))
    cl2.append(vl)
    if vl % 2 == 0:
        pa = pa + vl
    if n == 2:
        cln3 = cln3 + vl
matriz.append(cl2[:])
cl2.sort()

#linha 3
for n in range(0, 3):
    vl = (int(input(f'Adicione o elemento {n} da 3 coluna')))
    cl3.append(vl)
    if vl % 2 == 0:
        pa = pa + vl
    if n == 2:
        cln3 = cln3 + vl
matriz.append(cl3[:])

print('--------------------------------------------')

print(matriz[0])
print(matriz[1])
print(matriz[2])
print(f'a soma dos valores da 3 coluna é: {cln3}')
print(f'a soma dos valores pares é: {pa}')
print(f'o maior valor da segunda linha é: {cl2[2]}')

