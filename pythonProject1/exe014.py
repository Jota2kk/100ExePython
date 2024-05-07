from random import shuffle
n1 = str(input('Primeiro aluno'))
n2 = str(input('Segundo aluno'))
n3 = str(input('Terceiro aluno'))
li = [n1, n2, n3]
shuffle(li)
print('a ordem de apresentaçao sera:')
print(li)