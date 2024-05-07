from random import choice
n1 = str(input('Nome do primeiro aluno'))
n2 = str(input('Nome do segundo aluno'))
n3 = str(input('Nome do terceiro aluno'))
li = [n3, n1, n2]
print('O sorteado é:{}'.format(choice(li)))