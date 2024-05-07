nm = str(input('qual o seu nome?'))
print('Ola, {}! vamos calcular o seu IMC? \n Por favor preencha os proximos campos com suas informações'.format(nm))
al = float(input('Qual a sua altura, {}? :'.format(nm)))
ps = float(input('Qual o seu peso atual, {}? :'.format(nm)))
imc = ps / (al * al)
if imc < 18.5:
    print('{}, voce esta abaixo do peso recomendado'.format(nm))
elif imc >= 18.5 and imc < 25:
    print('Voce esta no peso ideal')
elif imc >= 25 and imc < 30:
    print('Voce esta acima do peso')
elif imc >= 30 and imc < 40:
    print('Voce esta obessa')
else:
    print('Voce esta com obessidade morbida')

