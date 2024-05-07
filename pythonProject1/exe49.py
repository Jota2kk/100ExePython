ttl = qnt = cont = 0
mb = 0
nm1 = ''
while True:
    nm = str(input('Qual o nome do produto: '))
    vl = int(input('Qual o valor do produto: '))
    cn = str(input('Gostaria de adicionar mais produtos? [S/N]: '))
    cont += 1
    qnt += vl
    if vl > 1000:
       ttl += 1
    if cont == 1 or vl < mb:
        mb = vl
        nm1 = nm
    if cn in 'Nn':
        break
print(f'O produto mais barato escolhido é: {nm1} e seu valor é de: {mb}')
print(f'O total gasto na compra é de: {qnt}')
print(f'O total de produtos acima de 1000 é de: {ttl} ')