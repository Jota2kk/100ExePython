dma = 0
dmn = 0
for pe in range(1, 8):
    nas = int(input('Qual a data de nascimento da {}´ pessoa?'.format(pe)))
    ida = 2023 - nas
    if ida >= 18:
        dma += 1
    else:
        dmn += 1
print('O numero de pessoas menores de idade é de:{} \n e o numero de pessoas maiores de idade é de: {}'.format(dmn, dma))


