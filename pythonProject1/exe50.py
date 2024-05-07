print('Caixa eletronico')
vl = int(input('Qual valor vai ser sacado? '))
ct50 = 50
ct20 = 20
ct10 = 10
ct1 = 1
tt50 = tt20 = tt10 = tt1 = ttl = 0
while ttl < vl:
    ttl = ttl + ct50
    tt50 += 1
    if ttl + ct50 == vl:
        tt50 += 1
        break
    if ttl < vl:
        ttl = ttl + ct20
        tt20 += 1
        if ttl + ct20 == vl:
            tt20 += 1
            break
    if ttl + ct10 < vl:
        ttl = ttl + ct10
        tt10 += 1
        if ttl + ct10 == vl:
                tt10 += 1
                break
    if ttl < vl:
        ttl = ttl + ct1
        tt1 += 1
        if ttl + tt1 == vl:
            tt1 += 1
            break
print(f'Serao entregues {tt50} notas de 50')
print(f'Serao entregues {tt20} notas de 20')
print(f'Serao entregues {tt10} notas de 10')
print(f'Serao entregues {tt1} notas de 1')




