# K é o total de lone
# N é o numero de lotes

# K/n = 2a + b
# A = a*b
# A = a*(K/n - 2a)
# A = a*k/n - 2a^2

# Yvertice = -b^2/(4*a)
# b = k/n e a = 2
# Amax = -((k/n)^2/(-4*2)
# Amax = K^2/(8*n^2)
# Amax = ((K/N)**2/8)

N = int(input('Digite o número de terrenos. \n'))
K = float(input('Quantos metros de lona? \n'))

print('A área máxima para cada terreno é de: {:.2f} m^2'.format((K/N)**2/8))