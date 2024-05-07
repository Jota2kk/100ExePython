lis = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in lis:
        lis.append(n)
        print('Valor adicionado com sucesso')
    else:
        print('Valor duplicado nao vou adicionar')
    sn = str(input('Gostaria de adiconar mais valores? (S/N) \n'))
    if sn in "Nn":
        break

lis.sort()
print(lis)
