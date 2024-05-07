r1 = float(input('Qual a primeira reta?'))
r2 = float(input('Qual a segunda reta?'))
r3 = float(input('Qual a terceira reta?'))
trg = r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1
eql = r1 == r2 == r3
esca = r1 != r2 != r3
if trg == True and trg == eql:
    print('Estas retas podem formar um triangulo Equilatero')
elif trg == True and trg == esca:
        print('Estas retas formam um triangulo')
elif trg:
        print('Essas retas formam um triangulo Isosceles')

