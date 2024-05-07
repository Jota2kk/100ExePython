sl = float(input('Qual é o seu salario atual?'))
if sl > 1250:
    print('Seu novo salario é de: R${}'.format(10 * sl / 100 + sl))
else:
    print('Seu novo salario é de: R${}'.format(15 * sl / 100 + sl))