nume = list()
while True:
    nume.append(int(input('Digite um valor para adicionar a lista: ')))
    sn = str(input('Gostaria de adicionar mais um valor? (S/N)'))
    if sn in "Nn":
        break
print(f'A sua lista é: {nume}')
nume.sort(reverse=True)
print(f'Essa é sua lista em ordem decrecente {nume}')

if 5 in nume:
    print('O numero 5 faz parte da lista')
else:
    print('O numero 5 nao faz parte da lista')
