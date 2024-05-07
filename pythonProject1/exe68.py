def cnt(a):
    print('Contagem de 1 ate 10 de 1 em 1')
    cont = 1
    while True:
        print(cont, end=' ')
        cont += 1
        if cont > 10:
            break

def cnt1(b):
    print('Contagem de 10 ate 0 de 2 em 2')
    cont = 10
    while True:
        print(cont, end=' ')
        cont -= 2
        if cont <= -1:
            break

def cntg(i, f, p):
    cont = i
    if i < f:
        if p == 0:
            p = 1
        elif p <= -1:
            p = -p
        while True:
            print(cont, end=' ')
            cont += p
            if cont >= f:
                break
    elif i > f:
        if p == 0:
            p = 1
        elif p <= -1:
            p = -p
        while True:
            print(cont, end=' ')
            cont -= p
            if cont <= (f - 1):
                break

#programa principal
cnt(1)
cnt1(2)
print('Agora é sua vez de personalizar a contagem!')
ini = int(input('Inicio: '))
fi = int(input('Fim: '))
ps = int(input('Passo: '))
cntg(ini, fi, ps)

