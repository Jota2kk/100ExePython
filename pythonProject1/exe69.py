from random import randint
lvl = list()
def vl(a):
    print('Analisando valores passados...')
    mv = 0
    v = 0
    for c in range(a):
        v = randint(1,10)
        lvl.append(v)
        if v > mv:
            mv = v
    print(f'{lvl}', end=' ')
    print(f'Foram informados {a} valores')
    print(f'O maior valor informado foi: {mv}')
    lvl.clear()



vl(6)
vl(3)
vl(2)
vl(1)
vl(0)