from random import randint
print('SORTEADOR DE NUMEROS MEGA SENA')
print('------------------------------')

jgs = int(input('Quantos jogos voce quer que eu sorteie? '))
print('----------------------')
print(f'SORTEANDO {jgs} JOGOS')
print('----------------------')

contj = randint(1, 61)
for c in range(jgs):
    print(f'Jogo {c}: [{contj}]')
