vl = float(input('Qual era a velocidade do carro?'))
mul = (vl - 80) * 7
if vl > 80:
    print('O valor de multa a ser pago é:{} \n e os Km execedentes são: {}'.format(mul, (vl - 80)))
else:
    print('O carro nao ultrapassou o limite de velocidade')
    