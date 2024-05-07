nms = 0
nr = 0
n = int(input('digite um numero: '))
while n != 999:
    nr += 1
    nms += n
    n = int(input('digite um numero: '))
print(nr, nms)