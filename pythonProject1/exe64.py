cnt = dict()
cnt['Nome'] = str(input('Nome: '))
idd = int(input('Ano de nascimento: '))
cnt['Idade'] = 2019 - idd
cnt['ctps'] = int(input('Carteira de trabalho (0 nao tem): '))
if cnt['ctps'] > 0:
    cnt['Contratação'] = int(input('Ano de contratação: '))
    cnt['Salario'] = int(input('Salario: R$: '))
    cnt['Aposentadoria'] = cnt['Contratação'] + 35 - idd
    for c, n in cnt.items():
        print(f'{c} tem o valor {n}')
else:
    for c, n in cnt.items():
        print(f'{c} tem o valor {n}')
