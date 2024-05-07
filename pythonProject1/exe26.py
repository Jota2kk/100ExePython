n1 = float(input('Qual a sua primeira nota?'))
n2 = float(input('Qual a sua segunda nota?'))
md = (n1 + n2) / 2
if md >= 7.0:
    print('Parabens voce foi aprovado com a nota {}'.format(md))
elif md < 5.0:
    print('Voce foi reprovado com a nota {}'.format(md))
elif md >= 5.0 and md <= 6.9:
    print('Voce esta de recuperação com a nota {}'.format(md))
