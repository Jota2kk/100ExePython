while True:
    tb = int(input('Voce quer a tabuada de que valor? '))
    if tb < 0:
        break
    for c in range (1,11):
        print(f'{tb} x {c}: {tb*c}')
print(f'Numero {tb} nao disponivel para tabuada')