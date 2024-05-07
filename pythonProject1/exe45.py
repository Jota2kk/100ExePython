vl = vz = 0
while True:
    n = int(input('Digite um numero: '))
    if n == 999:
        break
    vl += n
    vz += 1
print(f'Foram mostrados {vz} e sua soma é:{vl}')