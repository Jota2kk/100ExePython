mai = 0
men = 0
for pes in range(1,6):
    pe = float(input('Qual o peso da {}z pessoa'.format(pes)))
    if pes == 1:
        mai = pe
        men = pe
    else:
        if pe > mai:
            mai = pe
        if pe < men:
            men = pe
print('O maior peso é de:{}'.format(mai))
