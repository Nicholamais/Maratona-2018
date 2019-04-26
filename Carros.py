x = float(input('Massa do carrinho. \n'))
f1 = float(input('Intensidade da força 1.\n'))
f2 = float(input('Intensidade da força 2 com sentido oposto.\n'))


if f1>f2:
    print('A aceleração é igual a {:.1f} ms^-2 no sentido da força 1'.format(abs((f1-f2)/x)))
else:
    print('A aceleração é igual a {:.1f} ms^-2 no sentido da força 2'.format(abs((f1 - f2) / x)))