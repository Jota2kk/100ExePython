n = float(input('Digite um numero:  '))
numm = numn = n
nrm = 1
vlm = n
r = str(input('Gostaria de continuar adiconando numeros? utilize C/N'))
while r in "Cc":
    n = int(input('Digite um numero'))
    r = str(input('Gostaria de continuar adiconando numeros? utilize C/N'))
    vlm += n
    nrm += 1
    if n > numm:
        numm = n
    if n < numn:
        numn = n
print('A media entre todos valores digitados é: {} \n O numero maior é: {} \n O numero menor é: {}'.format((vlm/nrm), numm, numn))