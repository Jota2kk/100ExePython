from random import randint
print('QUAL NUMERO EU PENSEI?')
nmr = 1
pc = randint (1,10)
jg = int(input('Eu acho que voce pensou no numero: '))
while jg != pc:
    print('Voce errou, tente novamente')
    jg = int(input('Eu acho que voce pensou no numero: '))
    if jg != pc:
        nmr += 1
    if pc == jg:
        print('Parabens voce acertou. Seu numero de tentativas ate acertar foi de:{}'.format(nmr))

