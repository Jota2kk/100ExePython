valores = list()
ma = 0
mn = 0
for v in range (0, 5):
    valores.append(int(input(f'Digite um valor para a posição {v}: ')))
    if v == 0:
        ma = mn = valores[v]
    else:
        if valores[v] > ma:
            ma = valores[v]
        if valores[v] < mn:
            mn = valores[v]
print(f'Voce digitou os valores: {valores}')
print(f'O maior valor digitado foi: {ma} e ele esta na posição:')
for l , t in enumerate(valores):
    if t == ma:
        print(f'{l}')
print()
print(f'O menor valor digitado foi: {mn} e ele esta na posição:')
for l , t in enumerate(valores):
    if t == mn:
        print(f'{l}')

