n = 0
cont = 0
s = 0
n = int(input('Digite um número ou[999 para sair] '))
while n != 999:
    cont += 1
    s += n
    n = int(input('Digite um número ou[999 para sair] '))
print('Você digitou {} números e a soma entre eles foi {}.'.format(cont, s))

