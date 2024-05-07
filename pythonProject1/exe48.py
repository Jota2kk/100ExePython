ma = hm = mn = 0
while True:
    id = int(input('DIGITE AQUI A IDADE: '))
    sx = str(input('DIGITE AQUI O SEXO: M/F: '))
    cn = str(input('Gostaria de adiconar mais pessoas? responda com "s" ou "n"'))
    if id >= 18:
        ma += 1
    if sx in 'Mm':
        hm += 1
    if id < 20 and sx in 'Ff':
        mn += 1
    if cn in 'Nn':
        break
print(f'Foram cadastrados {ma} pessoas maiores de 18')
print(f'Foram cadastrados {hm} pessoas do sexo masculino')
print(f'Foram cadastradas {mn} pessoas do sexo feminino menores de 20 anos')
