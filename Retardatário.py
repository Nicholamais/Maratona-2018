import sys

x = float(input('Entre com o tempo do piloto mais rápido: \n'))
y = float(input('Entre com o tempo do piloto mais lento: \n'))

if x > y:
    print('O primeiro valor deve ser menor do que o segundo.')
    sys.exit()


# Velocidade angular relativa Wr = 2pi/t1 - 2pi/t2 tal que t1 < t2
# Posição angular O = Wr*t
# 2pi = 2pi*(1/x-1/y)*t
# 1 = (1/x-1/y)*t
# t = 1/(1/x-1/y)
# t = (y*x)/(y-x)
# A volta N é dado por int de t/x
# N = y/(y-x)

print('O encontro se dará na ' , int(y/(y-x)),'ª volta.')
