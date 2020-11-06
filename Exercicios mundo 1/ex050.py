s = 0
cont = 0
for c in range(1, 7):
    n = int(input('Digite o {}º valor:'.format(c)))
    if n % 2 == 0:
        s += n
        cont += 1
print('Você Informou {} numeros e a soma dos Pares foi {}'.format(cont, s))

s = 0
cont = 0
for c in range(1, 7):
    n = int(input('Digite o {}º valor:'.format(c)))
    if n % 2 == 1:
        s += n
        cont += 1
print('Você Informou {} numeros e a soma dos Impares  foi {}'.format(cont, s))
