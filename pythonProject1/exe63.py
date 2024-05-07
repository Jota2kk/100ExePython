from random import randint
from time import sleep
from operator import itemgetter

jg = {'Jogador1': randint(1, 6),
      'Jogador2': randint(1, 6),
      'Jogador3': randint(1, 6),
      'Jogador4': randint(1, 6)
      }
ranking = dict()
for n, v in jg.items():
    print(f'O {n} tirou {v}')
    sleep(1)

print('RANKING')
ranking = sorted(jg.items(), key=itemgetter(1), reverse=True) #para contar apartir de um parametro no caso parametro 1 é = valor de cada item de jg
for p, v in enumerate(ranking):
    print(f'{p + 1} lugar: {v[0]} com {v[1]}.')





