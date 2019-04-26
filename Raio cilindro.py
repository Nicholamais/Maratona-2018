C = int(input('Comprimento: \n'))
L = int(input('Largura: \n'))
R1 = int(input('Raio 1: \n'))
R2 = int(input('Raio 2: \n'))

if C>L:
    if 2*R1+2*R2 <= C and 2*R1 <= L and 2*R2<=C:
        print('S')
    else:
        print('N')

else:
    if 2*R1+2*R2 <= L and 2*R1 <= C and 2*R2 <= L:
        print('S')
    else:
        print('N')
