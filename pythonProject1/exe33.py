n = 0
for c in range(0, 501, 2):
    if c % 3 == 0:
        n = n + c
print('a soma de todos os valores é:{}'.format(n))