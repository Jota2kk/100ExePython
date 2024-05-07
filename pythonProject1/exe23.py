print('------------------------------------------------')
print('Olá, vamos fazer o calculo do seu financiamento?')
print('------------------------------------------------')
vl = float(input('Por favor nos fale o valor da casa desejada.'))
sl = float(input('Qual o seu salario?'))
an = float(input('Em quanto anos voce pretende realizar o financiamento?'))
valorcs = vl / (an * 12)
if valorcs > 30 * sl / 100:
    print('Infelizmente nao poderemos fazer esse financiamento. \n cada parcela coresponde ao valor de: {} \n Superando 30% de seu salario mensal'.format(valorcs))
else:
    print('Parabens seu financiamento foi aprovado. O valor mensal de suas parcelas sera de: {} \n esse valor corresponde a %{} do seu salario mensal'.format(valorcs, (valorcs / sl * 100)))