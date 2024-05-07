def cm(a, b):
    area = a * b
    print(f'A area de um tereno {la}x{cen} é de {area}m2')


#Programa principal

print('CONTROLE DE TERRENOS')
print('---------------------')
la = float(input('Largura (m): '))
cen = float(input('Comprimento (m): '))
cm(la, cen)