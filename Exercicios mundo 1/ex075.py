núm = (int(input('Digite um Número: ')),
       int(input('Digite outro Número: ')),
       int(input('Digite mais um  Número: ')),
       int(input('Digite o ultimo Número: ')),)
print(f'Você digitou os valores{núm}')
print(f'O valor 9 apareceu {núm.count(9)}vezes')
if 3 in núm:
    print(f'O valor 3 apareceu na {núm.index(3)+1}ª posição')
else:
    print('O valor 3 não foi digitado em nenhuma posicão')
print('Os valores pares digitados foram: ', end='')
for n in núm:
    if n % 2 == 0:
        print(n, end=' ')
