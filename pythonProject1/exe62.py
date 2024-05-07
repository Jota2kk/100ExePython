aluno = dict()
aluno['Nome'] = str(input('Nome:'))
aluno['Media'] = float(input(f'Media de {aluno["Nome"]}: '))
if aluno["Media"] >= 5:
    aluno['Situção'] = "Aprovado"
else:
    aluno['Situação'] = "Retido"
for c, n in aluno.items():
    print(f'{c} é igual a {n}')