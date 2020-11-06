'''from math import factorial
print('Digite um número para ')
n = int(input('calcular o seu Fatorial:'))
f = factorial(n)
print('O Fatorial de {} é {}.'.format(n, f))'''#usando o import factorial

print('Digite um número para ')
n = int(input('calcular o seu Fatorial:'))
c = n
f = 1
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' X ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))